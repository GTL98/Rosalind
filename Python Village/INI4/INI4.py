# --- Fornecido: Dois números inteiros a e b (a < b < 1000) --- #
# --- Problema: A soma dos números ímpares entre a e b, incluindo b --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.read()

    # --- Obter o número a --- #
    a = int(conteudo.split(' ')[0])

    # --- Obter o número b --- #
    b = int(conteudo.split(' ')[1])

# --- Criar uma lista dos números ímpares --- #
impares = []

# --- Criar um loop para saber quais são os números ímpares --- #
for numero in range(a, b+1):
    # --- Se sobrar 1 da divisão do número com 2, então ele é ímpar --- #
    if numero % 2 == 1:
        # --- Adicionar o número ímpar à lista --- #
        impares.append(numero)

# --- Saber a soma --- #
soma = sum(impares)

# --- Mostrar a resposta --- #
print(soma)
