def int_conv_bin_to_dec(num):
    #Перевод целого двоичного числа в десятичное
    index = len(num) - 1
    result = 0
    for i in num:
        result += int(i) * (2 ** index)
        index -= 1
    return result

def int_conv_dec_to_bin(num):
    #Перевод целого десятичного числа в двоичное
    return bin(num)[2:]

def bin_to_binhex(binary_str):
    #Перевод целого двоичного числа в двоично-шестнадцатеричное
    binhex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    # Дополняем двоичное число до длины кратной 4
    int_part_padded = binary_str.zfill(((len(binary_str) + 3) // 4) * 4)

    # Разбиваем на группы по 4 бита и переводим в шестнадцатеричное число
    binhex_int_part = ''.join([binhex_map[int_part_padded[i:i+4]] for i in range(0, len(int_part_padded), 4)])
    
    return binhex_int_part

if __name__ == "__main__":
   
    binary_num = input("Введите целое двоичное число: ")
    print(f"Двоичное в десятичное: {int_conv_bin_to_dec(binary_num)}")
    
    
    decimal_num = int(input("Введите целое десятичное число: "))
    print(f"Десятичное в двоичное: {int_conv_dec_to_bin(decimal_num)}")
    
    
    binary_for_binhex = input("Введите целое двоичное число для перевода в двоично-шестнадцатеричное: ")
    print(f"Двоичное в двоично-шестнадцатеричное: {bin_to_binhex(binary_for_binhex)}")
