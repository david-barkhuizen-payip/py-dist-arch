from typing import Optional
from services.test.service import configure_api
from services.merchant_pos_new_checkout.client import MerchantPosNewCheckoutClient
from sqlalchemy.engine.base import Engine
from model.common import DatabaseEndPoint, Endpoint, Service
from util.service_base import ServiceDefinition, launch_uvicorn_server
from services.migration.client import MigrationServiceClient
from util.env import database_endpoint_from_env, endpoint_from_env
from util.db import get_tested_database_engine

def service_definition():

    write_model_db_endpoint: Optional[DatabaseEndPoint] = None
    write_model_engine: Optional[Engine] = None

    migration_endpoint: Optional[Endpoint] = None
    migration_client = None
    
    merchant_pos_new_checkout_service = None

    def configure_service():
        nonlocal write_model_db_endpoint, migration_endpoint, migration_client, write_model_engine, merchant_pos_new_checkout_service

        migration_endpoint = endpoint_from_env('MIGRATION', no_path = True)
        migration_client = MigrationServiceClient(migration_endpoint)
        migration_client.wait_for_migrations()


        
        configure_api(write_model_engine, merchant_pos_new_checkout_service)

    return ServiceDefinition(Service.TEST, configure_service, None)

if __name__ == '__main__':
    launch_uvicorn_server(service_definition())