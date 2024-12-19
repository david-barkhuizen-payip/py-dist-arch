from typing import Optional
from sqlalchemy.engine.base import Engine
from model.common import DatabaseEndPoint, Endpoint, QueueEndpoint, Queue, Service
from util.service_base import ServiceDefinition, serve
from services.migration.client import MigrationServiceClient
from util.env import database_endpoint_from_env, endpoint_from_env, queue_endpoint_from_env
from util.db import get_tested_database_engine
from util.queue import wait_for_configured_queue_publisher
from services.create_buy_order.service import api, configure_api
# from services.btc_price.client import BtcPriceServiceClient

def service_definition():

    write_model_db_endpoint: Optional[DatabaseEndPoint] = None
    migration_endpoint: Optional[Endpoint] = None
    migration_client = None
    write_model_engine: Optional[Engine] = None
    pmt_proc_new_pmt_service = None

    def configure_service():
        nonlocal write_model_db_endpoint, migration_endpoint,\
            migration_client, write_model_engine, pmt_proc_new_pmt_service

        migration_endpoint = endpoint_from_env('MIGRATION', no_path = True)
        migration_client = MigrationServiceClient(migration_endpoint)
        migration_client.wait_for_migrations()

        write_model_db_endpoint = database_endpoint_from_env('WRITE_MODEL_DB')        
        write_model_engine = get_tested_database_engine(write_model_db_endpoint)

        btc_price_service = BtcPriceServiceClient(endpoint_from_env('BTC_PRICE', no_path = True))
        
        configure_api(write_model_engine, btc_price_service)

    return ServiceDefinition(Service.CREATE_BUY_ORDER, configure_service, None, api)

serve(service_definition())