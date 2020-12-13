## [re-pat]: Aplicar expressões regulares para encontrar padrões de texto simples em um documento

Q1) O script em [arquivos/re-pat-q1.py] gera um texto que contêm várias datas no formato americano MM/DD/AAAA. Use uma regra de substituição que converta todas estas datas para o formato brasileiro DD/MM/AAAA. Diga qual expressão regular e qual regra de substituição foi utilizada no seu editor de código.
'''

    dia = r"[\s|^][0-9]{2}"
    mes = r"\/[0-9]{2}\/"
    
    listaDia = re.findall(dia, frase)
    listaMes = re.findall(mes, frase)
            
    tempListaDia = []
    tempListaMes = []

    for i in listaDia:
        tempListaDia.append("/"+i[1:]+"/")
    for i in listaMes:
        tempListaMes.append(" "+i[1:-1])

    for i in range(0, len(listaDia)):
        frase = re.sub(listaDia[i], tempListaMes[i], frase)
        frase = re.sub(listaMes[i], tempListaDia[i], frase)
'''

Q2) O arquivo [arquivos/re-pat-q2.py] gera um html algumas tags <img> que fazem referências a arquivos ".gif" como em <img src="path-to-img.gif">. Crie uma expressão regular que encontre todas extensões .gif que aparecem dentro do atributo src das tags de img. Descreva como você poderia utilizar esta expressão em conjunto com alguma outra ferramenta para contar o número de ocorrências destas imagens no documento.
'''

    r"<img\ssrc=".*\.gif">"
'''
Um metodo que poderia ser utlizado para encontrar a quantidade de ocorrencias seria executar um findall no html gerado e contar a quantidade de elementos no vetor resultante.