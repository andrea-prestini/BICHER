from dataclasses import dataclass
import time

elenco = []

@dataclass
class Operaio:
    id: int 
    nome: str 
    cognome: str 
    paese: str 

    def __post_init__(self):

        if self.id in elenco:
            print("ID già presente...")
        else:
            elenco.append(self.id)


uno = Operaio(101, "andrea", "prestini", "esine")
due = Operaio(102, "mario", "mometto", "gambara")
tre = Operaio(103, "gianfranco", "favagrossa", "leno")
print("Stampo elenco id squadra:")
for val in elenco:
    print(val)
    time.sleep(2)
