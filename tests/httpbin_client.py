from decorest import RestClient
from decorest import GET
from decorest import header, query


@header('user-agent', 'decorest user agent test')
@header('accept', 'application/json')
class HttpBinClient(RestClient):
    def __init__(self, endpoint):
        super(HttpBinClient, self).__init__(endpoint)

    @GET('user-agent')
    def user_agent(self):
        """Returns user-agent"""