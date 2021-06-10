import re

fatos = {}
regras = {}

num_fatos, num_regras = [int(x) for x in input().rstrip().split(' ')]

for i in range(num_fatos):
    assinatura_fato, x, y = input().rstrip().split(' ')
    if assinatura_fato not in fatos:
        fatos[assinatura_fato] = []
    fatos[assinatura_fato].append([x, y])

for i in range(num_regras):
    assinatura_regra, condicao = input().rstrip().split(' -> ')
    print(assinatura_regra)
    print(condicao)

print(fatos)