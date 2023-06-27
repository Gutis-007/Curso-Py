numero = int(input("Digite um número inteiro: "))

soma_digitos = 0
temp_numero = numero

while temp_numero > 0:
    
    digito = temp_numero % 10
   
    soma_digitos += digito
    
    temp_numero //= 10

print(soma_digitos)
