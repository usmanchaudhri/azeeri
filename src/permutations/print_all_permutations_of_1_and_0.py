

def print_pattern():
    start = 2
    power = 1
    count = 100
    i = 0
    while count > 0:
        if i == start:
            i = 0
            start = start * 2
            power += 1

        current = format(i, 'b')

        # prefix 0 until the string becomes equal to the power.
        # when generating numbers between 0 -> 4
        # 0 = 0
        # 1 = 1
        # 2 = 10
        # 3 = 11
        # since 0 and 1 are of length 1 we will prefix 0 to both since the power is 2 which means
        # we are generating for two numbers i.e 00, 01, 10, 11
        while len(current) < power:
            current = '0' + current

        print(current)
        count -= 1
        i += 1



if __name__ == "__main__":
    # print(format(1, 'b'))
    # print(type(format(2, 'b')))
    # print(format(4, 'b'))
    # print(format(6, 'b'))
    print_pattern()

    # for i in range(100):
    #     print(format(i, 'b'))
    #     # print(bin(i))

