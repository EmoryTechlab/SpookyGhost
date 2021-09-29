import time
import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
ser.flushInput()

def send_angle(x, y):
    ser.write((f'{x:03d},{y:03d}').encode())


if __name__ == "__main__":
    send_angle(180, 0)
