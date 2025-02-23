from core.GroundControlState import GroundControlState
from arc import logger

if __name__  == '__main__':
    logger.info("Starting Application")
    gcs = GroundControlState()
    gcs.start()