from asyncio import protocols
import serial_asyncio
import asyncio
from serial_asyncio import create_serial_connection
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# test
if __name__ == '__main__':
    class Output(asyncio.Protocol):

        def __init__(self):
            super().__init__()
            self._transport = None

        def connection_made(self, transport):
            self._transport = transport
            print('port opened', self._transport)
            self._transport.serial.rts = False
            # self._transport.write(b'Hello, World!\n')

        def data_received(self, data):
            print('data received', repr(data))
            self._transport.write(data)
            if b'\n' in data:
                self._transport.close()

        def connection_lost(self, exc):
            print('port closed')
            self._transport.loop.stop()

        def pause_writing(self):
            print('pause writing')
            print(self._transport.get_write_buffer_size())

        def resume_writing(self):
            print(self._transport.get_write_buffer_size())
            print('resume writing')

async def send_interval(transport):
    while True:
        transport.write(b''.fromhex('00 00 00 00 00 00 00 00 00'))
        await asyncio.sleep(1)

async def main(loop):
    
    coro = create_serial_connection(loop, Output, 'COM7', baudrate=9600)
    task1 = asyncio.create_task(coro)
    transport,protocol = await task1
    transport.write(b''.fromhex('11 11 11 11'))
    task2 = asyncio.create_task(send_interval(transport))
    await task2

loop = asyncio.get_event_loop()
asyncio.run(main(loop))
loop.run_forever()

    # loop = asyncio.get_event_loop()
    # coro = create_serial_connection(loop, Output, 'COM7', baudrate=9600)
    
    # transport, protocol = loop.run_until_complete(coro)
    # # print(b''.fromhex('48 65 6C 6C 6F 2C 20 57 6F 72 6C 64 21 0A '))
    # transport.write(b'11 11 11 11 11 11 11 11')
    # loop.run_forever()
    # loop.close()
