def simularCrescimento(população, taxa, limite):
    anos = 0
    while população <= limite:
        população = população * (1+ taxa)
        anos += 1
        return anos

#main
p= float(input('população inicial: '))
t= float(input('Taxa (%):'))/100
l= float(input('Limite:'))

print(f'Anos={simularCrescimento(p,t,l)}')
