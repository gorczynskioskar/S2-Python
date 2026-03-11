#Oskar Górczyñski, 57785, 8/8
# Zadanie 1
fh = open("zad1.txt", "r")
linie = fh.readlines()
fh.close()
print("Zadanie 1")
print(linie)
print()
fh = open("iris.txt", "r")

# Zadanie 2
iris=[]
print("Zadanie 2")
for i in fh:
    wiersz=[]
    for j in range(0,4):
        wiersz.append(float(i.strip().split(",")[j]))
    iris.append(wiersz)
fh.close()
for i in range(len(iris)):
    print(iris[i])

# Zadanie 3
fh = open("zad3.txt", "w")
print("Zadanie 3")
for i in range(len(iris)):
    if iris[i][0]>5:
        for j in range(len(iris[i])):
            fh.write(str(iris[i][j])+" ")
        fh.write("\n")
fh.close()
print("Zapisano dane do pliku zad3.txt")
print()
# Zadanie 4
from calendar import c
import struct
a=2
a_b = struct.pack('i',a)
a_b_a = struct.unpack('i', a_b)
print("Zadanie 4")
print("a =", a)
print("Na bajty:", a_b)
print("Z bajtow: ", a_b_a[0])

print()
a=2097**101
a_b = a.to_bytes((a.bit_length()+7)//8, 'big')
a_b_a = int.from_bytes(a_b, byteorder='big')
print("a =", a)
print("Na bajty:", a_b)
print("Z bajtow: ", a_b_a)

print()
a=3.5
a_b = struct.pack('f',a)
a_b_a = struct.unpack('f', a_b)
print("a =", a)
print("Na bajty:", a_b)
print("Z bajtow: ", a_b_a[0])

print()
s='Hello World!'
p=bytes(s, encoding='raw_unicode_escape')
s2 = p.decode('raw_unicode_escape')
print("s:", s)
print("Na bajty:", p)
print("Z bajtow:", s2)
print()

#Zadanie 5
import xml.etree.ElementTree as ET
drzewo = ET.parse("pierwszy.xml")
korzen = drzewo.getroot()
print("Zadanie 5")
for element in korzen:
    for child in element:
        print(f"{child.tag}: {child.text}")
print()

# Zadanie 6
print("Zadanie 6")
print(f"{korzen[0][1].tag}: {korzen[0][1].text}")  
print()

# Zadanie 7
print("Zadanie 7")
data = ET.Element("root")
uczelnia = ET.SubElement(data, "Uczelnia")
uczelnia.set("Nazwa", "SIMS")
student1 = ET.SubElement(uczelnia, "student")
student1.set("Nrindeksu", "12333")
student1.text="Anna Kowalska"
student2 = ET.SubElement(uczelnia, "student")
student2.set("Nrindeksu", "23795")
student2.text="Przemyslaw Nowak"
student3 = ET.SubElement(uczelnia, "student")
student3.set("Nrindeksu", "65789")
student3.text="Piotr Pilawka"
fh=open("uczelnia.xml", "wb")
fh.write(ET.tostring(data))
fh.close()
print("Zapisano dane do pliku uczelnia.xml")
print()

# Zadanie 8
fh = open("sklep.xml", "r")
drzewo = ET.parse(fh)
korzen = drzewo.getroot()
print("Zadanie 8")
licznik=0
for element in korzen:
    if element.tag=="vitem": 
        licznik+=1
        print(element.attrib)
        for child in element:
            print(f"{child.tag}: {child.text}")
fh.close()
print()
print(f"Liczba elementow vitem w pliku sklep.xml: {licznik}.")