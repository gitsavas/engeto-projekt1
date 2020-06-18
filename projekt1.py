'''
author = Juraj
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# definece oddelovace
oddelovac = "-" * 40

# definice userov
credentials = {"bob" : "123" , "ann" : "pass123" , "mike" : "password123" , "liz" : "pass123"}

# privitanie a prihlasenie
print(oddelovac + "\n" + "Welcome to the app. Please log in:")
usern = input("USERNAME: ")
passw = input("PASSWORD: ")

# kotrola ci user exituje, ak ano, tak vyber textu, ak nie probram spadne kvoli key error
if credentials[usern] == passw:
    print(oddelovac + "\n" + "We have 3 texts to be analyzed.")
    volba = input("Enter a number btw. 1 and 3 to select: ")
    print(oddelovac)

# ocisti vybrany text
ocisteny = TEXTS[int(volba) - 1].replace("." , "").replace("," , "")

# rozdely na slova
ocisteny = ocisteny.split()

# vypise kolko je slov
print(f"There are {len(ocisteny)} words in the selected text.")

# zadefinujeme nulove hodnoty pre typy slov
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
suma = 0
dlzka = dict()

# zisti ostatne udaje o slovach
while ocisteny:
    slovo = ocisteny.pop(0)
    if slovo[0].isupper():
        titlecase += 1
    if slovo.isupper():
        uppercase += 1
    if slovo.islower():
        lowercase += 1
    if slovo.isnumeric():
        numeric += 1
        suma = suma + int(slovo)
    # tu vytvory slovnik, kluc je dlzka
    dlzka.setdefault(len(slovo) , 0)
    dlzka[len(slovo)] += 1

# vytlaci vypis o slovach
print(f"""There are {titlecase} titlecase words
There are {uppercase} uppercase words
There are {lowercase} lowercase words
There are {numeric} numeric strings""")

print(oddelovac)

# najpr si usporiada kluce zo slovnika dlzky slova
postupne = list(dlzka)
postupne.sort(reverse=True)

# vytlaci graf
while postupne:
    dlzka_slova = postupne.pop()
    print(f"{dlzka_slova:2} {int(dlzka[dlzka_slova])*'*'} {dlzka[dlzka_slova]}")

print(oddelovac)

# vytlaci sumu cisiel
print(f"If we summed all the numbers in this text we would get: {suma}")

print(oddelovac)