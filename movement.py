import time
import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

def send_angle(x, y):
    ser.write(','.join([x,y]))
