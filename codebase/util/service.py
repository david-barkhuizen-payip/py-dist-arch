from fastapi.exceptions import HTTPException
import traceback
import uuid
from model.logevent import RequestFailed
from typing import Callable
from util.structured_logging import log_event

def request_handler(TRqModel, callback: Callable):
    
    def handle(*args):
        
        # NEXT determine client_id from stateless header-sourced authentication token
        client_id: int = 1        

        try:
            rsp = callback(client_id, *args)
            return rsp
        except:
            error_reference = uuid.uuid4()
            trace = traceback.format_exc()
            print(trace)
            log_event( 
                RequestFailed(
                    request=TRqModel.__name__,
                    error=trace,
                    reference=str(error_reference)
                )
            )
            raise HTTPException(
                status_code=500, 
                detail=f'reference {error_reference} - {trace}'
            )
    
    return handle