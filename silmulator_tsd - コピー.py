
import serial
import time
import asyncio
import serial_asyncio

from datetime import datetime
from serial.serialutil import Timeout
ser = serial.Serial()
ser.port = 'COM7'
ser.open()
req = b''
async def wait_request():
    global ser,req
    while True:
        ser.timeout = 10
        
        # from datetime import datetime
        # start = datetime.now()
        req = ser.read_until(size=8)
        # print(datetime.now() - start)
        
        await asyncio.sleep(0.1)
                
async def say_regular(delay, what):
    global ser,req
    while True:
        print(f"{what} {datetime.now().strftime('%X.%f')}")
        if req == b'':
                ser.write(b''.fromhex('00 00 00 00 00 00 00 00'))
        ser.write(req)
        req = b''
        await asyncio.sleep(delay)

async def main():
    task1 = asyncio.create_task(wait_request())

    task2 = asyncio.create_task(say_regular(1,'hello'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task2
    print(f"finished at {time.strftime('%X')}")
    await task1
    
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())



# import logging
# import threading
# import time

# def worker(arg):
#     while not arg["stop"]:
#         logging.debug("worker thread checking in")
        
#         time.sleep(1)

# def main():
#     logging.basicConfig(
#         level=logging.DEBUG,
#         format="%(relativeCreated)6d %(threadName)s %(message)s"
#     )
#     info = {"stop": False}
#     thread = threading.Thread(target=worker, args=(info,))
#     thread_two = threading.Thread(target=worker, args=(info,))
#     thread.start()
#     thread_two.start()

#     while True:
#         try:
#             logging.debug("Checking in from main thread")
#             time.sleep(0.75)
#         except KeyboardInterrupt:
#             info["stop"] = True
#             logging.debug('Stopping')
#             break
#     thread.join()
#     thread_two.join()

# if __name__ == "__main__":
#     main()