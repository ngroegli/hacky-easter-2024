def bruteforce_character(flag, cipher, index):
    try:
        leet = 1337

        l = list(flag)


        for i in range(len(l)):
            l[i] = chr(ord(l[i]) - (leet % 10))

        leet = leet // 10

        for i in range(len(l) // 2):
            l[i] = chr(ord(l[i]) + (leet % 10))
        leet = leet // 10

        for i in range(len(l) // 2, len(l)):
            l[i] = chr(ord(l[i]) - (leet % 10))
        leet = leet // 10

        for i in range(len(l)):
            l[i] = chr(ord(l[i]) ^ (i % (leet % 10)))

        return l[index] == cipher[index]
    except:
        return False


def main():
    flag = "he2024{12345678901234567890123456789}" # length 37
    cipher = "da.,.0w`-vv[evv[luj^&dUZ'pp*pp)cXb'ds"
    
    for i in range(7, 36):
        ch = 0
        while not bruteforce_character(flag, cipher, i):
            ch = ch + 1
            string_list = list(flag)
            string_list[i] = chr(ch)
            flag = "".join(string_list)


        print("Next character for flag found: {0}".format(flag))


if __name__ == "__main__":
    main()