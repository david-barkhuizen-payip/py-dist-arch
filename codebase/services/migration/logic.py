import traceback
from model.logevent import DatabaseMigrated, DatabaseMigrationExceptionOccurred, PendingDatabaseMigrationsDetected
from util.db import get_tested_database_engine
from util.env import database_endpoint_from_env
from util.structured_logging import log_event
from yoyo import read_migrations, get_backend
from model.common import DatabaseEndPoint

write_model_db_endpoint = database_endpoint_from_env('WRITE_MODEL_DB')
read_model_db_endpoint = database_endpoint_from_env('READ_MODEL_DB')

def migrate(
    ep: DatabaseEndPoint, 
    relative_folder_path: str
):
    
    try:
        backend = get_backend(f'postgresql://{ep.user}:{ep.pwd}@{ep.host}:{ep.port}/{ep.database}')
        
        migrations = read_migrations(relative_folder_path)

        migrations_to_apply = backend.to_apply(migrations)

        log_event(PendingDatabaseMigrationsDetected(
            database=ep.database,
            pending_migrations=[migration.id for migration in migrations_to_apply]
        ))

        backend.apply_migrations(migrations_to_apply)

        log_event(DatabaseMigrated(
            database=ep.database,
            migrations_applied=[migration.id for migration in migrations_to_apply]
        ))
    except Exception:
        log_event(DatabaseMigrationExceptionOccurred(database=ep.database, info=traceback.format_exc()))
        raise

def get_write_model_db_engine():
    return get_tested_database_engine(write_model_db_endpoint)    

def get_read_model_db_engine():
    return get_tested_database_engine(read_model_db_endpoint)


def before_launching_migration_server():

    read_model_engine = get_read_model_db_engine()
    migrate(read_model_db_endpoint, 'model/migrations/read_model')

    write_model_engine = get_write_model_db_engine()
    migrate(write_model_db_endpoint, 'model/migrations/write_model')