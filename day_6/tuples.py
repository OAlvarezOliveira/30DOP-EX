#Exercises: Level 1


my_tuple =  ()
siblings = ()
family_members = ()



print(type(my_tuple))

my_brothers = ("Miguel", "Ramon", "Juan" , "Alberto" )
my_sisters = ("Laura", "Maria" , "Rosa")
siblings = my_brothers + my_sisters

print(siblings)
print(len(siblings))


siblings = list(siblings)
siblings.append("María Lourdes")
siblings.append("Pepe")
family_members =  tuple (siblings)

print(family_members)
print(type(family_members))

#Exercises: Level 2
siblings = list(siblings)

print(siblings[0])
print(siblings[1])
print(siblings[2])
print(siblings[3])
print(siblings[4])
print(siblings[5])
print(siblings[6])
print(siblings[7])
print(siblings[-1])

fruits = ("Orange", "Apple" ,"Watermelon" )
vegetables = ("Carrot", "Onion" , "Tomatoe" , "Potato" )
animal_products = ("Milk", "Butter", "Cheese", "Yogurt","Meat")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_tp = tuple (food_stuff_tp)
print(type(food_stuff_tp))
food_stuff_tp = list (food_stuff_tp)


middle = int(len(food_stuff_tp)/2) 
print(middle)
if  middle % 2 == 0:
    print(food_stuff_tp[middle] + " " + food_stuff_tp[middle +1] )
else:
    print(food_stuff_tp[middle])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if "Estonia" in nordic_countries:
    print ("Estonia is a nordic country")
else:
    print ("Estonia is not a nordic country")
    
if "Iceland" in nordic_countries:
    print ("Iceland is a nordic country")
else:
    print ("Iceland is not a nordic country")


