media_p=[0, 0, 0, 0, 0]
categorias=[0, 0, 0, 0, 0]
resp1 = int(0)
resp2 = int(0) 
ADD=1
media=0
while resp1 != 4:

    print('========================================================')
    print('                        BEM-VINDO                       ')
    print('________________________________________________________')
    print('O QUE DESEJA')
    print('1 - TABULAÇÃO')
    print('2 - MEDIA DE LIGAÇÕES PRODUTIVAS')
    print('3 - ENCERRAR')
    print('________________________________________________________')
    resp1=int(input())
    print('________________________________________________________')
    while resp2 != 6:
        if resp1 == 1:
                for X in range(1):
                    print('========================================================')
                    print('        QUE TIPO DE LIGAÇÃO É ESSA QUE VOCÊ TEVE        ')
                    print('________________________________________________________')
                    print('QUE TIPO DE LIGAÇÃO É ESSA QUE VOCÊ TEVE')
                    print('1 - LINHA MUDA')
                    print('2 - RECUSA(CLIENTES QUE MESMO SE TIVEREM INTERESSE, NÃO PODEM A INTERNET)')
                    print('3 - NÃO TEVE NEM CONVERÇA')
                    print('4 - NÃO É A PESSOA QUE ATENDEU QUE CUIDA, POREM SABE SOBRE O PLANO RESIDENCIAL')
                    print('5 - LIGAÇÃO QUE TINHA POTENCIAL DE VENDA')
                    print('6 - VOUTAR')
                    print('========================================================')
                    resp2 = int(input())
                    print('________________________________________________________')
                if resp2 == 1:
                    categorias[0]+=ADD
                    media+=ADD                   
                elif resp2 == 2:
                    categorias[1]+=ADD
                    media+=ADD
                elif resp2 == 3:
                    categorias[2]+=ADD
                    media+=ADD
                elif resp2 == 4:
                    categorias[3]+=ADD
                    media+=ADD
                elif resp2 == 5:
                    categorias[4]+=ADD
                    media+=ADD
                else:
                    print('FECHANDO')
                   

    if resp1 == 2:
        for x in range(len(categorias)):
            media_p[x]= (categorias[x] / media)*100

    print('========================================================')
    print('                    HISTORICO DE CHAMADAS               ')
    print('________________________________________________________')
    print('1 - LINHA MUDA:', categorias[0])
    print ('POCENTAGEM DE CHAMADAS:', f"{media_p[0]:.2f}")
    print('________________________________________________________')
    print('2 - RECUSA:', categorias[1])
    print('POCENTAGEM DE CHAMADAS: %', f"{media_p[1]:.2f}")
    print('________________________________________________________')
    print('3 - NÃO TEVE NEM CONVERÇA:', categorias[2])
    print('POCENTAGEM DE CHAMADAS: %', f"{media_p[2]:.2f}")
    print('________________________________________________________')
    print('4 - NÃO É A PESSOA QUE ATENDEU QUE CUIDA, POREM SABE SOBRE O PLANO RESIDENCIAL:', categorias[3])
    print('POCENTAGEM DE CHAMADAS: %', f"{media_p[3]:.2f}")
    print('________________________________________________________')
    print('5 - LIGAÇÃO QUE TINHA POTENCIAL DE VENDA:', categorias[4])
    print('POCENTAGEM DE CHAMADAS: %', f"{media_p[4]:.2f}")
    print('________________________________________________________')
    print('TOTAL DE LIGAÇÕES:', media)


