a = "5"
b = 5
c = 5.5
print(type(a))
print(type(b))
print(type(c))
print(a + a)
vards = input("Ievadi varoņa vārdu: ") 
punkti= int(input("Ievadi bāzes punktus: "))
reizinatajs= float(input("Ievadi reizinātāju: "))
kopa= punkti * reizinatajs
print(vards, "ieguva", kopa, "punktus")
# ValueError radās 9 rindā
# Arī rakstot 1,5 radās ValueError
# Python daļskaitļos vajag punktu, nevis komatu, jo float skaitlis ir ar .