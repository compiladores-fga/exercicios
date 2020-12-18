"""
ALEM DA ILHA ELEMENTARY, considerou-se importante a construção desse problema.
COMPETENICIAS ESPECIFICAS: [py-hifn][py-pep8]

Problema 2:
Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade. 
Retorne uma lista com os registro ordenados por nome.
Exemplo de arquivo:
Id;nome;telefone;idade
1;João;43383832;28
2;Maria;43839322;32
.
.
.
N;Zzzz;99999999;12
"""

import csv

with open('src/dados.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file,delimiter=';',  fieldnames=["Id", "nome", "telefone", "idade"])
    csv_reader = list(csv_reader)

    # Verificação do CSV lido    
    print("-"*(30))
    print("CSV lido: \n\n", csv_reader)
    print("-"*(30))

    csv_reader.pop(0)

    listaOrdenadaId = sorted(csv_reader, key = lambda x: x['Id'])
    listaOrdenadaNome = sorted(csv_reader, key = lambda x: x['nome'])
    listaOrdenadaTelefone = sorted(csv_reader, key = lambda x: x['telefone'])
    listaOrdenadaIdade = sorted(csv_reader, key = lambda x: x['idade'])

    # Verificação das ordenações
    print("Lista ordenada pelo ID: \n\n", listaOrdenadaId)
    print("-"*(30))
    print("Lista ordenada pelo Nome: \n\n", listaOrdenadaNome)
    print("-"*(30))
    print("Lista ordenada pelo Telefone: \n\n", listaOrdenadaTelefone)
    print("-"*(30))
    print("Lista ordenada pelo Idade: \n\n", listaOrdenadaIdade)
    print("-"*(30))
