# List

#Ex1
list1 = list ()

#Ex2
list1 = [1, 2, 3, 4, 5, 6 ,7]

#Ex3
print(len(list1))

#Ex4
middle = int(len(list1)/2) 
print(list1[0])
print(list1[middle])
print(list1[-1])

#Ex5
mixed_data_types = list ()
mixed_data_types = ["Oscar", 39, 1.72 , "not married" , "Avda de Zamora" ]

#Ex6
it_companies = list ()
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"] 

#Ex7
print(it_companies)

#Ex8
print(len(it_companies))

#Ex9
middle2 = int(len(it_companies)/2) 
print(it_companies[0])
print(it_companies[middle2])
print(it_companies[-1])

#Ex10
it_companies[1] = "philips"
print(it_companies)

#Ex11
it_companies.append("Samsung")
print(it_companies)

#Ex12
middle2 = int(len(it_companies)/2) 
it_companies.insert(middle2, "Mojan")
print(it_companies)

#Ex13
my_upper = it_companies[1]
my_upper = my_upper.upper()
it_companies[1] = my_upper.upper()
print(it_companies)

#Ex14
joined_companies = "#;".join(it_companies)
print(joined_companies)

#Ex15
check = input ("Comprueba la compañia: ")
print(it_companies.count(check))

#Ex16
print(it_companies.sort())

#Ex17
print(it_companies.reverse())

#Ex18
it_companies = it_companies[3:]
print(it_companies)

#Ex19
it_companies.pop(-4)
print(it_companies)

#Ex20
middle3 = int(len(it_companies)/2) 
middle_companies = (it_companies[middle3])
print(middle_companies)
print(it_companies)

#Ex21
it_companies.remove(it_companies[0])
print(it_companies)

#Ex22
middle4 = int(len(it_companies)/2) 
it_companies.remove(it_companies[middle4])
print(it_companies)

#Ex23
it_companies.pop()
print(it_companies)

#Ex24
it_companies.clear()
print(it_companies)


#Ex25
del it_companies

#Ex26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

#Ex27

full_stack = front_end + back_end
full_stack.insert(4, "Python")
full_stack.insert(4, "SQL")
print(full_stack)

#Exercises: Level 2

#Ex28
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

#Ex29
ages.append(18) #Add the min age
ages.append(27) #Add the max age
ages.sort()
print(ages)

#Ex30
middle4 = int(len(ages)/2) 
print(ages[middle4])

#Ex31
average_ages = sum(ages)/len(ages)
print(average_ages)

#Ex32
age_range = max(ages) - min(ages)
print("The range of the ages is:", age_range)


#Ex33
ages.sort()
min_difference = abs(min(ages) - average_ages)
max_difference = abs(max(ages) - average_ages)

#Ex34
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
countries1 = list()
countries2 = list()
middle5 = int(len(countries)/2)

if  middle5 % 2 == 0:
    countries1 = countries[:middle5]
    countries2 = countries[middle5:]
else:
    countries1 = countries[:middle5 + 1]
    countries2 = countries[middle5:]

#Ex35
scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_item, second_item, third_item, *rest = scandic_countries
print(rest)         



