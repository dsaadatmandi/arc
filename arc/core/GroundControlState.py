from common.utils.listener import RegistrationServer
from arc import logger

class GroundControlState():

    def __init__(self):
        logger.info("Starting GCS...")
        self.start_listener()
        logger.debug("We out here")
        pass
    
    def start_listener(self):
        RegistrationServer()
        return

    def gather_facts(self):
        pass
    
    def register_drone(self):
        pass
    
    def start(self):
        pass
    