from dataclasses import dataclass
from ipaddress import IPv4Address
from arc.common.types.states import State
from arc.channels.channels import Modem

@dataclass
class Drone():

    name: str
    address: IPv4Address
    state: State
    channel: Modem
    
    def __post_init__(self):
        self.channel = Modem(self.address)