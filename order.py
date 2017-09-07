import re
from array import *
fl = open('20170907.txt', 'r')
flstr = fl.read()
print("Contenido: \n"+flstr)
num_lines = sum(1 for line in open('20170907.txt'))
#print(num_lines)
numbers = flstr.split()
output = []
while numbers:
    smallest = min(numbers)
    index = numbers.index(smallest)
    output.append(numbers.pop(index))

f = open("order.txt", 'w')
f.write(str(output))
f.close()
print("Los numeros ordenados son: \n")
print(output)
