import os

def solve_rot_with_ascii_and_irrational_number(key, cipher):

    index = 0
    result = ""
    for c in cipher:
        plaintext_char = chr(ord(c) - int(key[index]))
        result = result + plaintext_char
        index = index + 1

    print("Flag {0} for key {1}".format(result,key.replace("\n", "")))


def read_lines_from_subdirectories(root_dir):
    all_keys = []

    # Walk through all subdirectories and files
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            keys_per_file = lambda: None
            keys_per_file.file = file
            keys_per_file.all_lines = []
            file_path = os.path.join(subdir, file)

            # Open each file and read its lines
            with open(file_path, 'r') as f:
                lines = f.readlines()
                keys_per_file.all_lines.extend(lines)

            all_keys.append(keys_per_file)

    return all_keys


if __name__ == "__main__":
    root_directory = './possible_keys'
    all_keys = read_lines_from_subdirectories(root_directory)
    cipher = "he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~"
    for entry in all_keys:
        print("File {0}".format(entry.file))
        for key in entry.all_lines:
            solve_rot_with_ascii_and_irrational_number(key, cipher)

        print("\n")