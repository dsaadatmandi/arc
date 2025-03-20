import asyncio
from .core.GroundControlState import GroundControlState
from arc import logger
import sys
import os 

if __name__  == '__main__':
    diradd = os.path.abspath("/Users/milad/code/arc")
    if diradd not in sys.path:
        sys.path.append(diradd)
        print("added to path")
    logger.info("Starting Application")
    gcs = GroundControlState()
