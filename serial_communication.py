import time
import serial
import struct
from crc import CrcCalculator, Crc16
import cv2

ser = serial.Serial("COM12", baudrate = 9600, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
counter = 0

data = bytes([0, 1, 0, 6, 1, 0, 1, 0, 0, 1, 2, C])

crc_calculator = CrcCalculator(Crc16.CCITT)
checksum = crc_calculator.calculate_checksum(data)
print(checksum)


# while True:
#     ser.write(b'\x01\x06\x10\x30\x00\x00\x8D\x05')

#     time.sleep(0.1)
#     rx_data = ser.read()
#     print(rx_data)

