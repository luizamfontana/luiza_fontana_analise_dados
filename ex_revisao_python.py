"""
Lista de exercícios de revisão de Python
Disciplina: Programação para Análise de Dados
Nome do aluno: Luiza Mulinari Fontana
Matrícula: 202501379559
Email: luizamulinarifontana@gmail.com 
        ou 202501379559@alunos.ibmec.edu.br

Orientações:
- Resolva cada exercício separadamente.
- Execute o arquivo após cada solução para conferir o resultado.
- Use apenas os comandos básicos estudados em aula.
- Não use IA para resolver os exercícios, pois o objetivo é relembrar e praticar os conceitos aprendidos.
- Duvidas, mande um e-mail para o professor: laerte.takeuti@professores.ibmec.edu.br
- Se quiser mais exercícios, consulte o site: https://www.w3schools.com/python/default.asp
- Se quiser aulas em vídeo, consulte o canal: https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
"""
# ============================================================================
# 1. VARIÁVEIS — EXERCÍCIOS 1 A 10
# ============================================================================

# Exercício 1 — Dados pessoais
# Crie quatro variáveis para armazenar seu nome, sua idade, sua altura e se você
# é estudante. Mostre o valor e o tipo de cada variável usando print() e type().

nome = "Luiza"
print(nome)
type (nome)

idade = 18
print(idade)
type (idade)

altura = 1.70
print(altura)
type (altura)

é_estudante = True
print(é_estudante)
type (é_estudante)

# _________________________________________________________

# Exercício 2 — Saudação
# Peça ao usuário seu nome e sua cidade. Depois, mostre a mensagem:
# "Olá, <nome>! Você mora em <cidade>."

nome_usuario = str(input("Digite seu nome:"))
cidade_usuario = str(input("Digite sua cidade:"))

print(f"Olá, {nome_usuario}! Você mora em {cidade_usuario}.")

# _________________________________________________________

# Exercício 3 — Soma de dois números
# Leia dois números inteiros usando input(), converta-os com int() e mostre
# a soma dos valores.

num_int1 = int(input("Digite um número inteiro:"))
num_int2 = int(input("Digite outro número inteiro:"))
soma_num_int = num_int1 + num_int2

print(f"A soma dos 2 números inteiros é: {soma_num_int}")

# _________________________________________________________

# Exercício 4 — Operações básicas
# Leia dois números e mostre o resultado da soma, subtração, multiplicação
# e divisão entre eles.

num1 = float(input("Digite um número:"))
num2 = float(input("Digite outro número:"))

soma_num = num1 + num2
sub_num = num1 - num2
mult_num = (num1 * num2)
div_num = num1 / num2

print(f"A soma dos 2 números é: {soma_num:.2f}")
print(f"A subtração dos 1° número pelo 2° é: {sub_num:2f}")
print(f"A multiplicação dos 2 números é: {mult_num:.2f}")
print(f"A divisão dos 2 números é: {div_num:.2f}")


# _________________________________________________________

# Exercício 5 — Média de três notas
# Leia três notas do tipo float, calcule a média aritmética e mostre o resultado
# com duas casas decimais.

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = ((nota1 + nota2 + nota3)/3)

print (f"A média das 3 notas é: {media:.2f}")

# _________________________________________________________

# Exercício 6 — Idade no futuro
# Peça a idade atual do usuário e informe quantos anos ele terá daqui a 10 anos.

idade = int(input("Digite sua idade atual:"))

print (f"Sua idade daqui 10 anos será {idade + 10} anos")

# _________________________________________________________

# Exercício 7 — Conversão de temperatura
# Leia uma temperatura em graus Celsius e converta para Fahrenheit.
# Fórmula: fahrenheit = (celsius * 9 / 5) + 32

temp_c = float(input("Digite uma temperatura, em °C:"))
temp_f = ((temp_c * 9/5) + 32)


print (f"Em Fahrenheit, {temp_c}°C será {temp_f}°F")

# _________________________________________________________

# Exercício 8 — Área de um retângulo
# Leia a largura e a altura de um retângulo. Calcule e mostre sua área.
# Fórmula: area = largura * altura

larg = float(input("Digite a largura do retângulo:"))
alt = float(input("Digite a altura do retângulo:"))
unidade = str(input("Qual a unidade de medida da largura e da altura?"))
area = larg * alt

print (f"A área desse retângulo é de: {area} {unidade}²")

# _________________________________________________________

# Exercício 9 — Manipulação de texto
# Peça uma frase ao usuário e mostre:
# a) a frase em letras maiúsculas;
# b) a frase em letras minúsculas;
# c) a quantidade de caracteres da frase.

frase = str(input("Digite uma frase:"))

!!!

# _________________________________________________________

# Exercício 10 — Preço com desconto
# Leia o nome de um produto, seu preço e um percentual de desconto.
# Calcule e mostre o nome do produto, o valor do desconto e o preço final.

produto = str(input("Digite o nome de um produto:"))
preco = int(input("Digite o preço desse produto:"))
desc = int(input("Digite o percentual de desconto para esse produto:"))
valor = (((100-desc)/100)*preco)

print (f"O produto {produto}, com desconto de {desc}%, terá valor final de R${valor:.2f}")


# ============================================================================
# 2. ESTRUTURA CONDICIONAL — EXERCÍCIOS 11 A 20
# ============================================================================

# Exercício 11 — Positivo, negativo ou zero
# Leia um número e informe se ele é positivo, negativo ou igual a zero.

numero = float(input("Digite um número:"))
if numero > 0: 
    print(f"O número é positivo.")
elif numero < 0:
    print(f"O número é negativo.")
else:
    print (f"O número é igual a zero.") 

# _________________________________________________________

# Exercício 12 — Par ou ímpar
# Leia um número inteiro e informe se ele é par ou ímpar.
# Dica: use o operador de resto da divisão (%).

numero_inteiro = float(input("Digite um número inteiro:"))

if numero_inteiro % 2 == 0:
    print(f"O número é par.")
else:
    print (f"O número é ímpar.")


# _________________________________________________________

# Exercício 13 — Aprovação
# Leia a média de um aluno. Mostre "Aprovado" se a média for maior ou igual
# a 7 e "Reprovado" caso contrário.

media_aluno = float(input("Digite sua média:"))
if media_aluno >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# _________________________________________________________

# Exercício 14 — Aprovação com recuperação
# Leia a média de um aluno e mostre:
# - "Aprovado", se a média for maior ou igual a 7;
# - "Recuperação", se a média estiver entre 5 e 6.9;
# - "Reprovado", se a média for menor que 5.

media_2 = float(input("Digite sua média:"))

if media_2 >= 7:
    print("Aprovado")
elif 5 < media_2 < 7 :
    print("Recuperação")
else: 
    print("Reprovado")


# _________________________________________________________

# Exercício 15 — Maior entre dois números
# Leia dois números e mostre qual é o maior. Se forem iguais, informe isso.

numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))

maior = max (numero1, numero2)

if numero1 != numero2: 
    print(f"O maior número é: {maior}.")
else:
    print(f"Os números são iguais.")


# _________________________________________________________

# Exercício 16 — Faixa etária
# Leia a idade de uma pessoa e classifique-a como:
# - "Criança": até 11 anos;
# - "Adolescente": de 12 a 17 anos;
# - "Adulto": de 18 a 59 anos;
# - "Idoso": 60 anos ou mais.

idade1 = int(input("Digite sua idade:"))

if idade1 <= 11:
    print("Criança")
elif 12 <= idade1 <= 17:
    print("Adolescente")
elif 18 <= idade1 <= 59:
    print("Adulto")
else: 
    print("Idoso")


# _________________________________________________________

# Exercício 17 — Desconto na compra
# Leia o valor de uma compra. Se o valor for maior que R$ 100,00, aplique
# desconto de 10%. Caso contrário, mantenha o valor original. Mostre o total.

compra = int(input("Digite o valor da compra."))
compra_desc = 0.9*compra

if compra > 100:
    print(f"O valor total é R${compra_desc:.2f}")
elif compra <= 100:
    print(f"O valor total é R${compra:.2f}")


# _________________________________________________________

# Exercício 18 — Acesso ao sistema
# Leia o nome de usuário e a senha. Mostre "Acesso permitido" somente quando
# o usuário for "admin" e a senha for "1234". Caso contrário, mostre
# "Acesso negado".

usuario = str(input("Digite o nome de usuário:"))
senha = str(input("Digite a senha:"))

if usuario == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")


# _________________________________________________________

# Exercício 19 — Número dentro do intervalo
# Leia um número e informe se ele está entre 10 e 50, incluindo os limites.
# Use os operadores and, >= e <=.

num_inp = float(input("Digite um número:"))

if 10 <= num_inp <= 50:
    print(f"O número está no intervalo.")
else:
    print(f"O número está fora do intervalo.")

# _________________________________________________________

# Exercício 20 — Calculadora simples
# Leia dois números e uma operação (+, -, * ou /). Use if/elif/else para
# realizar a operação escolhida e mostrar o resultado. Não permita divisão
# por zero.

n1 = float(input("Digite o 1° número:"))
n2 = float (input("Digite o 2° número:"))
operacao = str(input("Digite a operação (+, -, * ou /):"))

if operacao == "+":
    print(f"O resultado da soma é: {(n1+n2):.2f}")
elif operacao == "-":
    print(f"O resultado da subtração é: {(n1-n2):.2f}")
elif operacao == "*":
    print(f"O resultado da multiplicação é: {(n1*n2):.2f}")
elif operacao == "/":
    print(f"O resultado da divisão é: {(n1/n2)}")


# ============================================================================
# 3. LISTAS — EXERCÍCIOS 21 A 30
# ============================================================================

# Exercício 21 — Criando uma lista
# Crie uma lista com as frutas "maçã", "banana", "laranja" e "uva".
# Mostre a lista completa.

frutas = ["maçã", "banana", "laranja", "uva"]
print (frutas)

# _________________________________________________________

# Exercício 22 — Acessando elementos
# Usando a lista abaixo, mostre o primeiro e o último elemento.
# cores = ["azul", "verde", "amarelo", "vermelho"]

cores = ["azul", "verde", "amarelo", "vermelho"]
cores[0]
cores[-1]

# _________________________________________________________

# Exercício 23 — Adicionando elementos
# Crie uma lista com três nomes. Peça outro nome ao usuário, adicione-o ao
# final da lista com append() e mostre a lista atualizada.

nomes = ["Luiza", "Pedro", "Mateus"]
nome4 = str(input("Digite um nome:"))

nomes.append(nome4)

print(nomes)

# _________________________________________________________

# Exercício 24 — Removendo elementos
# Dada a lista abaixo, remova "banana" com remove() e mostre o resultado.
# frutas = ["maçã", "banana", "laranja", "uva"]

frutas = ["maçã", "banana", "laranja", "uva"]

frutas.remove("banana")

print(frutas)

# _________________________________________________________

# Exercício 25 — Alterando um elemento
# Dada a lista abaixo, substitua "laranja" por "abacaxi" usando seu índice.
# frutas = ["maçã", "banana", "laranja", "uva"]

frutas = ["maçã", "banana", "laranja", "uva"]

frutas[2] = "abacaxi"

print(frutas)

# _________________________________________________________

# Exercício 26 — Tamanho e presença
# Dada a lista abaixo, mostre a quantidade de elementos e verifique se
# o número 30 pertence à lista.
# numeros = [10, 20, 30, 40, 50]

numeros = [10, 20, 30, 40, 50]

len(numeros)

if 30 in numeros:
    print("O número 30 pertence à lista.")
else:
    print("O número 30 não pertence à lista")

# _________________________________________________________

# Exercício 27 — Soma, maior e menor
# Dada a lista abaixo, mostre a soma, o maior valor e o menor valor usando
# sum(), max() e min().
# valores = [12, 5, 28, 9, 17]

valores = [12, 5, 28, 9, 17]

print(f"A soma dos números da lista é: {sum(valores)}.")
print(f"O maior valor da lista é: {max(valores)}.")
print(f"O menor valor da lista é: {min(valores)}.")

# _________________________________________________________

# Exercício 28 — Ordenação
# Coloque a lista abaixo em ordem alfabética usando sort() e mostre o resultado.
# cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]

cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]

cidades.sort()

print(cidades)

# _________________________________________________________

# Exercício 29 — Concatenação
# Una as duas listas abaixo em uma terceira lista e mostre o resultado.
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b

print(lista_c)

# _________________________________________________________

# Exercício 30 — Fatiamento
# Dada a lista abaixo, use fatiamento para mostrar:
# a) os três primeiros números;
# b) os três últimos números;
# c) os números do índice 2 ao índice 5.
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Os 3 primeiros números são: {(numeros[0], numeros[1], numeros[2])}.")

print(f"Os 3 últimos números são: {(numeros[-3], numeros[-2], numeros[-1])}.")

print(f"Os números do índice 2 ao 5 são: {(numeros[1], numeros[2], numeros[3], numeros[4])}.")

# ============================================================================
# 4. ESTRUTURAS DE REPETIÇÃO — EXERCÍCIOS 31 A 40
# ============================================================================

# Exercício 31 — Números de 1 a 10
# Use um laço for e range() para mostrar os números de 1 a 10.

for n in range(1, 11):
    print(n)

# _________________________________________________________

# Exercício 32 — Números pares
# Use um laço for para mostrar apenas os números pares de 2 a 20.

for n in range(2,21):
    if n % 2 == 0:
        print(n)

# _________________________________________________________

# Exercício 33 — Percorrendo nomes
# Use um laço for para mostrar cada nome da lista abaixo em uma linha.
# nomes = ["Ana", "Bruno", "Carla", "Diego"]

nomes = ["Ana", "Bruno", "Carla", "Diego"]

for nome in nomes:
    print(nome)

# _________________________________________________________

# Exercício 34 — Quadrados
# Use um laço for para criar uma nova lista contendo o quadrado de cada número.
# numeros = [1, 2, 3, 4, 5]

numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrados.append(numero*numero)

print(quadrados)

# _________________________________________________________

# Exercício 35 — Soma com for
# Use um laço for e uma variável acumuladora para somar os valores abaixo.
# Não use a função sum().
# valores = [10, 20, 30, 40, 50]

valores = [10, 20, 30, 40, 50]
soma = 0

for valor in valores:
    soma =  soma + valor

print(soma)

# _________________________________________________________

# Exercício 36 — Contando aprovados
# Percorra a lista e conte quantas notas são maiores ou iguais a 7.
# notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]

notas = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]
notas1 = []

for nota in notas:
    if nota >= 7:
        notas1.append(nota)

print(f"O número de notas maiores ou iguais a 7 é: {len(notas1)}.")

# _________________________________________________________

# Exercício 37 — Contagem com while
# Use um laço while para mostrar os números de 1 a 10.

numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1

# _________________________________________________________

# Exercício 38 — Contagem regressiva
# Use um laço while para fazer uma contagem regressiva de 10 até 1.
# Ao terminar, mostre a mensagem "Fim!".

numero = 10

while numero >= 1:
    print(numero)
    numero = numero - 1

print("Fim!")

# _________________________________________________________

# Exercício 39 — Senha correta
# Peça uma senha ao usuário repetidamente usando while. O programa deve parar
# somente quando a senha digitada for "python123".

senha = str(input("Digite a senha:"))

while senha != "python123":
    print("Senha incorreta.")
    senha = str(input("Tente novamente:")) 

print("Senha correta!")

# _________________________________________________________

# Exercício 40 — Somando até zero
# Peça números inteiros ao usuário e some os valores digitados. Use while para
# continuar a leitura até que o usuário digite 0. Ao final, mostre a soma.

soma = 0
numero = int(input("Digite um número inteiro: "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número inteiro: "))

print(f"A soma dos números digitados é: {soma}")


# ============================================================================
# 5. DICIONÁRIOS — EXERCÍCIOS 41 A 50
# ============================================================================

# Exercício 41 — Criando um dicionário
# Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Preencha com valores fictícios e mostre o dicionário completo.

aluno = {
    "nome" : "Luiza",
    "idade" : 18,
    "curso" : "economia"
}

print(aluno)

# _________________________________________________________

# Exercício 42 — Acessando valores
# Dado o dicionário abaixo, mostre separadamente o nome e o preço do produto.
# produto = {"nome": "Teclado", "preco": 150.0, "estoque": 8}

produto = {"nome":"Teclado", "preco": 150.0, "estoque": 8}

print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto ['preco']}")

# _________________________________________________________

# Exercício 43 — Adicionando uma chave
# Adicione a chave "marca" ao dicionário abaixo e mostre o resultado.
# produto = {"nome": "Mouse", "preco": 80.0}

produto = {"nome": "Mouse", "preco": 80.0}

produto["marca"] = "Dell"

print(produto)

# _________________________________________________________

# Exercício 44 — Atualizando um valor
# Altere o estoque do produto abaixo para 15 unidades e mostre o dicionário.
# produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}

produto = {"nome": "Monitor", "preco": 900.0, "estoque": 5}

produto["estoque"] = 15

print(produto)

# _________________________________________________________

# Exercício 45 — Removendo uma chave
# Remova a chave "cor" do dicionário abaixo usando pop() e mostre o resultado.
# carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}

carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}

carro.pop("cor")

print(carro)

# _________________________________________________________

# Exercício 46 — Verificando uma chave
# Verifique se a chave "telefone" existe no dicionário abaixo. Mostre uma
# mensagem informando o resultado.
# contato = {"nome": "Marina", "email": "marina@email.com"}

contato = {"nome": "Marina", "email": "marina@email.com"}

if "telefone" in contato:
    print("A chave 'telefone' existe no dicionário.")
else:
    print("A chave 'telefone' não existe no dicionário.")

# _________________________________________________________

# Exercício 47 — Chaves e valores
# Use keys() para mostrar todas as chaves e values() para mostrar todos os
# valores do dicionário abaixo.
# capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}

capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}

capitais.keys()
capitais.values()

# _________________________________________________________

# Exercício 48 — Percorrendo um dicionário
# Use um laço for e items() para mostrar o nome de cada produto e seu preço.
# produtos = {"caderno": 25.0, "caneta": 4.5, "mochila": 120.0}

produtos = {"caderno": 25.0, "caneta": 4.5, "mochila": 120.0}

for nome, preco in produtos.items():    # items: keys e values juntos
    print(f"{nome}: R${preco}")

# _________________________________________________________

# Exercício 49 — Soma dos valores
# Calcule a soma de todas as quantidades do dicionário abaixo e mostre o total.
# estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}

estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}

print(sum(estoque.values()))

# _________________________________________________________

# Exercício 50 — Frequência de palavras
# Percorra a lista abaixo e crie um dicionário que conte quantas vezes cada
# palavra aparece. Ao final, mostre o dicionário de frequências.
# palavras = ["python", "dados", "python", "lista", "dados", "python"]

palavras = ["python", "dados", "python", "lista", "dados", "python"]

frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] = frequencia[palavra] + 1
    else:
        frequencia[palavra] = 1

print(frequencia)
#a 