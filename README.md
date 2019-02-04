# 7402-ass4
This application implements a One-Time-Pad in Python.
The keys are generated using the Python secrets module CSPRNG.
Generated keys are written to a seperate output file to ensure quality of key material can be maintained, while being reliably obtained for decryption.

# Usage
```
python3 main.py [e/d] <input_file> <output_file> <key_file>
```
For example, encryption would be done as follows:
```
python3 main.py e plaintext.txt ciphertext.txt key.txt
```
And decryption would be done as follows:
```
python3 main.py d ciphertext.txt decrypted.txt key.txt
```

# Requirements
 - Python 3.6+
