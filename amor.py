import time

def mensagem_romantica():
    frase = "Eu te amo <3"
    for letra in frase:
        print(letra, end='', flush=True)
        time.sleep(0.5)  # Pausa de meio segundo entre cada letra
    print()  # Nova linha após a mensagem

if __name__ == "__main__":
    print("Preparando uma surpresa...")
    time.sleep(2)  # Pausa antes de mostrar a mensagem
    mensagem_romantica()
