import requests

def consume_factor_db_primes(min_digits,perpage):
    for start in range(0, 10000000, perpage):
        url = "http://factordb.com/listtype.php?t=1&mindig={0}&perpage={1}&start={2}&download=1".format(min_digits,perpage,start)
        response = requests.get(url) 
        response.raise_for_status()
        body = response.content.decode()
        numbers = body.split('\n')
        for number in numbers:
            if number[0:120].count('0') + number[0:120].count('1') > 100 and number[0:120].count('1') >= 8:
                f = open("output.txt", "a")
                f.write(number)
                f.write("\n----------------------------------------------------------------------\n")
                f.close()



def main():
    consume_factor_db_primes(27000,500)


if __name__ == "__main__":
    main()