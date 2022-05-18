## Problema: Seis inteiros não negativos que não excedem 20.000. Os inteiros correspondem ao número
## de casais em uma população que possui cada par de genótipos para um determinado fator
## Resultado: O número esperado de descendentes exibindo o fenótipo dominante na próxima geração,
## supondo que cada casal tenha exatamente dois descendentes

# Informar o arquivo usado
arquivo = 'rosalind_iev.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Criar uma lista_pedacos com a população de cada genótipo
    inteiros = [int(num) for num in doc.read().split()]
    # Criar uma lista_pedacos com cada genótipo
    genoma = ['AA_AA', 'AA_Aa', 'AA_aa',
              'Aa_Aa', 'Aa_aa', 'aa_aa']
    # Criar um dicionário para armazenar as chaves sendo o genótipo e os valores, a população
    dic_genoma = dict.fromkeys(genoma)
    for posicao, genotipo in enumerate(genoma):
        dic_genoma[genotipo] = inteiros[posicao]

# Determinar o número de descendentes
descendentes = 2

# Criar um dicionário com as probabilidades dos pais gerarem filhos com ao menos um alelo dominante
probabilidades = {
    'AA_AA': 1, 'AA_Aa': 1, 'AA_aa': 1,
    'Aa_Aa': 0.75, 'Aa_aa': 0.5, 'aa_aa': 0
}

# Declarar a variável do número esperado da prole
prole = 0

# Iterar sobre o dicionário "dic_genomas"
for chave, valor in dic_genoma.items():
    # Descentendes: o número de descendentes informados acima
    # Valor: população do determinado genótipo
    # Probabilidades: dicionário de onde estão armazenadas as probabilidades
    # Chave: chave do dicionário "dic_genomas" que será usada para obter o valor da probabilidade
    # com a mesma chave do dicionário "probabilidades"
    prole += descendentes * (valor * probabilidades[chave])

# Mostrar a resposta
print(prole)
