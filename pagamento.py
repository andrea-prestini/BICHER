import time


def pagamento_accettato(value: int) -> bool:
    pagamento_accettato = value > 0

    print("Hai richiesto un pagamento di", value)
    time.sleep(3)
    if pagamento_accettato:
        print("Pagamento accettato..")
    else:
        print("Pagamento NON accettato, valore errato...")
    
    return pagamento_accettato


def pagamento_eseguito(value: int) -> bool:
    eseguito = pagamento_accettato(value)
    time.sleep(2)
    if eseguito:
        print("Pagemento ESEGUITO!")
    else:
        print("Pagamento RIFIUTATO!")
    
    print("Fine procedura...")

pagamento_eseguito(10)
print("-" * 50)
pagamento_eseguito(-10)