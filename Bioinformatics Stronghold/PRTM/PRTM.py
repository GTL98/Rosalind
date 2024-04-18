# --- Dado: A string p de uma proteína com até 1000 aminoácidos --- #
# --- Problema: A massa total de p. Use a massa monoisotópica --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a sequência da proteína --- #
    p = txt.read()


# --- Criar um dicionário com as massas monoisitópica de cada aminoácido --- #
dic_aa = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
    'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
    'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
    'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
    }

# --- Variável da massa total --- #
massa_total = 0

# --- Somar a massa de cada aminoácido --- #
for aa in p:
    massa_total += dic_aa[aa]

# --- Mostrar a resposta --- #
print(round(massa_total, 3))
