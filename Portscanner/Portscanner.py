import sys, time
import socket as s

if len(sys.argv) !=3:
    print ("USAGE: ")
    print ("./" + sys.argv[0] + " [IP] + [STARTPORT-ENDPORT]\n")
    sys.exit()

ip = sys.argv[1]
ports = sys.argv[2].split("-")

ts = time.time()
print("SCANNING " + ip + "Ports" + ports[0] + "-" + ports[1])

for port in range(int(ports[0]), int(ports[1]) +1)
print ("Texting Port" + str(port) + "...", end="\r")
soc = s.socket(s.AF_INET, s.SOCK_STREAM)

soc.settimeout(6)
res = soc.connect_ex((ip, port))

if res == 0:
    banner = ""
    if port == 80:
        soc.send(b'GET / HTTP/1.1 \r\n)
    try:
        banner = soc.recv(1024)
        banner = banner.decode("UTF-8", errors="replace").strip()
        if port == 80:
            tmp = banner.split("\n")
            for line in tmp:
                if line.strip().lower().startswith("server"):
                    banner = line.strip
    except:
        pass

    print("Port " + str(port) + "OPEN [" + banner + "]")

soc.close()

td = time.time() - ts
print("Done in " + str(td) + " sec.")