def solve_cipher():
    cipher_as_text = {1: ['t', 'r', 't', 'd', 'c', 't', 'd', 't', 'c', 'd', 'c', 'd', 'r', 'c', 't', 'r', 'd', 'r', 'r', 'l', 't', 'd', 'c', 'r', 'c', 'c', 'r', 'd', 'c', 'd', 'c', 'c', 'r', 'r', 'd', 'd', 'r', 'd', 't'], 2: ['c', 'd', 'c', 'd', 'l', 'r', 'r', 'd', 'r', 'd', 'l', 'c', 'd', 'c', 'd', 'c', 'c', 'r', 'd', 'd', 'c', 'd', 'r', 'c', 'c', 't', 'r', 'l', 'c', 'r', 'c', 'c', 'd', 'c', 'c', 'd', 'c', 'l', 'r'], 3: ['r', 'd', 'd', 'c', 'c', 'r', 'c', 'd', 'c', 'd', 't', 'l', 'r', 'd', 'd', 'c', 'c', 'c', 'd', 'c', 'd', 'c', 'c', 'c', 'r', 'd', 'r', 'c', 'l', 'l', 'c', 'c', 'd', 'r', 'l', 'l', 'c', 'c', 'l'], 4: ['l', 'd', 'r', 'c', 'c', 'r', 't', 'c', 'c', 'r', 'd', 'r', 'c', 'd', 'r', 'c', 'd', 'r', 'd', 'd', 'r', 'c', 't', 'd', 'c', 't', 'd', 't', 'd', 'r', 'c', 'l', 'c', 'r', 'd', 'r', 'c', 'd', 'r'], 5: ['r', 't', 'l', 'c', 'c', 't', 'c', 'c', 'c', 'r', 'd', 'r', 'r', 'd', 'c', 'r', 'l', 't', 'c', 'c', 'r', 'c', 'd', 'd', 'd', 't', 'c', 'r', 'l', 't', 'r', 'd', 't', 't', 'c', 'c', 'r', 'l', 'l'], 6: ['r', 'd', 'r', 'l', 'c', 'c', 'c', 'd', 't', 'l', 't', 'd', 'l', 'c', 'c', 'd', 'l', 'c', 'c', 't', 'r', 't', 'c', 'r', 'r', 'c', 'c', 'c', 'c', 'd', 'c', 'l', 'r', 't', 'c', 'c', 'r', 'd', 'r'], 7: ['c', 'd', 't', 'c', 'd', 'c', 'r', 't', 'l', 'r', 't', 'l', 'c', 'l', 'd', 'c', 'c', 'd', 'r', 'l', 't', 'd', 'c', 'd', 'd', 'c', 'l', 'r', 'd', 'c', 'r', 'r', 'c', 'r', 'r', 't', 'r', 'd', 'r'], 8: ['d', 'd', 'c', 'd', 'l', 'c', 'l', 'd', 'r', 'r', 'd', 'r', 't', 'r', 'r', 'l', 'l', 'c', 'd', 'c', 'd', 't', 'r', 'r', 'c', 'd', 'r', 'l', 't', 'd', 'd', 'd', 'r', 'd', 'l', 'c', 'l', 'd', 'r'], 9: ['d', 't', 'l', 'r', 'c', 't', 'c', 'r', 'c', 'r', 'c', 'l', 'd', 't', 't', 'r', 'd', 'r', 'r', 'd', 'c', 'r', 'd', 'r', 'r', 'd', 'r', 'd', 'c', 'l', 'c', 'l', 'l', 'c', 'c', 't', 'r', 'd', 'c'], 10: ['r', 'd', 'r', 'r', 'r', 'r', 'l', 'c', 'c', 'c', 'd', 'r', 'c', 'c', 'd', 'c', 'd', 'r', 'l', 'c', 'c', 't', 't', 'd', 'c', 'd', 'r', 'c', 'd', 'r', 'd', 'c', 'c', 'c', 'd', 'r', 'l', 'l', 'r'], 11: ['c', 'd', 'r', 'r', 'd', 'c', 'r', 'd', 'r', 'r', 'd', 'r', 'd', 'c', 'd', 'd', 'c', 't', 'c', 'c', 'd', 'd', 'c', 't'], 12: ['t', 't', 'd', 'l', 'c', 'c', 'r', 'l', 'r', 'l', 'd', 'r', 'c', 'l', 'r', 'd', 'l', 'r', 'c', 'l', 'r', 'd', 'c', 'c']}
    eye_direction_based_on_trigrams = {1:[],2:[],3:[],4:[],5:[],6:[]}
    number_based_on_trigrams = {1:[],2:[],3:[],4:[],5:[],6:[]}
    for i in range(1,7):
        line_length = len(cipher_as_text[i])
        pointer_1 = 0
        pointer_2 = 0
        iteration = 1
        while pointer_1 < line_length:
            if iteration == 1:
                eye_direction_based_on_trigrams[i].append(cipher_as_text[i][pointer_1] + cipher_as_text[i][pointer_1+1] + cipher_as_text[i+1][pointer_2])
                pointer_1 = pointer_1 + 2
                pointer_2 = pointer_2 + 1
                iteration = 2
            elif iteration == 2:
                eye_direction_based_on_trigrams[i].append(cipher_as_text[i+1][pointer_2+1] + cipher_as_text[i+1][pointer_2] + cipher_as_text[i][pointer_1])
                pointer_1 = pointer_1 + 1
                pointer_2 = pointer_2 + 2
                iteration = 1

        for entry in eye_direction_based_on_trigrams[i]:
            number_based_on_trigrams[i].append(str(entry).replace('c','0').replace('t','1').replace('r','2').replace('d','3').replace('l','4'))


    print(eye_direction_based_on_trigrams)
    print(number_based_on_trigrams)


def main():
    solve_cipher()


if __name__ == '__main__':
    main()
