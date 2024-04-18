# --- Dado: Uma string s de RNA de até 10 mil nucleotídeos --- #
# --- Problema: A proteína codificada por s --- #

# --- Importar a biblioteca --- #
from Bio.Seq import Seq

# --- Indicar o arquivo usado --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter a sequência de RNA --- #
    rna = Seq(txt.read())

# --- Traduzir para proteína --- #
proteina = rna.translate(to_stop=True)

# --- Mostrar a resposta --- #
print(proteina)
