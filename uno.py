import time
import os


lista = ["uno", "cane", "tre", "quattro", "cinque"]

squadra = {
    "operai": [
        {"nome": "andrea", "cognome": "prestini"},
        {"nome": "eleonora", "cognome": "favagrossa"},
        {"nome": "filippo", "cognome": "braccagnini"},
        {"nome": "aldo", "cognome": "tanzini"}],
    "amministrazione": [
        {"nome": "elonora", "cognome": "favagrossa"},
        {"nome": "federica", "cognome": "braccagnini"}
    ]
}


print("Stampo squadra Operai")
for val in squadra["operai"]:
    print(f'''nome: {val["nome"]}
cognome: {val["cognome"]}
          ''')
    time.sleep(1)

print("Stampo squadra amministrazione")
for val in squadra["amministrazione"]:
    print(f'''nome: {val["nome"]}
cognome: {val["cognome"]}''')
    time.sleep(1)
