import socketserver
from arc import logger
import yaml
import threading


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
        # separate thread required so shutdown doesnt deadlock
        server = socketserver.ThreadingTCPServer((self.ip, self.port), RegistrationHandler)
        server_thread = threading.Thread(target=server.serve_forever())
        server_thread.daemon = True
        server_thread.start()        
        
        
class RegistrationHandler(socketserver.StreamRequestHandler):
    
    def handle(self):
        logger.info("Handling request")
        # self.response = self.rfile.readline()
        print(self.rfile.readline().decode("utf-8"))
        self.wfile.write(bytes("bruh", "utf-8"))
        self.server.shutdown()
        