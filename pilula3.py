import datetime
data_compra = input('data da compra (dd/mm/a')
meses = int(input('prazo da garantia:'))
data_inicial = datetime.datetime.strptime(data_compra,'%d/%m/%Y')
data_final = data_inicial + datetime.timedelta(days = meses * 30)
print(f'garantia valida até {data_final.strftime('%d/%m/%Y')}')
print(f'dia da semana{data_final.strftime('%a')}')