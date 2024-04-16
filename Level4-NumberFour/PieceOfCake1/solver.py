def solve_rot_with_ascii_and_pi():
    numbers_after_decimal_point_of_pi = "141592653589793238462643383279502884197169399"
    cipher = "ii35;6Ykf|h~j8adgf7ve5uuiw37wflaj}x`9rbgj|7"

    index = 0
    result = ""
    for c in cipher:
        plaintext_char = chr(ord(c) - int(numbers_after_decimal_point_of_pi[index]))
        result = result + plaintext_char
        index = index + 1

    print(result) # he2024{That_wa5_a_b1t_1rrat10nal_but_0kaaay.}


if __name__ == "__main__":
    solve_rot_with_ascii_and_pi()