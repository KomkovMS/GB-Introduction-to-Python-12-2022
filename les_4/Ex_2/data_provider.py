from random import randint as RI


def get_temperature(sensor):
    return RI(-20, 0) if sensor else RI(0, 20)


def get_pressure(sensor):
    if sensor:
        return RI(720, 750)
    else:
        return RI(750, 770)


def get_wind_speed(sensor):
    if sensor == 1:
        return RI(0, 30)
    else:
        return RI(30, 50)


def data_collection(sensor=1):
    return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))
