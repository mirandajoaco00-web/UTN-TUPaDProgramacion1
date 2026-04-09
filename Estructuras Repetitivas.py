## Ejercicio 1 ##
nombre = input("Ingrese su nombre: ")
producto = int(input("Ingrese cantidad de productos: "))

total_descuento = 0
total_sindescuento = 0

for i in range(0, producto):
    precio_input = input(f"Ingrese precio de producto {i+1}: ")
    
    if precio_input.isdigit():
        precio = int(precio_input)
       
        total_sindescuento += precio 
        
      
        opcion_descuento = input("¿Tiene descuento? S/N: ").lower()
        while opcion_descuento not in ['s', 'n']:
            opcion_descuento = input("Error, ingrese S o N: ").lower()

        if opcion_descuento == 's':
            precio_final = precio * 0.90
        else:
            precio_final = precio

        
        total_descuento += precio_final 
        
    else:
        print("Precio no válido")


ahorro = total_sindescuento - total_descuento
promedio = total_descuento / producto

print(f"\nTotal sin descuentos: ${total_sindescuento}")
print(f"Total con descuentos: ${total_descuento}")
print(f"Ahorro total: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")


## Ejercicio 2 ##

usuario_correcto = "alumno"
clave_correcta = "python123"


for i in range(3):
    usuario_ingresado = input("Ingrese un usuario: ")
    clave_ingresada = input("Ingrese una clave: ")

    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("!Bienvenido")
        

        opcion = ""
        while opcion != "4":
            print("\n--- MENÚ ---")
            print("1. Estado / 2. Cambiar clave / 3. Frase / 4. Salir")
            opcion = input("Elegir una opcion: ")

            # Punto 5: Validar si es número
            if opcion.isdigit():
                if opcion == "1":
                    print("Estado: Inscripto")
                
                elif opcion == "2":
                    nueva_clave = input("Ingrese una nueva clave: ")
                    if len(nueva_clave) >= 6:
                        repetir_clave = input("Por favor repetir la clave: ")
                        if nueva_clave == repetir_clave:
                            clave_correcta = nueva_clave
                            print("Clave cambiada con éxito")
                        else:
                            print("Error: Las claves no coinciden")
                    else:
                        print("Error: La clave debe tener al menos 6 caracteres")
                
                elif opcion == "3":
                    print("Frase: El éxito es la suma de pequeños esfuerzos repetidos día tras día.")
                
                elif opcion == "4":
                    print("Saliendo del sistema...")
                
                else:
                    print("Opción no válida, debe ser entre 1 y 4")
            else:
                print("Error: Ingresá un número válido (1-4)")
        
        
        break 

    else:
        
        if i < 2:
            print(f"Datos incorrectos. Te quedan {2-i} intentos.")
        else:
            print("Cuenta bloqueada. Agotaste tus 3 intentos.")


## Ejercicio 3

lunes1 = ""; lunes2 = ""; lunes3 = ""; lunes4 = ""
martes1 = ""; martes2 = ""; martes3 = ""


usuario = input("Ingrese su usuario (solo letras): ")

menu = ""
while menu != "5":
    print("\n--- SISTEMA DE TURNOS ---")
    print("1. Reservar / 2. Cancelar / 3. Ver Agenda / 4. Resumen / 5. Salir")
    menu = input("Elija una opción: ")

    if menu == "1":
        dia = input("Día (1=Lun / 2=Mar): ")
        paciente = input("Nombre: ")
        
        if paciente.isalpha():
            if dia == "1":
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: El paciente ya tiene turno el lunes.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Reservado en Lunes 1")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Reservado en Lunes 2")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Reservado en Lunes 3")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Reservado en Lunes 4")
                else:
                    print("Lunes completo.")
            
            elif dia == "2":
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: El paciente ya tiene turno el martes.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Reservado en Martes 1")
                elif martes2 == "":
                    martes2 = paciente
                    print("Reservado en Martes 2")
                elif martes3 == "":
                    martes3 = paciente
                    print("Reservado en Martes 3")
                else:
                    print("Martes completo.")
        else:
            print("Error: Solo letras.")

    elif menu == "2":
        dia_restado = 0
        cancelar_dia = input("Día a cancelar (1/2): ")
        paciente_cancelar = input("Nombre del paciente: ")

        if cancelar_dia == "1":
            if paciente_cancelar == lunes1: lunes1 = ""; dia_restado = 1
            if paciente_cancelar == lunes2: lunes2 = ""; dia_restado = 1
            if paciente_cancelar == lunes3: lunes3 = ""; dia_restado = 1
            if paciente_cancelar == lunes4: lunes4 = ""; dia_restado = 1
        elif cancelar_dia == "2":
            if paciente_cancelar == martes1: martes1 = ""; dia_restado = 1
            if paciente_cancelar == martes2: martes2 = ""; dia_restado = 1
            if paciente_cancelar == martes3: martes3 = ""; dia_restado = 1

        if dia_restado == 1:
            print("Turno cancelado con éxito.")
        else:
            print("No se encontró al paciente.")

    elif menu == "3":
        ver_dia = input("¿Qué agenda ver? (1=Lun / 2=Mar): ")
        if ver_dia == "1":
            print("\n--- LUNES ---")
            if lunes1 == "": print("Turno 1: (libre)") 
            else: print("Turno 1:", lunes1)
            if lunes2 == "": print("Turno 2: (libre)") 
            else: print("Turno 2:", lunes2)
            if lunes3 == "": print("Turno 3: (libre)") 
            else: print("Turno 3:", lunes3)
            if lunes4 == "": print("Turno 4: (libre)") 
            else: print("Turno 4:", lunes4)
        elif ver_dia == "2":
            print("\n--- MARTES ---")
            if martes1 == "": print("Turno 1: (libre)") 
            else: print("Turno 1:", martes1)
            if martes2 == "": print("Turno 2: (libre)") 
            else: print("Turno 2:", martes2)
            if martes3 == "": print("Turno 3: (libre)") 
            else: print("Turno 3:", martes3)

    elif menu == "4":
        cupos_lunes = 0
        if lunes1 != "": cupos_lunes += 1
        if lunes2 != "": cupos_lunes += 1
        if lunes3 != "": cupos_lunes += 1
        if lunes4 != "": cupos_lunes += 1
        
        cupos_martes = 0
        if martes1 != "": cupos_martes += 1
        if martes2 != "": cupos_martes += 1
        if martes3 != "": cupos_martes += 1
        
        print("Turnos ocupados Lunes:", cupos_lunes)
        print("Turnos ocupados Martes:", cupos_martes)

        
        if cupos_lunes > cupos_martes:
            print("Lunes tiene más turnos ocupados.")
        elif cupos_martes > cupos_lunes:
            print("Martes tiene más turnos ocupados.")
        else:
            print("Ambos días tienen la misma cantidad de turnos.")

    elif menu == "5":
        print("Saliendo del sistema...")


        ## Ejercicio 4


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
Contador_forzar = 0


nombre = input("Ingrese el nombre del agente (solo letras): ")
while not nombre.isalpha():
    nombre = input("Error. Ingrese solo letras: ")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    
    print(f"\n--- ESTADO: Energía {energia} | Tiempo {tiempo} | Cerraduras {cerraduras_abiertas} ---")
    print("1. Forzar Cerradura / 2. Hackear Panel / 3. Descansar / 5. Salir")
    
    menu = input("Elije una opción: ")
    while not menu.isdigit(): 
        menu = input("Error. Elije una opción numérica (1, 2, 3 o 5): ")

    if menu == "1":
        Contador_forzar += 1
        energia -= 20
        tiempo -= 2
        
      
        if Contador_forzar == 3:
            print("!Alarma activada.")
            alarma = True
        else:
          
            if energia < 40:
                print("Riesgo de alarma...")
                alarma_input = input("Elija un número (1, 2 o 3): ")
                while not alarma_input.isdigit():
                    alarma_input = input("Debe ser un número. Elija 1, 2 o 3: ")
                
                if alarma_input == "3":
                    alarma = True
            
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Lograste abrir una cerradura!")

    elif menu == "2":
        Contador_forzar = 0 
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = "" # Reiniciamos el código tras usarlo
                print("Se abrio una cerradura")

    elif menu == "3":
        Contador_forzar = 0
        tiempo -= 1
        energia += 15
        
        if alarma: 
            print("¡alarma activada!")
            energia -= 10
            
        if energia > 100:
            energia = 100
        print(f"Energía actual: {energia}")

    elif menu == "5":
        print("salida..")
        break


print("\n--- RESULTADO FINAL ---")

if cerraduras_abiertas == 3:
    print("¡Felicitaciones Has ganado")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")



## Ejercicio 5


nombre_usuario = input("Ingrese nombre de usuario: ")
while not nombre_usuario.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_usuario = input("Ingrese nombre de usuario: ")


vida_enemigo = 100              
pociones_vida = 3               
daño_base_pesado = 15           
daño_base_enemigo = 12         
turno_gladiador = True          


while vida_gladiador > 0 and vida_enemigo > 0:
    
   
    print(f"\n--- NUEVO TURNO ---")
    print(f"{nombre_usuario} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion_usuario = input("Opción: ") 
    
   
    while not opcion_usuario.isdigit():
        print("Error: Ingrese un número válido.")
        opcion_usuario = input("Opción: ")
        
    
    if opcion_usuario == "1":
        if vida_enemigo < 20:
            daño_final = daño_base_pesado * 1.5 
            print(f"¡GOLPE CRÍTICO! Daño multiplicado a {daño_final}")
        else:
            daño_final = daño_base_pesado
            
        vida_enemigo -= daño_final
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")

    
    elif opcion_usuario == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    
    elif opcion_usuario == "3":
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1
            print(f"Te has curado. Vida actual: {vida_gladiador}")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
    
    else:
        print("Opción no válida (debe ser 1, 2 o 3). Pierdes el turno.")

    
    if vida_enemigo > 0:
        vida_gladiador -= daño_base_enemigo
        print(f">> ¡El enemigo te atacó por {daño_base_enemigo} puntos de daño!")


print("\n=== RESULTADO FINAL ===")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_usuario} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")