#Exercise: Level 1
#Ex1 Check the python version you are using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#Ex2 Open the python interactive shell and do the following operations. The operands are 3 and 4
op_1 = 4
op_2 = 3

print(op_1 + op_2)
print(op_1 - op_2)
print(op_1 * op_2)
print(op_1 % op_2)
print(op_1 / op_2)
print(op_1 ** op_2)
print(op_1 // op_2)

#Ex3 Write strings on the python interactive shell.
your_name = input("Cual es tu nombre? ") 
your_family_name = input ("Cual es tu Apellido? ")
your_country = input("Cual es tu pais? ")
i_am_enjoying_30_days_of_python = input ("Estas disfrutando los 30 días de Python? ")

#Ex4 Check the data types of the following data
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(your_name))
print(type(your_family_name))
print(type(your_country))