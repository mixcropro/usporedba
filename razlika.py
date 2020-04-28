#RADI SAMO U TXT FORMATU
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()
filename2 = askopenfilename()

#uspoređuje filove i izbaci samo razlicite stvari u novi
#vraca sve osim onoga sto je prisutno u oba filea
f = open(filename, "r")
f1 = open(filename2, "r")
diff = set(f).symmetric_difference(f1)
diff.discard("\n")
f2 = open("razlika.txt", "w")
for line in diff:
    f2.write(line)
f.close()
f1.close()
f2.close()