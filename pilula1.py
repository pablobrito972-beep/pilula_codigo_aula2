import math
#LEITURA
assinantes= int(input('digite a qtd de assinantes:'))
mensalidades= float(input('Digite o valor da mensalidades:'))
taxa=float(input('Digite a taxa de crescimento mensal%'))
meses= int(input('digite a qtd de meses da projeção:'))
#processamento
assinantes_finais = assinantes * math.pow((1+taxa),meses)
receita_final=assinantes_finais * mensalidades
print(f'assinantes estimados:.{assinantes_finais:.0f}')
receita_final= assinantes_finais * mensalidades
#saida
print(f'assinantes estimados{assinantes_finais:.0f}')
print(f'receita estimada:R${receita_final:.2f}')
