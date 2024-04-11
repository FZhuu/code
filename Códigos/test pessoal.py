# idade = int(input("Digite sua idade: "))
# print(idade)

# valor_pi = float(input("Digite valor de PI: "))
# print(valor_pi)

# numero = int(input("Digite número: "))
# if numero % 2 == 0:
#     print("valor é par.")
# else:
#     print("número é ímpar. ")

# pi = 3.14159265359
# pi_limitado = round(pi, 4)
# print(pi_limitado)

# raio = float(input("Digite o valor do raio: "))
# pi = 3.14
# perimetro = 2 * pi * raio
# print(perimetro)

# etiqueta = "etiqueta1"
# multiplicação = (etiqueta + "" + "|" + "")*20
# print (multiplicação)

# valor_tomate = 0.5
# quantidade_comprada = int(input("DIgite a quantidade de tomates comprados: "))
# horario = int(input("Digite o horario atual: "))
# if horario < 11:
#     if quantidade_comprada <= 10:
#         valor_compra = valor_tomate * quantidade_comprada
#         print(valor_compra)
#     else:
#         valor_compra2 = valor_tomate * quantidade_comprada - quantidade_comprada * 0.1
#         print (valor_compra2)
# else:
#     if quantidade_comprada <= 10:
#         valor_compra3 = valor_tomate * quantidade_comprada * 0.7
#         print(valor_compra3)
#     else:
#         valor_compra4 = (valor_tomate * quantidade_comprada - quantidade_comprada * 0.1) * 0.7
#         print (valor_compra4)
# lista_pokemons = ["charmander", "squirtle", "bulbasaur"]
# pokemonsadquiridos = ""
# for _ in range(6):
#         nome = input("Digite o nome dos pokemons adquiridos: ").lower()
#         if nome == "none":
#                 break
#         elif nome not in lista_pokemons:
#                 print("\nEste pokemon não existe")
#         else:
#                 pokemonsadquiridos += nome + " "

# if pokemonsadquiridos != "":
#     print("\nSeus pokemons são:""\n",pokemonsadquiridos) 
# else:
#     print("Você não possui pokemons.")






# """sistema que possibilite o jogador a explorar matos altos e cavernas
#  para encontrar pokemons"""



# import random
# import time

# # Lista de Pokémon que podem aparecer
# pokemons = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Eevee']

# # Função para simular a exploração
# def explorar_ambiente(ambiente):
#     print(f"Explorando {ambiente}...")
#     if random.random() < 0.55:  # 55% de chance de encontrar um Pokémon
#         pokemon = random.choice(pokemons)
#         print(f"Um {pokemon} selvagem apareceu!")
#         capturar = input("Deseja tentar capturar o Pokémon? (sim/não): ")
#         if capturar.lower() == 'sim':
#             # Simula a captura do Pokémon
#             if random.random() < 0.7:  # 80% de chance de sucesso na captura
#                 print(f"Você capturou {pokemon}!")
#                 return pokemon
#             else:
#                 print("O Pokémon escapou!")
#         elif capturar.lower() == "nao":
#             print("Você decidiu não capturar o Pokémon.")
#         else: 
#             print("você digitou uma opção invalida e o pokemon fugiu.")
#             print("Mais sorte na proxima")
        
#     else:
#         print("Nenhum Pokémon apareceu desta vez.")
#     return None

# # Loop principal do jogo
# capturados = []
# menu = True
# while menu:
#     print("---- andar = 1 ----")
#     print("---- sair  = 2 ----")
#     acao = input("digite sua ação: ")
#     if acao == "1":
#         print("andando...")
#         ambiente = random.choice(['matos altos', 'caverna'])
#         pokemon_capturado = explorar_ambiente(ambiente)
#         if pokemon_capturado:
#             capturados.append(pokemon_capturado)    
#     else:
#         print("Comando inválido. Por favor, digite 'explorar' ou 'sair'.")


# # Exibe os Pokémon capturados ao final do jogo
# print("Pokémon capturados durante sua aventura:")
# for pokemon in capturados:
#   print(pokemon)

# import random

# # Lista de Pokémon que podem aparecer
# pokemons = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Eevee']

# # Função para simular a exploração
# def explorar_ambiente(ambiente):
#     print(f"Explorando {ambiente}...")
#     if random.random() < 0.55:  # 55% de chance de encontrar um Pokémon
#         pokemon = random.choice(pokemons)
#         print(f"Um {pokemon} selvagem apareceu!")
#         capturar = input("Deseja tentar capturar o Pokémon? (sim/não): ")
#         if capturar.lower() == 'sim':
#             # Simula a captura do Pokémon
#             if random.random() < 0.7:  # 80% de chance de sucesso na captura
#                 print(f"Você capturou {pokemon}!")
#                 return pokemon
#             else:
#                 print("O Pokémon escapou!")
#         elif capturar.lower() == "nao":
#             print("Você decidiu não capturar o Pokémon.")
#         else: 
#             print("você digitou uma opção invalida e o pokemon fugiu.")
#             print("Mais sorte na proxima")
        
#     else:
#         print("Nenhum Pokémon apareceu desta vez.")
#     return None

# # Loop principal do jogo
# capturados = []
# menu = True
# while menu:
#     print("---- andar = 1 ----")
#     print("---- sair  = 2 ----")
#     acao = input("digite sua ação: ")
#     if acao == "1":
#         print("andando...")
#         ambiente = random.choice(['matos altos', 'caverna'])
#         pokemon_capturado = explorar_ambiente(ambiente)
#         if pokemon_capturado:
#             capturados.append(pokemon_capturado)    
#     else:
#         print("Comando inválido. Por favor, digite 'explorar' ou 'sair'.")


# # Exibe os Pokémon capturados ao final do jogo
# print("Pokémon capturados durante sua aventura:")
# for pokemon in capturados:
#         print(pokemon)

# import random
# import time

# pokedex_safari = ["Magikarp","Psyduck", "Goldeen", "Dragonair", "Dratini","Seaking","Poliwag","Exeggcute","Rhyhorn","Nidoran F.","Nidoran M","Nidorino","Nidorina","Doduo","Chansey","Kangaskhan","Scyther","Pinsir","Tauros"]



# box_pokemon = []
# menu = True
# posicao_na_box = 0
# def aparecendo_pokemon():
#    pokemon = random.choice(pokedex_safari)
#    box_pokemon.append(pokemon)

# while menu:
#    print("---- andar = 1 ----")
#    print("---- sair  = 2 ----")
#    acao = input("digite sua ação: ")
#    if acao == "1":
#       aparecendo_pokemon()
#       print(box_pokemon)
#       time.sleep(1)
#    elif acao == "2":
#       break
#    else:
#       print("opção invalida por favor digite apenas as opções definidas")
#       print("tente novamente")
#       continue

# def new_user():
#    nome_usuario = input("Digite o nome de usuário: ")
#    senha_usuario = input("Digite a senha: ")
#    rep_senha_usu = input("Digite novamente a senha:")
#    if senha_usuario == rep_senha_usu:
#       usuario = {
#          'usuario' : nome_usuario,
#          'senha' : senha_usuario
#          }
#       return usuario
#    else:
#       print("\nSenhas inconpatíveis.")
#       print("Tente novamente")
#       new_user()
# print()

# def main():
#     usuarios = []
#     continuar2 = True
#     continuar = True
#     while continuar:
#         novo_usuario = new_user()
#         usuarios.append(novo_usuario)
#         print("\nUsuário cadastrado com sucesso!")
#         while continuar2:
#          print("\nDeseja cadastrar outro usuário?:")
#          opcao = input("1 = Sim | 2 = Não ")
#          if opcao == "2":
#             continuar = False
#          elif opcao == "1":
#             continuar = False
#             continuar2 = False
#          else:
#            print("Opção inválida.")
#            print("Tente novamente.")
#            continue

#     print("\nLista de usuários cadastrados:")
#     for usuario in usuarios:
#         print(usuario)

# main()
# if __name__ == "__main__":
#     main()

# class Usuario:
#     valor_passagem = 6 
#     def __init__(self, nome):
#         self.nome = nome
#         self.saldo_atual = 0

#     def add_saldo(self, valor):
#         self.saldo_atual += valor

#     def usar_cartao(self):
#         if self.saldo_atual >= Usuario.valor_passagem:
#             self.saldo_atual -= Usuario.valor_passagem
#             print(f"Passagem utilizada. Saldo atual: {self.saldo_atual}")
#         else:
#             print("Saldo insuficiente.")

# class Administrador:
#     usuarios_cadastrados = {}

#     @staticmethod
#     def modificar_valor_passagem(novo_valor):
#         Usuario.valor_passagem = novo_valor
#         print(f"Novo valor da passagem: {Usuario.valor_passagem}")

#     @classmethod
    # def ver_saldo_usuarios(adm):
    #     for nome, usuario in adm.usuarios_cadastrados.items():
    #         print(f"Usuário: {nome}, Saldo: {usuario.saldo_atual}")

    # @classmethod
    # def cadastrar_usuario(adm, usuario):
    #     adm.usuarios_cadastrados[usuario.nome] = usuario

    # def ver_usuarios_cadastrador(adm):
#         for nome in adm.usuarios_cadastrados:
#             print(nome)


# usuario1 = Usuario("Zhu")
# admin1 = Administrador()



# usuario1 = Usuario("joao")
# admin1 = Administrador()      
# usuario1 = Usuario("Jv")
# usuario2 = Usuario("Zhu")
# usuario3 = Usuario("Zhou")
# usuario4 = Usuario("fabri")
# usuario5 = Usuario("João")

# admin1.cadastrar_usuario(usuario1)
# admin1.cadastrar_usuario(usuario2)
# admin1.cadastrar_usuario(usuario3)
# admin1.cadastrar_usuario(usuario4)
# admin1.cadastrar_usuario(usuario5)
#usuario1.add_saldo(50)

#usuario1.usar_cartao()


#admin1.ver_saldo_usuarios()


#admin1.modificar_valor_passagem(12)

# admin1.modificar_valor_passagem(6)
# print(Usuario.valor_passagem)
#print(admin1.usuarios_cadastrados)

# contador = 1
# soma = 0
# while contador < 11:
#     soma += contador
#     print("somatório = ", soma)
#     contador += 1
    
# etiqueta = "Eu amo Raciocínio Algorítimico"
# multiplicação = ( etiqueta + "\n" ) * 10
# print (multiplicação)
import random
num_b = int(random.randint(1, 10))
print(num_b)
sim = 1
while sim < 4:
    num_a = int(input("Digite o número: "))
    if num_a > num_b:
        print("o número de b é menor")
        sim += 1
    elif num_a < num_b:
        print("o número de b é maior")
        sim += 1
    else:
        print("acertou")
        break
if sim == 4:
    print("Tentativas encerrados.")
else:
    print("Parabéns você me derrotou.")