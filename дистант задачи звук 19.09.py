import math
def zad1(rate, time, resolution):
    time = time * 60  #перевод мин в сек
    rate = rate * 1000  #перевод КГц в Гц (только точка)
    v = (rate * time * resolution) / 8  #находим объем памяти в байтах
    return int(v)

def zad2(time1, resolution1, v1 ):
    time1 = time1 * 60  #переводим мин в сек
    v1 = v1 * (1024 ** 2)  #переводим Мегабайты в байты
    rate1 = v1 / (time1 * resolution1 * (8))  #находим частоту в Гц
    return float(rate1)

def zad3(v2, resolution2, rate2):
    v2 = v2 * (1024 ** 3)  #переводим Гигабайты в байты
    time2 = v2 / (rate2 * resolution2 * (8))  #находим время звучания в сек
    return float(time2)


def zad4(v3, resolution3, rate3):
    v3 = v3 * 1024  #переводим Килобайты в байты
    rate3 = rate3 * 1000  #переводим КГц в Гц
    time3 = v3 / (rate3 * resolution3 * (8))  #находим время звучания в сек
    return float(time3)

def zad5(rate4, time4, resolution4):
    time4 = time4 * 60  #перевод минут в сек
    rate4 = rate4 * 1000  #перевод кгц в гц (только с точкой)
    v4 = (rate4 * time4 * resolution4) / 8  #находим объем памяти в байтах
    return int(v4)


if __name__ == "__main__" :
    rate = float(input("частота: "))
    time =  int(input("время в минутах: "))
    resolution = int(input("разрешение: "))   
    print (zad1(rate, time, resolution))
    #v1 = float(input("объем в мб (писать с точкой): "))
    #time1 =  int(input("время в минутах: "))
    #resolution1 = int(input("разрешение: "))   
    #print (zad2(v1, time1, resolution1))
    #v2 = float(input("объем в гб (писать через точку): "))
    #rate2 =  int(input("частота: "))
    #resolution2 = int(input("разрешение: "))   
    #print (zad3(v2, rate2, resolution2))
    #v3 = float(input("объем в кб: "))
    #rate3 =  int(input("частота: "))
    #resolution3 = int(input("разрешение: "))   
    #print (zad4(v3, rate3, resolution3))
    #rate3 = int(input("частота: "))
    #time3 =  int(input("время в минутах: "))
    #resolution3 = int(input("разрешение: "))   
    #print (zad1(rate3, time3, resolution3))




