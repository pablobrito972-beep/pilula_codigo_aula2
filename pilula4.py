import statistics
lote1 = float(input('produção lote 1:'))
lote2 = float(input('produção lote 2:'))
lote3 = float(input('produção lote3:'))
media = statistics.mean((lote1, lote2, lote3))
desvio = statistics.stdev((lote1, lote2, lote3))
print(f'Média{media:.2f}')
print(f'desvio padrão{desvio:.2f}')