
# Exercises - Day 3
# modules
import math


# Ex1
age = int(39)

# Ex2
height = float(95.3)

# Ex3
complex_number = complex ( 4 + 4j)

# Ex4
print("Área Triángulo")
base2 = float(input ("Introduce la medida de la base : "))
height2 = float(input("Introduce la medida de la altura : "))
area_triangle = ( 0.5 * base2 * height2 )
print("El área del triangulo es : " , area_triangle ) 

# Ex5
print("Perímetro Triángulo ")
side_a = float (input ("Introduce la medida del lado a : "))
side_b = float (input ("Introduce la medida del lado b : "))
side_c = float (input ("Introduce la medida del lado c : "))
perimeter_of_the_triangle = side_a +  side_b + side_c
print("El perímetro del triangulo es : " , perimeter_of_the_triangle )

# Ex6
print("Área & Perímetro Rectángulo ")
length2 = float(input("Introduce la medida de la base : "))
width2 = float(input("Introduce la medida de la altura : "))
area_rectangle2 = (length2) * (width2)
perimeter_rectangle2 = 2 * ((length2) + (width2))
print("El área del rectangulo es : " , area_rectangle2)
print("El perímetro del rectangulo es : " , perimeter_rectangle2)

# Ex7

radius2 = float(input ("Introduce la medida del radio de la circulferencia : "))

area_of_circle2 = math. pi * (radius2) * (radius2)
circum_of_circle2 = math. pi* (radius2)

print("El área de la circunferencia es : " , area_of_circle2)
print("El perímetro de la circunferencia  : " , circum_of_circle2) 

# Ex8 (equation = "y = 2x - 2")

# La ecuación de la línea en su forma pendiente-intersección es 
# de la forma y = mx + b donde "m" es la pendiente y "b" es 
# la intersección en el eje y.
# En la ecuación y = 2x - 2, la pendiente es 2, que es el coeficiente de "x". 
# Por lo tanto, la pendiente de la línea es 2

slope = 2.0
## Calcular la intersección y
y_intercept = -2

# Calcular la intersección x
x_intercept = ( - slope / 2 )

y_intercept = print(" y_intercept es: " , y_intercept)
y_intercept = print(" x_intercept es: " , x_intercept)

#Ex9

#point (2, 2)
p1 = 2
p2 = 2

#point (6,10 )
q1 = 6
q2 = 10

#point (2, 2) & point (6,10 )
euclidean_distance   = math.sqrt((q1-p1)**2 + (q2-p2)**2)


slope2 = (q2 - p2) / (q1- p1)
print("La pendiente es: " , slope2)
print("La distancia euclidea es: " , euclidean_distance)


# Ex10
mayor = (slope > slope2)
igual = (slope == slope2)
menor = (slope < slope2)

print("La pendiente es slope es mayor que slope2 : " , mayor)
print("La pendiente es slope es igual que slope2 : " , igual)
print("La pendiente es slope es menor que slope2 : " , menor)

# Ex11
import math

x = float(input("Introduce el valor de x: "))

y = x ** 2 + 6 * x + 9

print(("La solución de y = (x ** 2) + 6*x + 9 con x="), x, ("es"), y )

#con tendencia de y = 0
a = 1
b = 6
c = 9

#En lugar de calcular la raíz cuadrada utilizando math.sqrt, 
#puede utilizar directamente el operador de exponenciación 
#(** 0.5) para ahorrar algo de tiempo de cómputo

raiz = math.sqrt(b ** 2 - 4 * a * c)
x1 = (-b + raiz) / (2 * a)
x2 = (-b - raiz) / (2 * a)

print("La solución de y = (x ** 2) + 6x + 9 con y=0 es: ", x1)
print("La solución de y = (x ** 2) + 6x + 9 con y=0 es: ", x2)

# Ex12
var1 = len("python")
var2 = len("dragon")
print (var1)
print (var2)

print("la string python es mayor que la string dragon = " , var1 > var2)

# Ex13
print('on' in 'python' and 'on' in 'dragon') 

# Ex14
print('jargon' in 'I hope this course is not full of jargon')
# Ex15
print('jargon' in "I hope this course is not full of jargon.")
# Ex16
print('on' not in 'python' and 'on' in 'dragon') 
# Ex17
num1 = float(input ("Introduce el número a comprobar : ")) 
if num1 % 2 == 0: print("es un número par")  
if num1 % 2 != 0: print("es un número impar") 

# Ex18
my_bool = 7 % 3 
my_bool2 = 2.7
my_bool3 = int (my_bool2)
print(my_bool == my_bool3)
  
# Ex19
print(type("10") == type(10))

# Ex20
print(int(9.8) == 10 )
# Ex21
hours = int(input ("Enter hours: ")) 
rate = int(input ("Enter rate per hour ")) 
salary = hours *  rate
print("Your weekly earning is" ,salary )

# Ex22
years = int(input ("Enter number of years you have lived (100 year max): ")) 
print("You have lived for : " , years * 315576000 , " seconds" )

# Ex23
print("1 1 1 1 1" )
print("2 1 2 4 8" )
print("3 1 3 9 27" )
print("4 1 4 16 64" )
print("5 1 5 25 125" )