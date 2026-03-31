def calcular_media(prod, qual, pont):
    return (prod + qual + pont)/3

def classificar(media):
    if media >= 8 :
        return 'Excelente'
    elif media >= 6:
        return 'Bom'
    else:
        return 'Critico'

def avaliar_funcionarios():
    total = 0
    exc = 0
    bom = 0
    crit = 0
    melhorNome = ''
    melhoMedia = -1
    while True:
        nome = input("Nome: ")
        if nome == 'fim':
            break
        prod = float(input('produtividade: '))
        qual = float(input('qualidade:' ))
        pont = float(input('pontualidade: '))
        
        media = calcular_media(prod,qual,prod)
        categoria = classificar(media)
        print(f'{nome}, media {media}, {categoria}')
        
        total += 1 
        if categoria == 'Excelente':
            exc += 1
        elif categoria == 'Bom':
            bom += 1
        else:
            crit += 1
            
        if media > melhoMedia:
            melhorMedia = media
            melhorNome = nome
        if total == 0:
            print('Nada para calcular')
            return
        print("-" * 50)
        print('Relatorio')
        print("-" * 50)
        print(f'total de func: {total}')
        print(f'Excelente: {exc}')
        print(f'Bom: {bom}')
        print(f'Critico: {crit}')
        print(f'melhor func:{melhorNome}')
        print(f'melhor func media:{melhorMedia}')
        
avaliar_funcionarios()        