#------1) Observe o trecho de código abaixo:

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K
print(SOMA)

#------2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Solicita um número ao usuário
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#------3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

import json

with open ("arquivo.json") as meu_json:
    arquivo = json.load(meu_json)

print(arquivo)

 #Função para calcular os valores requisitados
def calcular_faturamento(dicionario):
    faturamento = dicionario["faturamento_diario"]

#    # Ignorando dias sem faturamento (valores iguais a zero)
    faturamento_validos = [valor for valor in faturamento if valor > 0]

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    # Calcula a média mensal, ignorando dias com faturamento zero
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    # Conta quantos dias o faturamento foi superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

     #Retorna os resultados
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Calcula os valores
menor, maior, dias_acima_media = calcular_faturamento(arquivo)

# Exibe os resultados
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

#------4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# Calcular o valor total mensal da distribuidora
valor_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

# Calcular o percentual de representação de cada estado
percentual_sp = (faturamento_sp / valor_total) * 100
percentual_rj = (faturamento_rj / valor_total) * 100
percentual_mg = (faturamento_mg / valor_total) * 100
percentual_es = (faturamento_es / valor_total) * 100
percentual_outros = (faturamento_outros / valor_total) * 100

# Imprimir os resultados
print("Percentual de representação de cada estado:")
print(f"SP: {percentual_sp:.2f}%")
print(f"RJ: {percentual_rj:.2f}%")
print(f"MG: {percentual_mg:.2f}%")
print(f"ES: {percentual_es:.2f}%")
print(f"Outros: {percentual_outros:.2f}%")

#------5) Escreva um programa que inverta os caracteres de um string.

string = input("Insira a string: ")

# Inverter a string
inverted_string = ""

for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print("A string invertida é:", inverted_string)