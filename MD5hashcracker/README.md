# Python MD5 hash cracker

This Python script reads and hashes words from a wordlist, compares them to a given list of MD5 hashes and prints every match.

**FOR EDUCATIONAL PURPOSES ONLY! 
NEVER USE THIS SCRIPT IF YOU DO NOT FULLY UNDERSTAND IT! 
DO NOT ATTEMPT TO VIOLATE LOCAL LAW OR INFLICT ANY DAMAGE!
THE MISUSE OF  THIS SOFTWARE CAN RESULT IN SEVERE CONSEQUENCES! 
I ASSUME NO LIABILITY AND I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED!**

## Usage

**If you want to use all tools or already cloned the whole repository:**

```
git clone https://github.com/lucasvictorbraun/python-hacking-tools

cd python-hacking-tools/MD5hashcracker

python3 MD5hashcrack.py hashlist.txt wordlist.txt
```

**If you only want to use this tool, you have to perform a sparse checkout:**

```
mkdir python-hacking-tools && cd python-hacking-tools #choose any name for the directory

git init

git remote add -f origin https://github.com/lucasvictorbraun/python-hacking-tools

git config core.sparseCheckout true

echo "MD5hashcracker/" >> .git/info/sparse-checkout

git pull origin main

cd python-hacking-tools/MD5hashcracker

python3 MD5hashcrack.py hashlist.txt wordlist.txt
```

## Code
```python
import sys, hashlib, time 
```
Imports sys, hashlib and time.
```python
ts = time.time() 
if len(sys.argv) !=3: 
    print ("USAGE:")
    print ("./" + sys.argv[0] + " [HASHFILE] [WORDLIS] /n")
    sys.exit()
```
Saves starting time in **ts**.

Checks for hashlist and wordlist.

Terminates script if hashlist and wordlist miss.
```python
hashes = set()
with open(sys.argv[1],"r" ) as hashfile:
    for line in hashfile:
        hashes.add(line.strip())
```
Creates set and stores hashes from hashlist.
```python
print("start cracking...")
with open(sys.argv[2], "r") as wordlist:
    for line in wordlist:
        line = line.strip('\n')
        md5_hash = hashlib.md5(line.encode()).hexdigest()
        if md5_hash in hashes:
            print (md5_hash + " == " + line)
```
Prints "starting computation".

Opens wordlist, hashes words and saves them in **md5_hash**.

Prints word and hash if hash is found in hashlist.
```python
td = time.time() - ts
print("Done in " + str(td) + "sec.")
```
Prints time needed to crack all hashes.

## License
Licensed under the [MIT License](https://opensource.org/licenses/MIT).
