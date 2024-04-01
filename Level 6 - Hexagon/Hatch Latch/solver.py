import math

def bruteforc_off_kee(characters_he_with_solution_map):
    first_character = list(characters_he_with_solution_map[0].keys())[0]
    second_character = list(characters_he_with_solution_map[1].keys())[0]

    for i in range(1,5):
        for j in range(1,10000):
           print("Matches value of h? : {0} == {1}".format(str((ord(first_character) - i) ^ j), str(characters_he_with_solution_map[0]['h'])))
           if str((ord(first_character) - i) ^ j) == str(characters_he_with_solution_map[0]['h']):
                print("Matches value of e? : {0} == {1}".format(str((ord(second_character) - i) ^ j), str(characters_he_with_solution_map[1]['e'])))
                if str((ord(second_character) - i) ^ j) == str(characters_he_with_solution_map[1]['e']):
                    print("off ({0}) and kee {1} found!".format(i, j))
                    return {"off": i, "kee": j}
               

def reverse_cipher(cipher, off, kee):
    print("Off: {0}".format(off))
    print("Kee: {0}".format(kee))
    flag = ""
    for character in cipher:
        character_as_float = float(character)
        plaintext_character = (float(off) + character_as_float) ** (1/float(kee))
        print(chr(int(plaintext_character)))
        flag = flag + chr(int(plaintext_character)) 

    return flag


def main():
    bruteforceable_values = [{'h':6255},{'e': 6248}]
    off_and_kee = bruteforc_off_kee(bruteforceable_values)
    flag = reverse_cipher(['6255', '6248', '6181', '6183', '6181', '6203', '6258', '6255', '6203', '6267', '6250', '6255', '6230', '6203', '6250', '6250', '6202', '6200', '6200', '6230', '6254', '6245', '6203', '6241', '6267', '6202', '6251', '6256'], off_and_kee["off"], off_and_kee["kee"])
    print(flag)


if __name__ == '__main__':
    main()