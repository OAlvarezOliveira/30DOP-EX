 # Day 2: 30 Days of python programming
 
# Variables
 
#Exercises: Level 1

first_name = "Oscar"
last_name =  "Alvarez"
full_name = (first_name + " " + last_name)
country = "España"
city = "Ourense"
age = 39
year = 1983
is_married = False
is_true = False
is_light_on = True
  
a,b,c,d,e,f = 1,2,3,4,5,6

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(is_married)
print(is_true)
print(is_light_on)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Exercises: Level 2

# Ex1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Ex2
(len(first_name))
(len(last_name))
  
# Ex3 
print (len(first_name) > (len(last_name)))
print (len(first_name) == (len(last_name)))
print (len(first_name) < (len(last_name)))

# Ex4
num_one = 5
num_two = 4
    # Ex4 i.
total = num_one + num_two
    # Ex4 ii.    
diff = num_two - num_one
    # Ex4 iii.
product = num_one * num_two
     # Ex4 iv.
division = num_one / num_two
    # Ex4 v.
remainder = num_one % num_two
    # Ex4 vi.
exp = num_one ** num_two
    # Ex4 vii.
floor_division = num_one // num_one

# Ex5
import math
radius1 = 30

area_of_circle = math. pi * radius1 * radius1
circum_of_circle = math. pi* radius1 

radius2 = int(input("Define el radio del circulo cuya area deseas calcular : "))
area_of_circle2 = math. pi * radius2 * radius2
print (area_of_circle2)

# Ex6

first_name = input( "Cual es tu nombre ? ")
last_name = input("Cual es tu apellido ? ")
country = input("En que pais  vives ? ")
city = input("En que ciudad  vives ? ")
age = input("Cual es tu edad ? ")

# Ex7
print (help('keywords'))
