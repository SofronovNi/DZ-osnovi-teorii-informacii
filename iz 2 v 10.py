import math 

def int_fract(num):
    int_part = ""
    fract_part = ""
    flag = False
    for i in num:
        if i == "." :
            flag = True
            continue
        if not flag:
            int_part += i
        else:
            fract_part += i
    if not flag:
        fract_part = "0"

   
    int_result = int_conv(int_part)
    fract_result = fract_conv(fract_part)

    if fract_result == 0:
        return str(int_result)
    else:
        return f"{int_result}.{str(fract_result)[2:]}"  

def int_conv(num):
    index = len(num) - 1
    result = 0
    for i in num:
        result += int(i) * (2 ** index)
        index -= 1
    return result

def fract_conv(fract_part):
    result = 0.0
    for i, digit in enumerate(fract_part):
        result += int(digit) * (2 ** -(i + 1))
    return result

if __name__ == "__main__":
    num = input("Введите двоичное число: ")
    print(f"Результат: {int_fract(num)}")
