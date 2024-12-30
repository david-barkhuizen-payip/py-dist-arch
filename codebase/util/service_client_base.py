import requests
from model.common import Endpoint
from util.web import http_post, url_for_endpoint


class ServiceClientBase:

    def __init__(self, endpoint: Endpoint, TRq, TRsp):
        self.endpoint = endpoint
        self.TRq = TRq
        self.TRsp = TRsp

    def invoke(self, **kwargs):

        rq = self.TRq(**kwargs)

        http_rsp = http_post(
            url=f'{url_for_endpoint(self.endpoint)}', 
            json=rq.dict()
        )

        if http_rsp.status_code != 200: # TODO 201 Created ?
            print(str(http_rsp))
            raise Exception(str(http_rsp))

        return self.TRsp.parse_raw(http_rsp.text)
