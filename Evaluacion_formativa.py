pikachu_roll = 4500
otaku_roll = 5000
pulpo_venenoso_roll = 5200
anguila_electrica_roll = 4800
sushi = 0
total = 0
codigo_descuento = .10
tipo = 0
eleccion = 0
print("""Elija una opcion de sushi que desea pedir
      1. Pikachu Roll
      2. Otaku Roll
      3. Pulpo Venenoso Roll
      4. Anguila Electrica Roll
      5. Desea hacer otro pedido""")


while sushi != 6:

    eleccion == int (input("Elija una opcion entre 1-5: "))
    if sushi == 1:
        print("Has elejido Opcion 1")
        eleccion += pikachu_roll

    elif sushi == 2:
        print("Has elejido Opcion 2")
        eleccion += otaku_roll

    elif sushi == 3:
        print("Has elejido Opcion 3")
        eleccion += pulpo_venenoso_roll

    elif sushi == 4:
        print("Has elejido Opcion 4")
        eleccion += anguila_electrica_roll

    elif sushi == 5:
        print("Desea hacer otro pedido")
        break
    else:
        print("Elija una opcion entre 1-5")

    

