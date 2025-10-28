#Reads CHG file and outputs lines after second iteration of 90 90 90 into new file; SPIN.txt
#input files: CHGCAR
#output files: SPIN
import argparse

parser = argparse.ArgumentParser(description="Arguments for CHG file ",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-chg", nargs='?', default = "./CHG", help="chg file location")
args = parser.parse_args()
config = vars(args)
count=0
count2=0
num2=0
num=0
molName='none'
print("Running code to create SPIN.vasp file")
#Reads CHG file and outputs lines after second iteration of 90 90 90 into new file; SPIN.txt
always_print = False
with open(config["chg"], 'r') as f:
    molName=f.readline()
    for line in f:
        if '   90   90   90' in line:
            count2 += 1
with open(config["chg"], 'r') as f, open("SPIN.vasp", "w") as y:
    for line in f:
        if '   90   90   90' in line and num2<=(count2):
            always_print=False
            num += 1
            num2 += 1
        if molName in line and num==(count2-2):
           always_print=True
           if '   90   90   90' in line:
               always_print=False
        if num == count2:
           print(line, file=y, end='')
           always_print= True
           continue
        if always_print:
            print(line, file=y, end='')
print("Output files: SPIN.vasp")

