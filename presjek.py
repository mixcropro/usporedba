#RADI SAMO U TXT FORMATU
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()
filename2 = askopenfilename()

#uspoređuje filove i izbaci samo razlicite stvari u novi
#vraca sve sto se poklapa
f = open(filename, "r")
f1 = open(filename2, "r")
isti = set(f).intersection(f1)
isti.discard("\n")
f2 = open("presjek.txt", "w")
for line in isti:
    f2.write(line)
f.close()
f1.close()
f2.close()