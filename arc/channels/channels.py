from arc import logger
from abc import ABC, abstractmethod
from ipaddress import IPv4Address


class Channel(ABC):
    
    @abstractmethod
    async def healthcheck(self):
        return
    
    @abstractmethod
    def send(self):
        return
    
    @abstractmethod
    def handle_response(self):
        return
    
    

class Modem(Channel):
    def __init__(self, address: IPv4Address):
        logger.info('Starting Modem channel.')
        
        pass
    
    async def healthcheck(self):
        logger.debug('Starting Modem healthcheck.')
        pass
    
    def send(self):
        return
    
    def handle_response(self):
        return