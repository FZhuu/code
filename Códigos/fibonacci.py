# def fibonacci(n):
#     fib_sequence  =[0, 1]  # os dois primeiros termos da sequência Fibonacci

#     # Loop para calcular os próximos termos da sequência
#     for i in range(2, n):
#         next_term = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_term)

#     return fib_sequence

# # Quantidade de termos que você deseja calcular
# num_terms = int(input("Quantos termos de Fibonacci você deseja calcular? "))

# # Chama a função fibonacci e imprime a sequência
# fib_sequence = fibonacci(num_terms)
# print("Sequência de Fibonacci com", num_terms, "termos:", fib_sequence)


import matplotlib.pyplot as plt

def fibonacci(n):
    fib_sequence = [0, 1]  # os dois primeiros termos da sequência Fibonacci

    # Loop para calcular os próximos termos da sequência
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Quantidade de termos que você deseja calcular
num_terms = int(input("Quantos termos de Fibonacci você deseja calcular? "))

# Chama a função fibonacci para obter a sequência
fib_sequence = fibonacci(num_terms)

# Cria uma lista com os números dos termos
term_numbers = list(range(1, num_terms + 1))

# Plota o gráfico
plt.plot(term_numbers, fib_sequence, marker='o', linestyle='-')
plt.title('Sequência de Fibonacci')
plt.xlabel('Número do Termo')
plt.ylabel('Valor')
plt.grid(True)
plt.show()
