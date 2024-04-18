# --- Dado: 2 strings de DNA de mesmo tamanho de no máximo mil nucleotídeos --- #
# --- Problema: A distância de Hamming entre as duas sequências --- #

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter as sequências de DNA --- #
    seq_1 = conteudo[0].strip()
    seq_2 = conteudo[1].strip()

# --- Contador da distância de Hamming --- #
hamm = 0

# --- Comparar nucleotídeo com nucleotídeo --- #
for nt_1, nt_2 in zip(seq_1, seq_2):
    # --- Verificar se o nucleotídeo de uma sequência é diferente do nucleotídeo da outra --- #
    if nt_1 != nt_2:
        hamm += 1

# --- Mostrar a resposta --- #
print(hamm)
