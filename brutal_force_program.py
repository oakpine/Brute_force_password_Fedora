from zipfile import ZipFile

# get list of possible passwords
dictionary = open("dict.txt", "r")
passwords = dictionary.readlines()
# get zip file
zf = ZipFile('./my_secret_texts.zip')

for pw in passwords:
    pw = pw.strip()
    try:
        zf.extractall(pwd=pw.encode('utf-8'))
        print("Password " + pw + " worked!")
        break
    except RuntimeError:
        #if "encrypted" in e.args[0] or "Bad password" in e.args[0]:
        print("Password " + pw + " didn't work")
        continue

dictionary.close()
