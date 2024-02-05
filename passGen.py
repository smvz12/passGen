import array as arr
import random

lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num = ["1","2","3","4","5","6","7","8","9","0"]
sym = ["!","@","#","$","%","&","^","*","(",")","-","_","=","+","[","]","{","}",":",";","'",",","<",".",">","/","?"]
finalPass = []
fPass = ""

for x in range(27):
    choice = random.randrange(1, 5)
    if choice == 1:
        finalPass.append(lower[random.randrange(0,26)])
    elif choice == 2:
        finalPass.append(num[random.randrange(0,10)])
    elif choice == 3:
        finalPass.append(sym[random.randrange(0,27)])
    elif choice == 4:
        finalPass.append(upper[random.randrange(0,26)])
print(fPass.join(finalPass))