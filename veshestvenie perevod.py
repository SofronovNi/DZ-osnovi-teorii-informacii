def float_conv_bin_to_dec(binary_num):
    # Разделяем целую и дробную части
    if '.' in binary_num:
        int_part, frac_part = binary_num.split('.')
    else:
        int_part, frac_part = binary_num, ''

    # Переводим целую часть из двоичной в десятичную
    int_value = int(int_part, 2)

    # Переводим дробную часть из двоичной в десятичную
    frac_value = 0.0
    for i, bit in enumerate(frac_part):
        frac_value += int(bit) * (2 ** -(i + 1))

    return int_value + frac_value

def float_conv_dec_to_bin(num):
    # Переводим целую часть в двоичное
    int_part = int(num)
    int_bin = bin(int_part)[2:]

    # Переводим дробную часть в двоичное
    frac_part = num - int(num)
    frac_bin = []
    while frac_part and len(frac_bin) < 23:  
        frac_part *= 2
        frac_bit = int(frac_part)
        frac_bin.append(str(frac_bit))
        frac_part -= frac_bit

    
    return int_bin + ('.' + ''.join(frac_bin) if frac_bin else '')

if __name__ == "__main__":
   
    binary_num = input("Введите двоичное число (положительное вещественное): ")
    print(f"Двоичное в десятичное: {float_conv_bin_to_dec(binary_num)}")

    decimal_num = float(input("Введите десятичное число (положительное): "))
    print(f"Десятичное в двоичное: {float_conv_dec_to_bin(decimal_num)}")
