#"a" for append
from time import *
f = open("demofile.txt", "a")
f.write(str(time())+"\n")
f.write("Now the file has more content durin the reboot!")
f.write("\n")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()
