# --- Dado: Uma string de DNA s com até 10 mil nucleotídeos e a proteína p traduzida de s --- #
# --- Problema: A tabela usada para a tradução da proteína (se existir mais de uma solução pode usar qualquer uma --- #

# --- Importar as bibliotecas --- #
from Bio.Seq import translate
from Bio.Data import CodonTable

# --- Indicar o arquivo --- #
arquivo = 'rosalind_ptra.txt'

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.read().split()

    # --- Obter a sequência de DNA --- #
    s = conteudo[0]

    # --- Obter a sequência de proteína --- #
    p = conteudo[1]

# --- Obter os índices das tabelas --- #
tabelas = []
for tabela_id in CodonTable.ambiguous_generic_by_id:
    tabelas.append(tabela_id)

# --- Verificar qual é a tabela correta --- #
for tabela in tabelas:
    prot = translate(
        s,  # sequência de DNA
        table=tabela,  # tabela atual da iteração
        stop_symbol='@'  # caractere de parada
        )

    # --- Retirar o símbolo de parada da proteina --- #
    prot = prot[:-1]

    # --- Mostrar qual é a tabela correta de tradução --- #
    if prot == p:
        print(tabela)
