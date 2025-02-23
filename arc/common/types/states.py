from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class State():

    state: str
    error: Optional[RuntimeError]
    lastAction: str
    lastCommand: str
    lastResponse: datetime