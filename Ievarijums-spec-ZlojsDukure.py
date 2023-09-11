import math

appleMass = round(float(input('Ievadiet ābolu daudzumu (kg): ')),2)
sugarPrice = round(float(input('Ievadiet cukura cenu (EUR/kg): ')),2)
proportion = int(input('Ievadiet ābolu daļu no ievārījuma (%): '))

jamMass = round(appleMass/(proportion*0.01),2)
reqSugarMass = jamMass - appleMass
sugarMass = math.ceil(reqSugarMass)
leftoverSugar = int((sugarMass-reqSugarMass)*1000)
endSugarPrice = round((sugarMass*sugarPrice),2)

print(f'''
Čeks
-------------------------
Ievārījuma daudzums: {jamMass} kg
Cukura izmaksas: {endSugarPrice} EUR
Pāri palikušais cukura daudzums: {leftoverSugar} g
''')
