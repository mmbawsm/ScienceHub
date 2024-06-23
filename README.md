# ScienceHub

# Este aplicación se encarga de simular el lanzamiento de dados.
# La URL del repositorio ScienceHub es https://github.com/mmbawsm/ScienceHub

import dice
import time

# Definición de la función lanzar_dados
def lanzar_dados(amount, sides):
    resultados = dice.roll(f'{amount}d{sides}')
    print(f'Resultado del lanzamiento de {amount} dado(s) de {sides} caras: {resultados}')

# Bucle que realiza 5 lanzamientos de un dado de 6 caras
for i in range(5):
    lanzar_dados(1, 6)  # Lanza un dado de 6 caras
    time.sleep(5)  # Espera 5 segundos entre lanzamientos



