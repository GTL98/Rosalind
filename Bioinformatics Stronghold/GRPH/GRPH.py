# --- Dado: Coleção de strings de DNA no formato FASTA de até 10 mil nucleotídeos --- #
# --- Problema: Os IDs das sequências que possuem os 3 últimos e os 3 primeiros nucleotídeos iguais --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO

# --- Indicar o arquivo --- #
arquivo = ''

# --- Criar uma lista para armazenar as informações --- #
infos = []

# --- Iterar sobre cada entrada FASTA --- #
for registro in SeqIO.parse(arquivo, 'fasta'):
    # --- Obter o ID --- #
    id_seq = registro.id

    # --- Obter o começo e o final da sequência --- #
    comeco = registro.seq[0:3]
    final = registro.seq[-3:]

    # --- Adicionar ao dicionário as informações --- #
    infos.append([id_seq, comeco, final])


# --- Iterar sobre cada item da lista --- #
for info_1 in infos:
    # --- Obter o ID e a sequência de início --- #
    id_1 = info_1[0]
    seq_1 = info_1[1]

    # --- Criar um segundo loop para comparar a sequência inicial com a final --- #
    for info_2 in infos:
        id_2 = info_2[0]
        seq_2 = info_2[2]

        # --- Verificar se as sequências são iguais --- #
        if seq_1 == seq_2:
            # --- Isso impede que o ID seja da mesma sequência --- #
            if id_1 != id_2:
                # --- Mostrar a resposta --- #
                print(id_2, id_1)
        
