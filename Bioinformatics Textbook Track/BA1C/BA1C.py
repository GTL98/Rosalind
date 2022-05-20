## Problema: Uma string de DNA
## Resultado: O reverso complementar da string de DNA

# Importar a bilioteca
import pyperclip  # usar essa bilioteca para copiar automaticamente a resposta_peptideo

# Informar o arquivo usado
arquivo = 'rosalind_ba1c.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    sequencia = doc.read()

# Dicionario com os valores sendo a base complementar das chaves
bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Declarar a variável para armazenar a sequência reversa
sequencia_reversa = ''

# Loop para criar a sequência reversa
for nt in sequencia:
    # Adicionar à "sequencia_reversa" o valor correspondente a chave "nt"
    sequencia_reversa += bases[nt]

# Mostrar a reposta
print(sequencia_reversa[::-1])

# Copiar a resposta_peptideo
pyperclip.copy(sequencia_reversa[::-1])
