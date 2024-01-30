from time import sleep
from Forca import palavras_aleatorias
from random import randint
while True:
    word = palavras_aleatorias[randint(0,39)].upper()
    show = list()
    trys = list()
    vidas=5
    for c in range(0,len(word)):
        show.append('_')
    while True:
        part=0
        while True:
            print(f'Você ainda tem {vidas} vidas')
            sleep(0.3)
            if vidas!=5:
                print(f'Tentativas: {trys}')    
                sleep(0.3)
            print(f'Sua palavra: {show}')
            sleep(0.3)
            letra = str(input('Qual será seu chute? ')).upper()
            sleep(0.5)
            if len(letra)>1:
                print('\033[31mDigite apenas uma letra!\033[m')
            elif letra in trys:
                print('Você já tentou esta letra! Tente outra')
            elif letra not in trys:
                break
        if letra in word:
            times=word.count(letra)
            for c in range(0,times):
                if c==0:
                    indice=word.index(letra,part)
                else:
                    indice=word.index(letra,part+1)
                show[indice]=word[indice]
                part=indice
        else:
            vidas-=1
            trys.append(letra)
        if vidas==0:
            game=False
            break
        if show==list(word):
            game=True
            break
    if game==False:
        print(show)
        print('Você perdeu! ')
        print(f'A palavra era {word}')
    elif game==True:
        print(show)
        print('Você \033[32mvenceu\033[m!')
        print(f'Sobraram {vidas} vidas')
    while True:
        res = input('Quer jogar novamente? [S/N] ').upper()
        if res == 'S' or res=='N':
            break
        else: 
            print('Digite uma resposta válida!')
    if res == 'N':
        break
print('Obrigado por jogar!!')
         

