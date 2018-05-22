from time import sleep, strftime, time
import os

def sensor2():
    for j in os.listdir("/sys/bus/w1/devices"):
        if j == "28-01183087f8ff":
            outsidesensor = j
    return outsidesensor

def read(outsidesensor):
    location = "/sys/bus/w1/devices/" + outsidesensor + "/w1_slave"
    file = open(location)
    text = file.read()
    file.close()
    temperatureline = text.split("\n")[1]
    temperaturedata = temperatureline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    return celsius

def outsideTemperature(outsidesensor):
    with open ("outside_temp.csv", "a") as logging:
        temp = read(outsidesensor)
        logging.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

if __name__ == '__main__':
    s2 = sensor2()
    outsideTemperature(s2)
    