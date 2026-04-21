import serial
import time
import matplotlib

ser = serial.Serial('COM3', 115200, timeout=1)

time.sleep(2)

while True:
    cmd = input("[1] wlacz diode [2] wylacz diode [3] dioda ma migac [4] miganie diod")
    ser.write(cmd.encode())
