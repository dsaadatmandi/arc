import asyncio
from tarfile import REGULAR_TYPES
from arc import logger
from arc.common.utils.UdpServer import UDPRegistrator

class GroundControlState():

    def __init__(self):
        logger.info("Starting GCS...")
        self.tasks = []
        asyncio.run(self.initialize())
        logger.debug("We out here")
        pass
    
    async def initialize(self):
        stop_event = asyncio.Event()
        registrator = UDPRegistrator(stop_event)
        self.tasks.append(self.loop_fast(stop_event))
        async with asyncio.TaskGroup() as tg:
            # first run statically defined tasks
            t1 = tg.create_task(registrator.run_serve(stop_event))
            # then run task list
            for t in self.tasks:
                tg.create_task(t)
        self.tasks = []
        print(t1.result())
        
        logger.info("Completed Tasks")


    def gather_facts(self):
        pass
    
    def register_drone(self):
        pass
    
    def start(self):
        pass
    
    def start_telemetry_listener(self):
        pass

    async def loop_fast(self, stop_event: asyncio.Event):
        while not stop_event.is_set():
            print(5)
            await asyncio.sleep(1)