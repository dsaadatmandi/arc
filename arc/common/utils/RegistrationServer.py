from socket import socket
import socketserver
from typing import cast
from arc import logger
import yaml

class RegistrationServer():
    # TODO: currently this only allows for registration once. can use asyncio server to continuously listen for new registration requests.
    
    def __init__(self):
        logger.debug("Initialising RegistrationServer.")
        self.register_config()
        
    
    def register_config(self):
        with open('config.yml') as stream:
            cfg = yaml.safe_load(stream)
            self.ip: str = cfg['listener']['ip']
            self.port: int = cfg['listener']['port']
            
    def start_server(self):
        # separate thread required so shutdown doesnt deadlock
        # server = socketserver.ThreadingUDPServer((self.ip, self.port), RequestHandler)
        # server_thread = threading.Thread(target=server.serve_forever())
        # server_thread.start()
        
        with SubUDPServer((self.ip, self.port), RequestHandler) as server:
            server.data = None
            while server.data == None:
                server.handle_request()
            logger.debug(server.data)
            return server.data
        
        
class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        server = cast("SubUDPServer", self.server)
        logger.info("Handling request")
        data: bytes = self.request[0].strip()
        client_socket: socket = self.request[1]
        validation = self.validate_response(data)
        if validation:
            client_socket.sendto(data.upper(), self.client_address)
            server.data = data
        else:
            client_socket.sendto(b'\n', self.client_address)

    def validate_response(self, value: bytes) -> bytes | None:
        if value == b'gottem':
            return value
        else:
            return None


class SubUDPServer(socketserver.UDPServer):
    data: bytes | None = None
            
