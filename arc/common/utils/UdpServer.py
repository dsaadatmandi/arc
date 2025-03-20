import asyncio
from typing import Optional, cast
from arc import logger

HOST, PORT = 'localhost', 1234

class UdpReceiver(asyncio.BaseProtocol):
    def __init__(self, stop_event: asyncio.Event, result_future: asyncio.Future) -> None:
        self.transport = None
        self.message = ""
        self.build_final_message = ""
        self.stop_event = stop_event
        self.result_future = result_future

    def connection_made(self, transport) -> None:
        self.transport = transport

    def connection_lost(self, exc: Optional[Exception]):
        logger.info(f"Connection has been lost. Optional error message: {exc}")
    
    def datagram_received(self, data: bytes, addr: str) -> None:
        logger.info(f"Received {data} from {addr}")

        validation = self.validate_message(data)

        if not validation:
            logger.info("Received message that is not stop event.")
            self.build_final_message += self.message
            return
        
        logger.debug("Shutting down registration server due to successful receiving stop message.")
        # self.transport.sendto(data, addr)

        if not self.result_future.done():
            self.result_future.set_result(self.build_final_message)

        self.stop_event.set()

    def validate_message(self, data: bytes) -> bool:
        try:
            msg = data.decode("UTF-16")
            logger.debug(msg)
            if msg == "end":
                logger.debug("Received stop message.")
                return True
            else:
                self.message = msg
                return False
        except UnicodeDecodeError:
            logger.warning("Response is not UTF-16 decodable.")
            return False
        except:
            logger.warning("Uncaught error when trying to parse response.")
            return False


class UDPRegistrator():
    def __init__(self, stop_event: asyncio.Event) -> None:
        logger.info("Created UDP Registrator Object.")

    async def run_serve(self, stop_event: asyncio.Event) -> str:
        loop = asyncio.get_running_loop()
        result_future = loop.create_future()

        transport, protocol = await loop.create_datagram_endpoint(
            lambda: UdpReceiver(stop_event, result_future), local_addr=('127.0.0.1', PORT)
        )

        try:
            result = await result_future
        finally:
            transport.close()

        return result



