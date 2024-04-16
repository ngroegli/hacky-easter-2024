def display_flag_from_qr_text():
    f = open("flag_qr_only.txt", "r")
    text = f.read()
    print(text.replace('1','█'))



def main():
    display_flag_from_qr_text()


if __name__ == "__main__":
    main()