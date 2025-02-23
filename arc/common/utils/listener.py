import socketserver
from arc import logger
import yaml


class RegistrationServer():
    # TODO: currently this only allows for registration once. can use asyncio server to continuously listen for new registration requests.
    
    def __init__(self):
        logger.debug("Initialising RegistrationServer.")
        self.register_config()
        self.start_server()
        
    
    def register_config(self):
        with open('config.yml') as stream:
            cfg = yaml.safe_load(stream)
            self.ip: str = cfg['listener']['ip']
            self.port: int = cfg['listener']['port']
            
    def start_server(self):
        with socketserver.TCPServer((self.ip, self.port), RegistrationHandler) as server:
            server.serve_forever()
        
            

class RegistrationHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        logger.info("Handling request")
        self.response = self.request.recv()
        print(self.request.recv())
        self.server.shutdown()
        