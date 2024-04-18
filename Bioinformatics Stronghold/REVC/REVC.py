# --- Dado: Uma string de DNA de até 1000 nucleotídeos --- #
# --- Problema: A string reversa complementar --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a string de DNA --- #
    dna = txt.read()

# --- Dicionário com as trocas dos nucleotídeos --- #
dic_nt = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
    }

# --- Criar a string que será a reversa complementar --- #
dna_rc = ''
for nt in dna:
    # --- Colocar na string a base complementar --- #
    dna_rc += dic_nt[nt]

# --- Mostrar a resposta --- #
print(dna_rc[::-1])
