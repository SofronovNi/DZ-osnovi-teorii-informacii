import math
def zad1(n, m,):
    k = 1
    V = n * m * k #находим объем памяти изображения
    return int (V)

def zad2(before, after,):
    result = after / before #находим во сколько раз увеличился объем памяти
    return int (result)

def zad3(nn, mm, vv):
    vv = vv * 1024 * 8 #переводим Килобайты в биты
    k = vv / (nn * mm) #определяем количество цветов
    return int (k)

def zad4 (k, vvv):
    vvv = vvv * 8 #переводим из байтов в биты
    k = math.log2 (k) # сколько бит в одной точке
    mn = vvv / k #количество точек на экране
    return int (mn)
    

if __name__ == "__main__" :
    #n = int (input("ширина: "))
    #m = int (input("высота: "))
    #print (zad1(n, m))
    #before = int (input("количество цветов до: "))
    #after = int (input("количество цветов после: "))
    #print (zad2(before, after))
    #nn = int (input("ширина: "))
    #mm = int (input("высота: "))
    #vv = int (input("объем памяти: "))
    #print (zad3(nn, mm, vv))
    k = int (input("количество цветов: "))
    vvv = int (input("объем памяти: "))
    print (zad1(k, vvv))