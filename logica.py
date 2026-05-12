# Boas vindas
print("""
       -----------------------------------------------------------------------------
      | Seja bem Vindo! Siga as instruções para analisarmos os dados meteorológicos |
       -----------------------------------------------------------------------------
      """)

temperaturas_ano = []
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

# Coleta de dados
print("Informe corretamente as temperaturas máximas obtidas em cada mês...\n")
mes = 0
while mes < 12:
  temp = float(input(f"informe {meses[mes]}: "))
  
  if temp > 50 or temp < -60:
    print("⚠️  Atenção: Verifique se a temperatura informada e está correta e tente novamente")
    continue
    
  else:
    temperaturas_ano.append(temp)
    mes += 1

#Temperatura média máxima anual: soma das temperaturas divida pela quantidade de meses(12)
soma_temp = 0
count = 0
for count in range(0,12):
  soma_temp = float(temperaturas_ano[count] + soma_temp)
media_max = float(soma_temp / 12)


# Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
qnt_meses_escaldantes = 0
count = 0
meses_escaldantes = []
for count in range(0,12):
  if temperaturas_ano[count] > 33:
    qnt_meses_escaldantes += 1
    meses_escaldantes.append(meses[count])
    

# Mês mais escaldante do ano
mes_mais_escaldante = 0
max_temp = 0
for count in range(0,12):
  if temperaturas_ano[count] > max_temp: 
    max_temp = float(temperaturas_ano[count])
    mes_mais_escaldante = count

print(f"\ntemperatura máxima média: {media_max:.2f}°C")
print(f"Quantidade de meses escaldantes: {qnt_meses_escaldantes} ",", ".join(meses_escaldantes))
print(f"Mês mais escaldante: {meses[mes_mais_escaldante]}, {max_temp}°C")