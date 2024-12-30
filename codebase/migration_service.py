from model.common import Service
from services.migration.logic import before_launching_migration_server
from util.service_base import launch_uvicorn_server

if __name__ == '__main__':
    launch_uvicorn_server(
        service=Service.MIGRATION,
        before_launching_rest_server=before_launching_migration_server,
        wait_for_migrations=False
        )