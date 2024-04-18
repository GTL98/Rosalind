# --- Dado: Uma string s de até 1000 nucleotídeos --- #
# --- Problema: A quantidade de quantas vezes cada nucleotídeo aparece na string (A, C, G e T) --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Ler o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a string --- #
    dna = txt.read()

# --- Contar quantas adeninas há na string --- #
adenina = dna.count('A')

# --- Contar quantas citosinas há na string --- #
citosina = dna.count('C')

# --- Contar quantas guanina há na string --- #
guanina = dna.count('G')

# --- Contar quantas timinas há na string --- #
timina = dna.count('T')

# --- Mostrar a resposta --- #
print(adenina, citosina, guanina, timina)
