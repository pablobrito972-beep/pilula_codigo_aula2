import random
cotacao = float(input('cotação atual do dolar:'))
variação = random.uniform(-0.015, 0.015)
nova_cotação = cotacao * (1 + variação)
print(f'variação simulada:{variação:.3%}')
print(f'nova cotação:{nova_cotação:.2f}')