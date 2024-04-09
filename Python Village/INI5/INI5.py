# --- Fornecido: Um arquivo com até 1000 linhas --- #
# --- Problema: Retornar somente as linhas nas posições pares --- #

# --- Indicar o arquivo --- #
arquivo = 'rosalind_ini5.txt'

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter as linhas do arquivo --- #
    linhas = txt.readlines()

    # --- Separar as linhas pares --- #
    linhas_pares = linhas[1::2]

    # --- Mostrar a resposta --- #
    for linha_par in linhas_pares:
        print(linha_par, end='')
