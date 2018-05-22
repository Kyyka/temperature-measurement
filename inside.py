import os

def sensor1():
    for i in os.listdir("/sys/bus/w1/devices"):
        if i == "28-01183085f3ff":
            insidesensor = i
    return insidesensor

def read(insidesensor):
    location = "/sys/bus/w1/devices/" + insidesensor + "/w1_slave"
    file = open(location)
    text = file.read()
    file.close()
    temperatureline = text.split("\n")[1]
    temperaturedata = temperatureline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    return celsius


def insideTemperature(insidesensor):
    if read(insidesensor) != None:
        print("%0.3f" % read(insidesensor))

def kill():
    quit()

if __name__ == '__main__':
    try:
        s1 = sensor1()
        insideTemperature(s1)
    except KeyboardInterrupt:
        kill()