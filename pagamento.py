import time


def accettato(value: int) -> bool:
    accettato = value > 0

    print("Hai richeisto un pagamento di", value)
    time.sleep(3)
    if accettato:
        print("Pagamento accettato...")
    else:
        print("Pagamento NON accettato, valore errato...")
    
    return accettato


def eseguito(value: int) -> bool:
    eseguito = accettato(value)
    time.sleep(2)
    if eseguito:
        print("Pagemento ESEGUITO!")
    else:
        print("Pagamento RIFIUTATO!")
    
    print("Fine procedura...")

eseguito(10)

    