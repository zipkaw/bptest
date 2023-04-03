#0xbeef


def max_input():
    num = input("Введите двухбайтное число( максимальное 65535)")
    if int(num) > 0xFFFF:
        return False
    return True, int(num)
failure = False
while not failure:
    failure, num = max_input()
    byte1 = num & 0xFF
    byte2 = (num >> 8) & 0xFF
    num = byte2 + (byte1 << 8)
    print(f'swapped num is {num}')   
