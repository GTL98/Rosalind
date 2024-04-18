# --- Dado: uma string de DNA com no máximo 1000 nucleotídeos --- #
# --- Problema: A string de RNA traduzida --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a string de DNA --- #
    dna = txt.read()

# --- Trocar a timina (T) por uracila (U) --- #
rna = dna.replace('T', 'U')

# --- Mostrar a resposta --- #
print(rna)
