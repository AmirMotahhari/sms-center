from pyws.server import SoapServer

server = SoapServer(
    service_name = 'smsws',
    tns = 'http://local.host',
    location = 'http://localhost:8000/api/',
)

from pyws.functions.register import register

@register()
def keygen(mobile):
    pass


@register()
def checksent(mobile):
    pass
