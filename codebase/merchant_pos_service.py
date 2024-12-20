from typing import Optional
from services.platform_new_receipt.client import PlatformNewReceiptClient
from services.pmt_proc_new_pmt.client import PaymentProcessorNewCustomerPaymentClient
from sqlalchemy.engine.base import Engine
from model.common import DatabaseEndPoint, Endpoint, Service
from util.service_base import ServiceDefinition, serve
from services.migration.client import MigrationServiceClient
from util.env import database_endpoint_from_env, endpoint_from_env
from util.db import get_tested_database_engine
from services.merchant_pos.service import api, configure_api

def service_definition():

    write_model_db_endpoint: Optional[DatabaseEndPoint] = None
    write_model_engine: Optional[Engine] = None

    migration_endpoint: Optional[Endpoint] = None
    migration_client = None
    
    pmt_proc_new_pmt_service = None
    platform_new_receipt_service = None

    def configure_service():
        nonlocal write_model_db_endpoint, migration_endpoint, migration_client, write_model_engine, pmt_proc_new_pmt_service, platform_new_receipt_service

        migration_endpoint = endpoint_from_env('MIGRATION', no_path = True)
        migration_client = MigrationServiceClient(migration_endpoint)
        migration_client.wait_for_migrations()

        write_model_db_endpoint = database_endpoint_from_env('WRITE_MODEL_DB')        
        write_model_engine = get_tested_database_engine(write_model_db_endpoint)

        pmt_proc_new_pmt_service = PaymentProcessorNewCustomerPaymentClient(endpoint_from_env('PMT_PROC_NEW_PMT', no_path = True))
        platform_new_receipt_service = PlatformNewReceiptClient(endpoint_from_env('PLATFORM_NEW_RECEIPT', no_path = True))
        
        configure_api(write_model_engine, pmt_proc_new_pmt_service, platform_new_receipt_service)

    return ServiceDefinition(Service.CREATE_BUY_ORDER, configure_service, None, api)

serve(service_definition())