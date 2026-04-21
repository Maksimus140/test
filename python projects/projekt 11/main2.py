import serial
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.ion()
ax_list = []
ay_list = []
az_list = []
ax_m_list = []
az_m_list = []
ay_m_list = []

ser = serial.Serial('COM3', 115200, timeout=1)

time.sleep(2)

while True:
    cmd = input("Wpisz 1 [led on] 2 [led off] 3 [MOD_BLINK] 4 [ACC_READ] 5 [MAG_READ]")
    ser.write(cmd.encode())
    data = ser.readline().decode().strip()
    if data:
        print(data)
        ax, ay, az, ax_m, az_m, ay_m = map(int, data.split())
        ax_list.append(ax)
        ay_list.append(ay)
        az_list.append(az)
        if len(ax_list) > 100:
                ax_list.pop(0)
                ay_list.pop(0)
                az_list.pop(0)
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.title("ACC")
        plt.plot(ax_list, label="x")
        plt.plot(ay_list, label="y")
        plt.plot(az_list, label="z")
        plt.subplot(2, 1, 2)
        plt.legend()
        plt.pause(0.01)
        ax_m_list.append(ax_m)
        ay_m_list.append(ay_m)
        az_m_list.append(az_m)
        if len(ax_m_list) > 100:
               ax_m_list.pop(0)
               ay_m_list.pop(0)
               az_m_list.pop(0)

        plt.subplot(2, 1, 2)
        plt.title("MAG")
        plt.plot(ax_m_list, label="x")
        plt.plot(ay_m_list, label="y")
        plt.plot(az_m_list, label="z")
        plt.legend()
        plt.pause(0.01)





    