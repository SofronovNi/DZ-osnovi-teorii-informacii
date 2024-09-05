import math

#def task18(a, b, c, d):
    #i = 2 ** (d / (a*b*c))
    #return int (i)

#if __name__ == "__main__":
    #inp1 = int (input("кол-во страниц: "))
    #inp2 = int (input("кол-во строк: "))
    #inp3 = int (input("кол-во символов: "))
    #inp4 = int (input("кол-во бит: "))
    #print(task1(inp1, inp2, inp3, inp4))

#def task19(a, b):
    #N = (math.log2(a)) / (math.log2(b)) 
    #return float (N)

#if __name__ == "__main__":
    #inp5 = float (input("первая страница: "))
    #inp6 = float (input("вторая страница: "))
    #print(task2(inp5, inp6))

#def task20(a, b):
    #I = a / (math.log2(b))
    #return int (I)

#if __name__ == "__main__":
    #inp7 = int (input("сколько бит: "))
    #inp8 = int (input("сколько символов: "))
    #print(task3(inp7, inp8))

#def task19(a):
    #N = 2 ** a
    #return int (N)

#if __name__ == "__main__":
    #inp9 = int (input("сколько бит: "))
    #print(task4(inp9))

#def task20(a):
    #N = 2 ** a
    #return int (N)

#if __name__ == "__main__":
    #inp10 = int (input("сколько бит: "))
    #print(task5(inp10))

def task7(a, b, c):
    k = (a * b) / (2 ** c)
    return int(k)

if __name__ == "__main__":
    inp1 = int(input("кол-во белой краски: "))
    inp2 = int(input("кол-во синей краски: "))
    inp3 = int(input("сколько бит: "))
    print(task7(inp1, inp2, inp3))