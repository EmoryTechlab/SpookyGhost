import time
import serial

# ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
print("Serial setup...")
ser = serial.Serial(port="/dev/cu.usbserial-10", baudrate=9600)
ser.flushInput()

def send_angle(x, y):
    cmd = f'{x:03d},{y:03d}\n'
    print("Writing: " + cmd)
    ser.write(cmd.encode())


if __name__ == "__main__":
    send_angle(90, 0)
