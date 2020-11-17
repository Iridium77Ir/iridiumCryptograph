# iridiumCryptograph

This is my custom passphrase encryption algorithm. It substitutes, XOR and shifts the message to encrypt it. To use it:  
- > python3 main.py -e True (This encrypts a file - e for encryption) -f test.txt (the file to encrypt, any file will work) -p test (enter the passphrase here)
- This will generate test.txt.icr
- > python3 main.py -d True (This decrypts a file - d for decryption) -f test.txt.icr (the file to decrypt) -p test (enter the passphrase you used before here)
- This will generate dec_test.txt which is the decrypted version of the test.txt.icr file