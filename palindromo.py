#6. Testar se uma palavra é um palíndromo:

palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
   palavra = palavra.lower().replace(" ", "") 
if palavra == palavra[::-1]: 
    print(f"A palavra '{palavra}' é um PALÍNDROMO.") 
else: 
    print(f"A palavra '{palavra}' NÃO é um palíndromo.")