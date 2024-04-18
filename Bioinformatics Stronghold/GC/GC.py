# --- Dado: No máximo 10 entradas FASTA, com cada uma com no máximo mil nucleotídeos --- #
# --- Problema: O ID da sequência que possui o maior conteúdo GC --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO

# --- Indicar o arquivo --- #
arquivo = ''

# --- Criar as variáveis para armazenar o ID e o valor de GC --- #
id_seq = ''
conteudo_gc = 0

# --- Abrir o arquivo FASTA --- #
for registro in SeqIO.parse(arquivo, 'fasta'):
    # --- Obter a sequência --- #
    sequencia = registro.seq

    # --- Obter o tamanho total da sequência --- #
    k = len(sequencia)

    # --- Contar quantas citosinas e guaninas há na sequência --- #
    citosina = sequencia.count('C')
    guanina = sequencia.count('G')
    total_gc = citosina + guanina

    # --- Cálculo do conteúdo GC --- #
    gc = round((total_gc / k) * 100, 6)

    # --- Verificar se o valor encontrado de GC é maior que o armazenado em "conteudo_gc" --- #
    if gc > conteudo_gc:
        conteudo_gc = gc
        id_seq = registro.id

# --- Mostrar a resposta --- #
print(f'''{id_seq}
{conteudo_gc}''')
