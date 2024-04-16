# Challenge "Dizzazzembly"
<img src="banner.jpg" width="400px" alt="Banner Image" />

Have a look at this dizzazzembly.

When entering the flag, the corresponding program did output:

    da.,.0w`-vv[evv[luj^&dUZ'pp*pp)cXb'ds  

[code.txt](code.txt)

  1           0 LOAD_CONST               0 (1337)
              2 STORE_NAME               0 (leet)

  2           4 LOAD_NAME                1 (input)
              6 LOAD_CONST               1 ('enter the flag:')
              8 CALL_FUNCTION            1
             10 STORE_NAME               2 (flag)

  3          12 LOAD_NAME                3 (list)
             14 LOAD_NAME                2 (flag)
             16 CALL_FUNCTION            1
             18 STORE_NAME               4 (l)

  5          20 LOAD_NAME                5 (range)
             22 LOAD_NAME                6 (len)
             24 LOAD_NAME                4 (l)
             26 CALL_FUNCTION            1
             28 CALL_FUNCTION            1
             30 GET_ITER
        >>   32 FOR_ITER                32 (to 66)
             34 STORE_NAME               7 (i)

  6          36 LOAD_NAME                8 (chr)
             38 LOAD_NAME                9 (ord)
             40 LOAD_NAME                4 (l)
             42 LOAD_NAME                7 (i)
             44 BINARY_SUBSCR
             46 CALL_FUNCTION            1
             48 LOAD_NAME                0 (leet)
             50 LOAD_CONST               2 (10)
             52 BINARY_MODULO
             54 BINARY_SUBTRACT
             56 CALL_FUNCTION            1
             58 LOAD_NAME                4 (l)
             60 LOAD_NAME                7 (i)
             62 STORE_SUBSCR
             64 JUMP_ABSOLUTE           32

  7     >>   66 LOAD_NAME                0 (leet)
             68 LOAD_CONST               2 (10)
             70 BINARY_FLOOR_DIVIDE
             72 STORE_NAME               0 (leet)

  8          74 LOAD_NAME                5 (range)
             76 LOAD_NAME                6 (len)
             78 LOAD_NAME                4 (l)
             80 CALL_FUNCTION            1
             82 LOAD_CONST               3 (2)
             84 BINARY_FLOOR_DIVIDE
             86 CALL_FUNCTION            1
             88 GET_ITER
        >>   90 FOR_ITER                32 (to 124)
             92 STORE_NAME               7 (i)

  9          94 LOAD_NAME                8 (chr)
             96 LOAD_NAME                9 (ord)
             98 LOAD_NAME                4 (l)
            100 LOAD_NAME                7 (i)
            102 BINARY_SUBSCR
            104 CALL_FUNCTION            1
            106 LOAD_NAME                0 (leet)
            108 LOAD_CONST               2 (10)
            110 BINARY_MODULO
            112 BINARY_ADD
            114 CALL_FUNCTION            1
            116 LOAD_NAME                4 (l)
            118 LOAD_NAME                7 (i)
            120 STORE_SUBSCR
            122 JUMP_ABSOLUTE           90

 10     >>  124 LOAD_NAME                0 (leet)
            126 LOAD_CONST               2 (10)
            128 BINARY_FLOOR_DIVIDE
            130 STORE_NAME               0 (leet)

 11         132 LOAD_NAME                5 (range)
            134 LOAD_NAME                6 (len)
            136 LOAD_NAME                4 (l)
            138 CALL_FUNCTION            1
            140 LOAD_CONST               3 (2)
            142 BINARY_FLOOR_DIVIDE
            144 LOAD_NAME                6 (len)
            146 LOAD_NAME                4 (l)
            148 CALL_FUNCTION            1
            150 CALL_FUNCTION            2
            152 GET_ITER
        >>  154 FOR_ITER                32 (to 188)
            156 STORE_NAME               7 (i)

 12         158 LOAD_NAME                8 (chr)
            160 LOAD_NAME                9 (ord)
            162 LOAD_NAME                4 (l)
            164 LOAD_NAME                7 (i)
            166 BINARY_SUBSCR
            168 CALL_FUNCTION            1
            170 LOAD_NAME                0 (leet)
            172 LOAD_CONST               2 (10)
            174 BINARY_MODULO
            176 BINARY_SUBTRACT
            178 CALL_FUNCTION            1
            180 LOAD_NAME                4 (l)
            182 LOAD_NAME                7 (i)
            184 STORE_SUBSCR
            186 JUMP_ABSOLUTE          154

 13     >>  188 LOAD_NAME                0 (leet)
            190 LOAD_CONST               2 (10)
            192 BINARY_FLOOR_DIVIDE
            194 STORE_NAME               0 (leet)

 14         196 LOAD_NAME                5 (range)
            198 LOAD_NAME                6 (len)
            200 LOAD_NAME                4 (l)
            202 CALL_FUNCTION            1
            204 CALL_FUNCTION            1
            206 GET_ITER
        >>  208 FOR_ITER                36 (to 246)
            210 STORE_NAME               7 (i)

 15         212 LOAD_NAME                8 (chr)
            214 LOAD_NAME                9 (ord)
            216 LOAD_NAME                4 (l)
            218 LOAD_NAME                7 (i)
            220 BINARY_SUBSCR
            222 CALL_FUNCTION            1
            224 LOAD_NAME                7 (i)
            226 LOAD_NAME                0 (leet)
            228 LOAD_CONST               2 (10)
            230 BINARY_MODULO
            232 BINARY_MODULO
            234 BINARY_XOR
            236 CALL_FUNCTION            1
            238 LOAD_NAME                4 (l)
            240 LOAD_NAME                7 (i)
            242 STORE_SUBSCR
            244 JUMP_ABSOLUTE          208

 17     >>  246 LOAD_NAME               10 (print)
            248 LOAD_CONST               4 ('')
            250 LOAD_METHOD             11 (join)
            252 LOAD_NAME                4 (l)
            254 CALL_METHOD              1
            256 CALL_FUNCTION            1
            258 POP_TOP
            260 LOAD_CONST               5 (None)
            262 RETURN_VALUE
None


# Solution
The encoded flag "da.,.0w`-vv[evv[luj^&dUZ'pp*pp)cXb'ds" is 37 characters long.

With the help of ChatGPT I could decompile the code:

[code_translated.py](code_translated.py)

Then I wrapped the code in a function, which checks each next character if it matches the output. The inner loop iterates the character for each index as long as the flag is not found:

[solver.py](solver.py)

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

## The flag
    he2024{d1zz_izz_pyth0n_d1zz4zz3mbl1n}
