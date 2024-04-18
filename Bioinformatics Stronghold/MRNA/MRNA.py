# --- Dado: Uma string de com até mil aminoácidos --- #
# --- Problema: O número total de diferentes mRNA que podem ter gerado a tradução. A resposta é sobre o módulo de um milhão --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a sequência de aminoácidos --- #
    aminoacidos = txt.read()

    # --- Adicionar o stop codon --- #
    aminoacidos += '*'


# --- Criar um dicionário com os aminoácidos e em quantos códons eles podem ser traduzidos --- #
dic_aa = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
    'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
    'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
    'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2, '*': 3
    }

# --- Salvar as possibilidades --- #
p = 1

# --- Obter a quantidade de quantas maneiras o aminoácido pode ser traduzido --- #
for aa in aminoacidos:
    p *= dic_aa[aa]

# --- Mostrar a resposta --- #
print(p%1_000_000)
