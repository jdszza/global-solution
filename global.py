#GRUPO: Gustavo Paraszczuk, Fernando Bertolucci e Jennifer de Souza

#Tarefas:
# Entrada de Dados: Solicite ao usuário para inserir o número de leituras e, em seguida, insira os dados (nível do mar, temperatura da água e a velocidade do vento) para cada leitura.
# Lógica de Verificação: Implemente a lógica para verificar as condições críticas, calcular as médias e desvios-padrão, e determinar máximos, mínimos e tendências.
# Saída de Dados: Imprima Alerta, média e desvio padrão, Estado Geral e análise histórica.

# nivel do mar - metros
# temperatura da agua - Celsius
# velocidade do vento - Km/h

# Condições Críticas:
# Nível do mar acima de 3 metros.
# Temperatura da água abaixo de 2°C ou acima de 30°C.
# Velocidade do vento acima de 70 km/h.
# Se qualquer uma das condições críticas for atendida em qualquer leitura, o algoritmo deve imprimir "Alerta: Condições críticas detectadas!".
# Se todas as leituras estiverem dentro dos limites seguros, o algoritmo deve imprimir "Tudo está normal."

#preciso que meu usuario me informe tres informacoes quantas vezes ele quiser

nivel_mar = []
temperatura_agua = []
velocidade_vento = []
critico = 0

num_leituras = int(input("Quantas leituras serão realizadas?"))
while num_leituras < 2:
    print()
    print("O número de leituras deve ser 2 ou mais. Por favor, insira novamente.")
    num_leituras = int(input("Quantas leituras serão realizadas?"))
print()

for cont in range(num_leituras):
    print(f"Insira os dados para a {cont+1}º leitura")
    print()
    nivel_mar.append(float(input("Informe o nível do mar em metros:")))
    temperatura_agua.append(float(input("Informe a temperatura da água em °C:")))
    velocidade_vento.append(float(input("Informe a velocidade do vento em Km/h:")))
    print()
    if nivel_mar[cont] > 3.0:
        print("Alerta: Condições críticas detectadas!")
        critico = critico + 1
        print()
    elif temperatura_agua[cont] < 2.0 or temperatura_agua[cont] > 30.0:
        print("Alerta: Condições críticas detectadas!")
        critico = critico + 1
        print()
    elif velocidade_vento[cont] > 70.0:
        print("Alerta: Condições críticas detectadas!")
        critico = critico + 1
        print()
    else:
        print("Tudo está normal.") 
        print()


# Calcule e exiba a média e o desvio padrão para os valores das leituras do nível do mar, temperatura da água e velocidade do vento.

# MÉDIAS ----------------------------------------------------------------

# Média do Nível do Mar
soma_mar = 0
for i in nivel_mar:
    soma_mar += i
    
media_mar = soma_mar/num_leituras
print(f"O nível médio do mar é de {media_mar:.2f} metros.")



# Média da Temperatura da Água
soma_agua = 0
for i in temperatura_agua:
    soma_agua += i
    
media_agua = soma_agua/num_leituras
print(f"A temperatura média da água é de {media_agua:.2f}°C")


# Média da Velocidade do Vento
soma_vento = 0
for i in velocidade_vento:
    soma_vento += i
    
media_vento = soma_vento/num_leituras
print(f"A velocidade média do vento é de {media_vento:.2f}Km/h")
print()




# DESVIO PADRÃO -------------------------------------------------------------------------------------------------

# Cálculo das diferenças e quadrados das diferenças
diferencas_mar = [(x - media_mar) ** 2 for x in nivel_mar]
diferencas_agua = [(x - media_agua) ** 2 for x in temperatura_agua]
diferencas_vento = [(x - media_vento) ** 2 for x in velocidade_vento]

# Cálculo da variação do nível da água

varia_mar = 0
for i in diferencas_mar:
    varia_mar += i

variacao_mar =  varia_mar/ num_leituras

# Cálculo da variação da temperatura da água

varia_agua = 0
for i in diferencas_agua:
    varia_agua += i

variacao_agua =  varia_agua/ num_leituras

# Cálculo da variação da velocidade do vento

varia_vento = 0
for i in diferencas_vento:
    varia_vento += i

variacao_vento =  varia_vento/ num_leituras

# Cálculo do desvio padrão (raiz quadrada da variância)
desvio_padrao_mar = variacao_mar ** 0.5
desvio_padrao_agua = variacao_agua ** 0.5
desvio_padrao_vento = variacao_vento ** 0.5

# Exibição dos resultados
print(f"Desvio padrão do nível do mar: {desvio_padrao_mar:.2f} metros")

print(f"Desvio padrão da temperatura da água: {desvio_padrao_agua:.2f}°C")

print(f"Desvio padrão da velocidade do vento: {desvio_padrao_vento:.2f} Km/h")

print()

# Se mais de 50% das leituras indicarem condições críticas, exiba "Estado Geral: Crítico".
# Caso contrário, exiba "Estado Geral: Estável".

porc_critico = critico/num_leituras

if porc_critico >= 0.5:
    print("Estado Geral: Crítico")
    print()
else:
    print("Estado Geral: Estável")
    print()
    

# Determine e exiba a leitura máxima e mínima para cada parâmetro (nível do mar, temperatura da água e velocidade do vento).

print()

maximo_mar = max(nivel_mar)
print(f"O nível do mar máximo inserido foi de: {maximo_mar}")

maximo_temperatura = max(temperatura_agua)
print(f"O grau de temperatura máximo inserido foi de: {maximo_temperatura}")

maximo_vento = max(velocidade_vento)
print(f"A velocidade do vento máxima inserida foi de: {maximo_vento}")
print()

minimo_mar = min(nivel_mar)
print(f"O nível do mar mínimo inserido foi de: {minimo_mar}")

minimo_temperatura = min(temperatura_agua)
print(f"O grau de temperatura mínimo inserido foi de: {minimo_temperatura}")

minimo_vento = min(velocidade_vento)
print(f"A velocidade do vento mínima inserida foi de: {minimo_vento}")
print()



# Determine a tendência dos dados (aumentando, diminuindo ou estável) para cada parâmetro

# Nível do Mar
aumento_mar = 0
diminuicao_mar = 0

for i in range(1, num_leituras):
    if nivel_mar[i] > nivel_mar[i - 1]:
        aumento_mar += 1
    elif nivel_mar[i] < nivel_mar[i - 1]:
        diminuicao_mar += 1

tendencia_mar = "Estável"
if aumento_mar > diminuicao_mar:
    tendencia_mar = "Aumentando"
elif diminuicao_mar > aumento_mar:
    tendencia_mar = "Diminuindo"

# Temperatura da Água
aumento_agua = 0
diminuicao_agua = 0

for i in range(1, num_leituras):
    if temperatura_agua[i] > temperatura_agua[i - 1]:
        aumento_agua += 1
    elif temperatura_agua[i] < temperatura_agua[i - 1]:
        diminuicao_agua += 1

tendencia_agua = "Estável"
if aumento_agua > diminuicao_agua:
    tendencia_agua = "Aumentando"
elif diminuicao_agua > aumento_agua:
    tendencia_agua = "Diminuindo"

# Velocidade do Vento
aumento_vento = 0
diminuicao_vento = 0
for i in range(1, num_leituras):
    if velocidade_vento[i] > velocidade_vento[i - 1]:
        aumento_vento += 1
    elif velocidade_vento[i] < velocidade_vento[i - 1]:
        diminuicao_vento += 1

tendencia_vento = "Estável"
if aumento_vento > diminuicao_vento:
    tendencia_vento = "Aumentando"
elif diminuicao_vento > aumento_vento:
    tendencia_vento = "Diminuindo"

# Exibir as tendências
print(f"Tendência do nível do mar: {tendencia_mar}")

print(f"Tendência da temperatura da água: {tendencia_agua}")

print(f"Tendência da velocidade do vento: {tendencia_vento}")
print()

