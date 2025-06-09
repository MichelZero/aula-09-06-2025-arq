# autor: Michel
# data: 09/06/2025
#

import psutil

total_RAM = psutil.virtual_memory().total / (1024 ** 3)
total_Disponivel = psutil.virtual_memory().available / (1024 ** 3)
porcentagem_usado = psutil.virtual_memory().percent

print(f"Total de RAM = {total_RAM:.2f} GB")
print(f"Disponível de RAM = {total_Disponivel:.2f} GB")
print(f"Porcentagem usada = {porcentagem_usado:.2f} %")