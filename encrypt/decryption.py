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
    