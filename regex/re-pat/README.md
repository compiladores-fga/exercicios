# Q1

para gerar o arquivo necessário digite:
	
	python3 ../../arquivos/re-pat-q1.py > fake_text.txt

depois execute o programa [resposta1.py](resposta1.py) para mudar as datas do arquivo.

	python3 resposta1.py

a regex usada para capturar as datas foi:

	(?P<month>\d{2})(?P<bar1>/)(?P<day>\d{2})(?P<bar2>/)(?P<year>\d{4})

foi usado grupos nomeados pois desta maneira é possivel utilizalos na função que faz a transformação do texto usando a função sub do modulo re.

# Q2

para gerar o arquivo necessário digite:

	python3 ../../arquivos/re-pat-q2.py > fake.html

depois execute o programa [resposta2.py](resposta2.py) para mudar as datas do arquivo.

	python3 resposta2.py

a regex usada para capturar as datas foi:

	<\s*img .*src=\".+\.gif\"

usando esta regex junto com a função findall do módulo re, se consegue uma lista de todas as ocorrencias de gifs em uma pagina html válida, para conseguir a quantidade de gifs é só pegar o tamanho da lista com a função len.