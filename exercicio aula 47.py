"""
Faça um jogo para o usuario descobrir a palavra secreta
-Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuario digitar apenas uma letra.
-Quando o usuario digitar a letra, vcê 
vai conferir se a letra esta na palavra secreta.
-se a letra digitada estiver na palavra secreta;
exiba a letra.
- se a letra não estiver exiba *
Faça a contagem de tentativas do usuario
"""

import os #import para buscar o clear e limpar terminal
palavra_secreta = 'kalio' # fora do While pra não zerar quando reiniciar
letras_acertadas='' #para salvar as letras acertadas e não zerar ao reiniciar
tentativas = 0 #para iniciar a contagem de tenativas

while True:
    letra = input('digite uma letra: ')
    tentativas += 1

    if len(letra) > 1: #faz com que usuario digite apenas uma letra
        print('Digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra #salva as letras digitadas

    palavra_formada='' # para ordenar letras na horizontal
    for letra in palavra_secreta: # configurar apresentação das letra
        if letra in letras_acertadas: # se letra esta correta mostrar a letra
            palavra_formada += letra
        else: # se letra errada mostrar *
            palavra_formada += '*'
    
    print('palavra_formada:', palavra_formada) # mostra a palavra formada na horizontal
    if palavra_formada == palavra_secreta: #finaliza quando acerta a palavra
        os.system('cls') # para limpar o terminal antes de apresentar resultados\
        #clear ou cls dependendo do sistema operacional do pc
        print('VOCÊ GANHOU! PARABÉNS')
        print('A palavra era:',palavra_secreta)
        print('Tentaivas:', tentativas)

        letra ='' #para zerar o jogo apos vencer
        tentativas = 0 #para zerar o jogo apos vencer
        letras_acertadas = '' #para zerar o jogo apos vencer