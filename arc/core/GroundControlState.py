from arc.common.utils.RegistrationServer import RegistrationServer
from arc import logger


class GroundControlState():

    def __init__(self):
        logger.info("Starting GCS...")
        self.start_listener()
        logger.debug("We out here")
        pass
    
    def start_listener(self):
        server = RegistrationServer()
        data = server.start_server()
        print(data)
        pass

    def gather_facts(self):
        pass
    
    def register_drone(self):
        pass
    
    def start(self):
        pass
    
    def start_telemetry_listener(self):
        pass