print("Hello there! Welcome to the world of Pokémon! My name is Oak! People call me the Pokémon Prof! This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. Myself… I study Pokémon as a profession.")

player_name = input("\nFirst, what is your name? ")

print("\nRight! So your name is ", player_name, "!")

print("\nThis is my grandson. He's been your rival since you were a baby.")

rival_name = input("\n...Erm, what is his name again? ")

print("\nThat's right! I remember now! His name is " + rival_name + "!" + player_name + 
      " Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let's go!")

print("\n",rival_name, "? Let me think… Oh, that's right. I told you to come! Just wait! Here, ",player_name,
       "! There are 3 Pokémon here! Haha! They are inside the Poké Balls. When I was young, I was a serious Pokémon trainer! In my old age, I have only 3 left, but you can have one! Choose!")

print("\nBe patient!",rival_name, ", you can have one too!")

print("\nNow,", player_name, ", which Pokémon do you want?")

print("\nSo! You want the fire/water/plant Pokémon, Charmander/Squirtle/Bulbasaur?")


pokemons = ["charmander", "bulbasaur", "squirtle"]

while True:
  first_poke = (input("\nchoose your pokémon:")).lower()

  if first_poke in pokemons:
    print("\nOH nice,this pokémon is really energetic! "+ first_poke + " is a good option for a starter pokémon! ")
    break
  else: 
    print("\nThis isn't a option, please, chose between charmander,bulbasaur or squirtle.")

lista_pokemons = ["bulbassauro", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard", "squirtle", "wartortle",
                   "blastoise", "caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto",
                     "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu", "sandshrew",
                       "sandslash", "nidoran", "nidorina", "nidoqueen", "nidorino", "nidoking", "clefairy", "clefable", "vulpix",
                         "ninetales", "jigglypuff", "wigglytuff", "zubat", "golbat", "oddish", "gloom", "vileplume", "paras",
                           "parasect", "venonat", "venomoth", "diglett", "dugtrio", "meowth", "persian", "psyduck", "golduck",
                             "mankey", "primeape", "growlithe", "arcanine", "poliwag", "poliwhirl", "poliwrath", "abra", "kadabra",
                               "alakazam", "machop", "machoke", "machamp", "bellsprout", "weepinbell", "victreebel", "tentacool",
                                 "tentacruel", "geodude", "graveler", "golem", "ponyta", "rapidash", "slowpoke", "slowbro",
                                   "magnemite", "magneton", "farfetchd", "doduo", "dodrio", "seel", "dewgong", "grimer", "muk",
                                     "shellder", "cloyster", "gastly", "haunter", "gengar", "onix", "drowzee", "hypno", "krabby",
                                       "kingler", "voltorb", "electrode", "exeggcute", "exeggutor", "cubone", "marowak", "hitmonlee",
                                         "hitmonchan", "lickitung", "koffing", "weezing", "rhyhorn", "rhydon", "chansey", "tangela",
                                           "kangaskhan", "horsea", "seadra", "goldeen", "seaking", "staryu", "starmie", "mr-mime",
                                             "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros", "magikarp", "gyarados",
                                               "lapras", "ditto", "eevee", "vaporeon", "jolteon", "flareon", "porygon", "omanyte",
                                                 "omastar", "kabuto", "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos",
                                                   "moltres", "dratini", "dragonair", "dragonite", "mewtwo", "mew", "none"]

# pokemonsadquiridos = []
# for _ in range(6):
#   nome = input("Digite o nome dos pokemons adquiridos: ").lower()
#   if nome == "none":
#     break
#   elif nome not in lista_pokemons:
#     print("\neste pokemon não existe")
#   else:
#     pokemonsadquiridos += nome + ", "

# if pokemonsadquiridos != "":
#   print("\nSeus pokemons são:""\n",pokemonsadquiridos[:-2]) 
# else:
#   print("Você não pussue pokemons.")

