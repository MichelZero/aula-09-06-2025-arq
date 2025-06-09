# autor: Michel
# data: 09/06/2025
#

import psutil # Biblioteca psutil é usada para obter informações sobre o sistema
# Instalação: pip install psutil

# psutil.virtual_memory() retorna um objeto com informações sobre a memória virtual do sistema
# total: Total de memória RAM do sistema
total_RAM = psutil.virtual_memory().total / (1024 ** 3)
# 1024 ** 3 converte bytes para gigabytes
# 1024 ** 3 = 1024 * 1024 * 1024

total_Disponivel = psutil.virtual_memory().available / (1024 ** 3)
porcentagem_usado = psutil.virtual_memory().percent


# Exibe as informações de memória formatadas
# :.2f formata o número para duas casas decimais
# se quiser mais casas decimais, basta alterar o número após o ponto
# .3f formata o número para três casas decimais 
# f-strings são usadas para formatar strings de forma mais legível
print("Informações de Memória:")
print(f"Total de RAM = {total_RAM:.2f} GB")
print(f"Disponível de RAM = {total_Disponivel:.2f} GB")
print(f"Porcentagem usada = {porcentagem_usado:.2f} %")