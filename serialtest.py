import serial
from serial.serialutil import Timeout
with serial.Serial() as ser:
    # ser.baudrate = 
    ser.port = 'COM7'
    ser.open()
    ser.write(b'hello')
    for i in range(8):
        can_byte = ser.read_until(size=8)
        print(ser.read_until(size=8))
        