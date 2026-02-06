import math
#perguntas
notas_mensal=0
while notas_mensal <= 0:
    try:
        notas_mensal = int(input("quantas notas entraram esse mês?"))
        if notas_mensal <= 0:
            print("tente um valor valido por gentileza")
    except ValueError:
        print("Entrada invalida! Por favor, utilize apenas NÚMEROS")
        notas_mensal = 0
quantidade_pessoas = 0
while quantidade_pessoas <= 0:
    try:
        quantidade_pessoas = int(input("quantas pessoas estão validando?"))
        if quantidade_pessoas <= 0:
            print("valor invalido")
    except ValueError:
        print("Entrada invalida! Por favor, utilize apenas NÚMEROS")
        quantidade_pessoas = 0
dias_uteis = 0
while dias_uteis <= 0:
    try:
        dias_uteis = int(input("quantos dias foram trabalhados no mês?"))
        if dias_uteis <= 0:
            print ("É necessario informar os dias que foram trabalhados")
    except ValueError:
        print("Entrada invalida! Por favor, utilize apenas NÚMEROS")
        dias_uteis = 0
#calculos
divisao_total = notas_mensal/quantidade_pessoas
divisao_dia = divisao_total/dias_uteis
meta_pessoa = math.ceil(divisao_dia)
#slots
total_slot = quantidade_pessoas*dias_uteis
base_slot = notas_mensal // total_slot
resto = notas_mensal % total_slot

#resposta

print("\n" * 2)
print("======================================================")
print("PLANO DE LANÇAMENTOS")
print("======================================================")

print("\n" * 2)
print("PLANO DE LANÇAMENTOS")
print("====================")
print("Notas no mês:", notas_mensal)
print("Pessoas:", quantidade_pessoas)
print("Dias considerados:", dias_uteis)
print("-")
print("Média por pessoa no mês:", round(divisao_total, 2))
print("Média por pessoa por dia:", round(divisao_dia, 2))
print("Meta por pessoa por dia:", meta_pessoa, "(arredondada para cima)")
print("-")
print("Distribuição exata por pessoa-dia (slots):")
print("  Base por slot:", base_slot)
print("  Slots com +1:", resto, f"(farão {base_slot + 1})")
print("  Slots na base:", total_slot - resto, f"(farão {base_slot})")
print("====================")
    
    
    
    
    
    
    
    
    
    
    
    