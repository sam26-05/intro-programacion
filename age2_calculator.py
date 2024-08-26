print("hola ingresa tu nombre y fecha de nacimiento")
nombre = input("ingresar nombre")
year = int(input("ingresa el año"))

edad = 2024 - year

if year<= 1948:
    print("hola", nombre,"tienes", edad, "años y pertences a la genereacion posguerra")

elif year <= 1968:
    print("hola", nombre,"tienes", edad, "años y pertences a la genereacion baby boomer")

elif year<= 1980:
    print("hola", nombre,"tienes", edad, "años y pertences a la genereacion genaracion x")

elif year <= 1993:
    print("hola", nombre,"tienes", edad, "años y pertences a la genereacion milenials")

elif year<= 2010:
    print("hola", nombre,"tienes", edad, "años y pertences a la genereacion z")

elif year > 2011:
    print("hola", nombre,"tienes", edad, "años y pertences a la genereacion alfa ")