# Python Portscanner

This Python script is a information gathering tool.

It scans a server for open ports, their services and their banners.

Its purpose is to show you how a Portscanner works.

**FOR EDUCATIONAL PURPOSES ONLY! 
NEVER USE THIS SCRIPT IF YOU DO NOT FULLY UNDERSTAND IT! 
DO NOT ATTEMPT TO VIOLATE LOCAL LAW OR INFLICT ANY DAMAGE!
THE MISUSE OF  THIS SOFTWARE CAN RESULT IN SEVERE CONSEQUENCES! 
I ASSUME NO LIABILITY AND I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED!**

## Usage

**If you want to use all tools or already cloned the whole repository:**

```
git clone https://github.com/lucasvictorbraun/python-hacking-tools

cd python-hacking-tools/Portscanner

python3 Portscanner.py [IP Adress] startport-endport
```

**If you only want to use this tool, you have to perform a sparse checkout:**

```
mkdir python-hacking-tools && cd python-hacking-tools #choose any name for the directory

git init

git remote add -f origin https://github.com/lucasvictorbraun/python-hacking-tools

git config core.sparseCheckout true

echo "Portscanner/" >> .git/info/sparse-checkout

git pull origin main

cd python-hacking-tools/Portscanner

python3 Portscanner.py [IP Adress] startport-endport
```

## Code

```python
import sys, time
import socket as s
```

Imports sys, time and socket.

```python
if len(sys.argv) !=3:
    print ("USAGE: ")
    print ("./" + sys.argv[0] + " [IP] + [STARTPORT-ENDPORT]\n")
    sys.exit()
```

Checks for arguments.

```python
ip = sys.argv[1]
ports = sys.argv[2].split("-")
```

Assigns the arguments to the corresponding variables.

```python
ts = time.time()
print("SCANNING " + ip + "Ports" + ports[0] + "-" + ports[1])
```

Saves starting time in ts.

Prints server ip and ports.

```python
for port in range(int(ports[0]), int(ports[1]) +1)
print ("Texting Port" + str(port) + "...", end="\r")
soc = s.socket(s.AF_INET, s.SOCK_STREAM)
```

Runs through all of the ports.

Notice: end needs +1, otherwise the scan would end to soon.

Prints current port number (the end="\r" makes the cursor jump back).

```python
soc.settimeout(6)
res = soc.connect_ex((ip, port))
```

Defines socket and connects to server.

Generates Status-Code stored in res.

```python
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

```

If res = 0 (port is open) we delete the last operation's banner value with the empty string.

Sends HTTP request if port = 80.

Tries to recieve 1024 Bytes (enough for SSH or FTP).

Splits banner if port = 80 and looks for the line that starts with "server".

Prints open ports and banners.

```python
td = time.time() - ts
print("Done in " + str(td) + " sec.")
```

Prints time passed.

## License
Licensed under the [MIT License](https://opensource.org/licenses/MIT).
