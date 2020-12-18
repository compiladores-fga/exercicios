def afd(delta, estado_inicial, estados_aceitacao, sequencia):
        
    estado_atual = estado_inicial    
    caminho_automato = []
    caminho_automato.append(estado_atual)
    # print('estado_atual:', estado_atual)

    for simbolo in sequencia:
        estado_atual = delta[(estado_atual, simbolo)]
        caminho_automato.append(estado_atual)

    # print('Caminho: ', caminho_automato)

    return estado_atual in estados_aceitacao
    
#---------------------------------
automato = {
        # A
        ('A','b'):'B',
        # B
        ('B','a'):'B',
        ('B','c'):'C',
        ('B','b'):'D',
        # C
        ('C','a'):'B',
        #D
        ('D','b'):'A'}
# ------------------------------

estado_inicial = 'A'
estado_final = ['D']
string_testa = input("Entre com a string: ")
resposta = afd(automato, estado_inicial, estado_final,str(string_testa))# -> True3

if resposta:
    print('Aceito')
else:
    print('Rejeitado')
