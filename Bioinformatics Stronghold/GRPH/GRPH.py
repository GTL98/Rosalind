## Problema: Uma coleção de cadeias de DNA no formato FASTA com comprimento total de 10 kb
## Resultado: A lista_pedacos dos IDs do arquivo FASTA correspondentes O3. A resposta pode ser
## devolvida em qualquer ordem

# Importar a bilioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_grph.txt'

# Criar um dicionário para armazenar as sequências e seus IDs
registros = {str(registro.seq): registro.id for registro in SeqIO.parse(arquivo, 'fasta')}

# Verificar qual sequência é a continuação de qual, respeitando que os 3 últimos nucleotídeos
# de uma sequência são iguais aos 3 primeiros nucleotídeos de outra sequência
for chave_1 in registros.keys():
    for chave_2 in registros.keys():
        # Isso evita que a mesma sequência seja considerada diferente se o começo for igual ao final
        if chave_1 != chave_2:
            if chave_1[-3:] == chave_2[:3]:
                # Como a resposta é muito grande, a melhor solução é escrevê-la em um arquivo
                with open('resposta_grph.txt', 'a') as txt:
                    txt.write(registros[chave_1])
                    txt.write(' ')
                    txt.write(registros[chave_2])
                    txt.write('\n')
