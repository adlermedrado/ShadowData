from shadow_data.cryptohash.symmetric_cipher import Symmetricfrom torch.distributions.constraints import symmetric

# Symmetric encryption

This simple encryption and decryption approach use symmetric cryptography
Basically the user can generate a encryption key and use it to encrypt and decrypt data.

**The key management is user's responsability, ShadowData don't save any kind of keys or credentials.**

## How to use

```python
from shadow_data.cryptohash.symmetric_cipher import Symmetric
symmetric = Symmetric()
key = symmetric.create_key() # Generate a new key. It can be saved at a safe place to be used later
print(f"Key: {key}")


content = "Hello World!"
encrypted_content = symmetric.encrypt(content)
print(f"Encrypted: {encrypted_content}")

decrypted_content = symmetric.decrypt(encrypted_content)
print(f"Decrypted: {decrypted_content}")
```
### Results
```plain
Key: b'bpSGcODTJ1iOwxloIQJrAiYDRaqyypdCsQfg1EwVOTc='
Encrypted: b'gAAAAABnDAexPmKZ0Bh9U4KH7iv_OsHQ1p2ijjJjdHYbagZ-xdyWRT5ChcAw_gVSwfPhE-HG4aZd2xG02123UPTVeJm3nSTF0w=='
Decrypted: Hello World!
```

## If the key was already created

```python
from shadow_data.cryptohash.symmetric_cipher import Symmetric
key = b'bpSGcODTJ1iOwxloIQJrAiYDRaqyypdCsQfg1EwVOTc='
symmetric = Symmetric()
symmetric.cipher_key = key
content = "Hello World"
encrypted = symmetric.encrypt(content)
decrypted = symmetric.decrypt(encrypted)
print(f"Encrypted using key {key}: {encrypted}")
print(f"Decrypted using key {key}: {decrypted}")

```

### Results:
```
Encrypted using key b'bpSGcODTJ1iOwxloIQJrAiYDRaqyypdCsQfg1EwVOTc=': b'gAAAAABnDAi8t8YvtEPlmdtvwL5t-P31db82r49yjIfX-HhQGxK0Sd3_IpxrvD3PiajyOSm835OpfcXFQ1kHkAlt1EzqXNBInA=='
Decrypted using key b'bpSGcODTJ1iOwxloIQJrAiYDRaqyypdCsQfg1EwVOTc=': Hello World
```