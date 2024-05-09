pikachu_roll = 0
otaku_roll = 0
pulpo_venenoso_roll = 0
anguila_electrica_roll = 0
codigo_descuento = .10
sushi = 0


while True:

    sushi = int(input("""
                      Elija una opcion de sushi que desea pedir
                        1. Pikachu Roll
                        2. Otaku Roll
                        3. Pulpo Venenoso Roll
                        4. Anguila Electrica Roll
                       Elija una opcion entre 1-4
                       presiona 5 para avanzar
                       presiona 6 para salir: """))
    
    if sushi == 1:
        print("Has elejido Opcion 1")
        
        pikachu_roll += 1
    elif sushi == 2:
        print("Has elejido Opcion 2")
        
        otaku_roll += 1
    elif sushi == 3:
        print("Has elejido Opcion 3")
        
        pulpo_venenoso_roll += 1
    elif sushi == 4:
        print("Has elejido Opcion 4")
        
        anguila_electrica_roll += 1

    elif sushi == 5:
        total_productos = (pikachu_roll + otaku_roll + pulpo_venenoso_roll + anguila_electrica_roll)
        total_pagar = (pikachu_roll * 4500 + otaku_roll * 5000 + pulpo_venenoso_roll * 5200 + anguila_electrica_roll * 4800)
        
        while True:
            cupon = input("¿Posee algun codigo de descuento responder? si / no: ")
            if cupon == "si":
                descuento = input("Ingrese su cupon de descuento: ")
                if descuento == "soyotaku":
                    total_descuento_pagar = total_pagar * codigo_descuento
            print(f"""
                      *****************************
                    Total Productos:{total_productos}
                      *****************************
                      Pikachu Roll: {pikachu_roll}
                      Otaku Roll  : {otaku_roll}
                      Pulpo Venenoso Roll  : {pulpo_venenoso_roll}
                      Anguila Electrica Roll: {anguila_electrica_roll}
                      *****************************
                      Subtotal a Pagar: {total_pagar}
                      Descuento por codigo: {round(total_descuento_pagar)}
                      Total: {round(total_pagar - total_descuento_pagar)}""")
            break
        


    elif sushi == 6:
        print("Gracias por su compra")
        break
    

    

