import hashlib
import sys

#64KB in bytes
BUF_SIZE = 65536

# Initializing the sha256() method
sha256 = hashlib.sha256()

file = sys.argv[1]

with open(file, 'rb') as f:
    data = f.read(BUF_SIZE)
    while data:
        sha256.update(data)
        data = f.read(BUF_SIZE)

print(sha256.hexdigest())
    