import time
import random

def lanzar_dados(amount, sides):
    resultados = []
    for i in range(amount):
        resultado = random.randint(1, sides)
        resultados.append(resultado)
        print(f"Lanzamiento {i+1} número obtenido {resultado}")
        time.sleep(5)
    return resultados

if __name__ == "__main__":
    lanzar_dados(5, 6)
