import qrGen as qr
import os
import sys
import colorGen as colG

content = ""
if len(sys.argv) > 2 :
    # if more than one Command Line Arguments are not used
    print("USAGE : \n"+
          "python3(or python) main.py [qr content]\n"
          "OR\n"
          "python3(or python) main.py")
    exit()
elif len(sys.argv)  == 2:
    # if Command Line Arguments are not used
    content = sys.argv[1]
    print(f"Qr code for content({content}) is being created...")
else:
    # if content was not specifyed yet
    content = input("Enter the qr content : ")



path = qr.createQR_Advanced(content, bgColor="black", fillColor=colG.generateColor())
os.startfile(path)