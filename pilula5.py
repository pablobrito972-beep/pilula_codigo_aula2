def calcularNotas(valor):
    for nota in (100,50,20,10):
        qtd = valor // nota
        valor = valor % nota 
        if qtd > 0:
            print(f'{qtd} de notas  R$ {nota}')

valor = int(input('Digite o valor'))
calcularNotas(valor)
