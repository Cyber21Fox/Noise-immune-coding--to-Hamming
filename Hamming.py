def coding(m):
    print("Кодовое расстояние кода:", len(m))
    all = []
    j = 0
    bit = 4
    res = [int(item) for item in m]
    for i in range(0, (len(res) // 4)):
        part = res[j:bit]
        part.append(res[1] ^ res[2] ^ res[3])
        part.append(res[0] ^ res[2] ^ res[3])
        part.append(res[0] ^ res[1] ^ res[3])
        part.reverse()
        part.append(part.pop(0))
        all.extend(part)
        part.clear()
        j = j + 4
        bit = bit + 4
    print("Кодовая комбинация:", all)

def decoding(m):
    res = [int(item) for item in m]
    nul = (res[0] ^ res[1] ^ res[2] ^ res[3] ^ res[4] ^ res[5] ^ res[6])
    print("Символ старшего разряда:", nul)
    s = []
    r = []
    s.append(res[3] ^ res[4] ^ res[5] ^ res[6])
    s.append(res[1] ^ res[2] ^ res[5] ^ res[6])
    s.append(res[0] ^ res[2] ^ res[4] ^ res[6])
    if (nul == 0) and (s != [0, 0, 0]):
        print("В коде двойная ошибка")
    else:
        print('В коде ошибок нет')


if __name__ == '__main__':
    try:
        print("###### Помехоустойчивое кодирование по Хэммингу ######")
        if int(input("Закодировать сообщение - 1\nПроверить сообщение - 2\nВведите значение: ")) == 1:
            message = list(input("Введите сообщение: "))
            coding(message)
        else:
            message = list(input("Введите сообщение(8 бит): "))
            decoding(message)
    except:
        print("Ошибка ввода!")