import matplotlib.pyplot as plt
from aux_functions import getAllPokemons, getPokemonByName, getLocationsByName, getTypesByName, getWeaknessesByName, getHeightsByName, getWeightsByName, getAvgSpawnsByName


def grafico1():
  print("Ejecutando grafico 1")
  # Variable que almacena todos los pokemones
  pokemon = getAllPokemons() 
  # Arrays que representan eje X, eje Y y Colores
  types = [] # Eje X
  cantidades = [] # Eje Y
  colors = ['green','purple','red','steelblue','navy','darkgreen','gray','yellow','olive','hotpink','magenta','peru','cyan','indigo','blue'] # Colores
  # Iteramos para definir todos los tipos de pokemon posibles
  for pkmn in range(len(pokemon)):
    tipos = getTypesByName(pokemon[pkmn]['name'])
    for i in tipos:
      if i not in types:
        types.append(i)
        cantidades.append(0)
  # Iteramos para cada tipo de 'types'
  for i in range(len(types)):
    # Iteramos para cada pkmn de 'pokemon'
    for pkmn in range(len(pokemon)):
      debilidades=getWeaknessesByName(pokemon[pkmn]['name']) # Almacena cada debilidad
      # Iteramos para cada wkns de las 'debilidades' del pkmn
      for wkns in range(len(debilidades)):
        # Si la debilidad específica coincide con el types[i], sumamos 1 a su cantidad
        if(types[i]==debilidades[wkns]):
          cantidades[i]+=1
  # Dibujamos el gráfico
  plt.bar(types, cantidades, color=colors)
  plt.title('Gráfico 1: Pokemones que son débiles a cada tipo')
  plt.show()


def grafico2():
  print("Ejecutando grafico 2") 
  # Variable que almacena todos los pokemones
  pokemon=getAllPokemons()
  # Arrays que representan eje X y eje Y
  heights=[]; weights=[]
  # Iteramos para cada pokemon
  for i in range(len(pokemon)):
    # Obtenemos altura y peso con funciones
    height=getHeightsByName(pokemon[i]['name'])
    weight=getWeightsByName(pokemon[i]['name'])
    heights.append(height)
    weights.append(weight)
  # Dibujamos el gráfico
  plt.scatter(heights,weights)
  plt.title('Gráfico 2: Altura vs. Peso')
  plt.show()


def grafico3():
  print("Ejecutando grafico 3")
  # Mostramos imagen del mapa de Kanto
  im = plt.imread('Kanto.png')
  plt.imshow(im)
  # Variable que almacena todos los pokemones
  pokemon = getAllPokemons()
  # Creamos un array para obtener todos los numeros primos desde el 2 hasta el 151
  Primo = [] 
  for Number in range(2,len(pokemon)):
    for n in range(2,Number):
      p = True 
      if Number%n==0:
        p = False
        break
      if p==True:
        Primo.append(Number)
  # Iteramos para cada pokemon con id prima y obtenemos sus coordenadas
  for i in range(len(Primo)):
   KantoDex = getLocationsByName(pokemon[Primo[i]]['name'])
   # Graficamos coordenadas usando plt.plot y el array de coordenadas (KantoDex)
   for j in range(len(KantoDex[0])-1):
     plt.plot(KantoDex[0][j], KantoDex[1][j], 'o', color="cyan")
  # Dibujamos el gráfico
  plt.title('Gráfico 3: Coordenadas de pokemones con ID prima')
  plt.show()


def grafico4():
  fig, ax = plt.subplots()
  # Variable que almacena todos los pokemones
  pokemon = getAllPokemons()
  # Arrays que representan eje X, eje Y y Colores
  types = [] # Eje X
  cantidades = [] # Eje Y
  # Iteramos para definir todos los tipos de pokemon posibles
  for pkmn in range(len(pokemon)):
    tipos = getTypesByName(pokemon[pkmn]['name'])
    for i in tipos:
      if i not in types:
        types.append(i)
        cantidades.append(0)
  # Iteramos para cada tipo de 'types'
  for i in range(len(types)):
    # Iteramos para cada pkmn de 'pokemon'
    for pkmn in range(len(pokemon)):
      tipos = getTypesByName(pokemon[pkmn]['name'])
      # Iteramos para cada tipo de los 'tipos' del pkmn
      for tp in range(len(tipos)):
        # Si el tipo del pkmn coincide con el types[i], sumamos los avg_spawns al array
        if(types[i]==tipos[tp]):
          cantidades[i]+=getAvgSpawnsByName(pokemon[pkmn]['name'])
  # Dibujamos el gráfico
  ax.plot(types, cantidades, marker='o')
  plt.title('Gráfico 4: Marcadores para el numero de avg_spawns por tipo')
  plt.show()

#grafico1()
#grafico2()
#grafico3()
#grafico4()

grafico4()