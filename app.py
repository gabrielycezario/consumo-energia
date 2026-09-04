#cálculadora de consumo de energia 
#autor: Gabriely Cezario

#entrada:
nome_aparelho = input ("Digite o nome do aparelho: ")
potencia_aparelho = float (input ("Digite a potência do aparelho em watts (W): "))
tempo_medio_diario = float (input ("Digite o tempo médio de uso diário do aparelho: "))

#processamento 
consumo_mensal = (potencia_aparelho * tempo_medio_diario * 30) / 1000
valor_mensal = 0.75 * consumo_mensal

#saída
print (f"Aparelho: {nome_aparelho}\nConsumo estimado: {consumo_mensal}\nCusto estimado: R${valor_mensal}")