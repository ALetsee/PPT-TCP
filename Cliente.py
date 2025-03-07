import socket
import os
import threading
import time
import json

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_ascii_logo():
    print(r"""
 _ ___ __ _  _  _     _  _  _  __      \ /   ______    __ _  _  __
|_) | |_ | \|_)|_|   |_)|_||_)|_ |      Y     |  |   ||_ |_)|_|(_ 
|  _|_|__|_/| \| |   |  | ||  |__|__    |     | _|_\_||__| \| |__)

    """)

def mostrar_marcador_ascii():

    print(r"""
   
  __  __          _____   _____          _____   ____  _____  
 |  \/  |   /\   |  __ \ / ____|   /\   |  __ \ / __ \|  __ \ 
 | \  / |  /  \  | |__) | |       /  \  | |  | | |  | | |__) |
 | |\/| | / /\ \ |  _  /| |      / /\ \ | |  | | |  | |  _  / 
 | |  | |/ ____ \| | \ \| |____ / ____ \| |__| | |__| | | \ \ 
 |_|  |_/_/    \_\_|  \_\\_____/_/    \_\_____/ \____/|_|  \_\
                                                              
                                                              

    """)

def mostrar_linea_decorativa():

    print(r"""
    ╠═════════════════════════════════════════════════════════╣
    """)

def mostrar_opciones_juego():

  print(r"""
    ╔═══════════════════════════════════════════════╗
    ║            ELIGE TU JUGADA                    ║
    ╠═══════════════════════════════════════════════╣
    ║  1. 🪨 PIEDRA    2. 📄 PAPEL    3. ✂️ TIJERA  ║
    ╚═══════════════════════════════════════════════╝
""")

def mostrar_espera_animada(mensaje, segundos=30):
    inicio = time.time()
    puntos = 1
    while time.time() - inicio < segundos:
        limpiar_pantalla()
        print(r"""

  ____                                _              _            _ 
 |  _ \                              | |            (_)          | |
 | |_) |_   _ ___  ___ __ _ _ __   __| | ___    _ __ ___   ____ _| |
 |  _ <| | | / __|/ __/ _` | '_ \ / _` |/ _ \  | '__| \ \ / / _` | |
 | |_) | |_| \__ \ (_| (_| | | | | (_| | (_) | | |  | |\ V / (_| | |
 |____/ \__,_|___/\___\__,_|_| |_|\__,_|\___/  |_|  |_| \_/ \__,_|_|
                                                                    
                                                                    

        """)
        print(f"\n{mensaje}{'.' * puntos}")
        puntos = (puntos % 3) + 1
        time.sleep(0.5)

        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                if msvcrt.getch() == b'\r':
                    return False
        else:

            print("\nPresiona Ctrl+C para cancelar la espera.")
    return True

def mostrar_resultado_ronda(tu_jugada, servidor_jugada, ganador):

    print(r"""

  _____                 _ _            _       
 |  __ \               | | |          | |      
 | |__) |___  ___ _   _| | |_ __ _  __| | ___  
 |  _  // _ \/ __| | | | | __/ _` |/ _` |/ _ \ 
 | | \ \  __/\__ \ |_| | | || (_| | (_| | (_) |
 |_|  \_\___||___/\__,_|_|\__\__,_|\__,_|\___/ 
                                               
                                               

    """)
    
    print(f"    TÚ ELEGISTE: {tu_jugada}")
    print(f"    RIVAL ELIGIÓ: {servidor_jugada}")
    print()
    
    if ganador == "Cliente":
        print(r"""

 __     __                    _       _ 
 \ \   / /                   (_)     | |
  \ \_/ /__  _   _  __      ___ _ __ | |
   \   / _ \| | | | \ \ /\ / / | '_ \| |
    | | (_) | |_| |  \ V  V /| | | | |_|
    |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
                                        
                                        

        """)
    elif ganador == "Servidor":
        print(r"""

 __     __           _           _   _ 
 \ \   / /          | |         | | | |
  \ \_/ /__  _   _  | | ___  ___| |_| |
   \   / _ \| | | | | |/ _ \/ __| __| |
    | | (_) | |_| | | | (_) \__ \ |_|_|
    |_|\___/ \__,_| |_|\___/|___/\__(_)
                                       
                                       

        """)
    else:
        print(r"""

  _____  _____       __          __
 |  __ \|  __ \     /\ \        / /
 | |  | | |__) |   /  \ \  /\  / / 
 | |  | |  _  /   / /\ \ \/  \/ /  
 | |__| | | \ \  / ____ \  /\  /   
 |_____/|_|  \_\/_/    \_\/  \/    
                                   
                                   

        """)

def mostrar_menu_principal():
    limpiar_pantalla()
    mostrar_ascii_logo()
    print(r"""
    ╔═══════════════════════════════════════╗
    ║           MENÚ PRINCIPAL              ║
    ╠═══════════════════════════════════════╣
    ║ 1. Jugar                              ║
    ║ 2. Cambiar IP y puerto                ║
    ║ 3. Salir                              ║
    ╚═══════════════════════════════════════╝
    """)

def mostrar_menu_modo_juego():
    limpiar_pantalla()
    mostrar_ascii_logo()
    print(r"""
    ╔═══════════════════════════════════════╗
    ║           MODO DE JUEGO               ║
    ╠═══════════════════════════════════════╣
    ║ 1. Jugar contra el servidor           ║
    ║ 2. Jugar contra otro cliente          ║
    ║ 3. Volver al menú principal           ║
    ╚═══════════════════════════════════════╝
    """)

def mostrar_configuracion_servidor(ip, puerto):
    print(r"""
    ╔═══════════════════════════════════════╗
    ║      CONFIGURACIÓN DEL SERVIDOR       ║
    ╠═══════════════════════════════════════╣""")
    print(f"    ║ IP: {ip:<33} ║")
    print(f"    ║ Puerto: {puerto:<29} ║")
    print(r"""    ╚═══════════════════════════════════════╝
    """)

def cliente_juego_servidor(client_id, server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            limpiar_pantalla()
            mostrar_ascii_logo()
            print(r"""

   _____                      _                  _                                _                       _     _            
  / ____|                    | |                | |                              | |                     (_)   | |           
 | |     ___  _ __   ___  ___| |_ __ _ _ __   __| | ___     ___ ___  _ __     ___| |  ___  ___ _ ____   ___  __| | ___  _ __ 
 | |    / _ \| '_ \ / _ \/ __| __/ _` | '_ \ / _` |/ _ \   / __/ _ \| '_ \   / _ \ | / __|/ _ \ '__\ \ / / |/ _` |/ _ \| '__|
 | |___| (_) | | | |  __/ (__| || (_| | | | | (_| | (_) | | (_| (_) | | | | |  __/ | \__ \  __/ |   \ V /| | (_| | (_) | |   
  \_____\___/|_| |_|\___|\___|\__\__,_|_| |_|\__,_|\___/   \___\___/|_| |_|  \___|_| |___/\___|_|    \_/ |_|\__,_|\___/|_|   
                                                                                                                             
                                                                                                                             

            """)
            print(f"\nCliente {client_id}: Conectando a {server_ip}:{server_port}...")
            cliente.connect((server_ip, server_port))
            
            cliente.send(json.dumps({"tipo": "servidor"}).encode())

            mensaje_inicial = cliente.recv(1024).decode()
            limpiar_pantalla()
            mostrar_ascii_logo()
            print(r"""

  _   _                                            
 | \ | |                                           
 |  \| | _____      __   __ _  __ _ _ __ ___   ___ 
 | . ` |/ _ \ \ /\ / /  / _` |/ _` | '_ ` _ \ / _ \
 | |\  |  __/\ V  V /  | (_| | (_| | | | | | |  __/
 |_| \_|\___| \_/\_/    \__, |\__,_|_| |_| |_|\___|
                         __/ |                     
                        |___/                      

            """)
            print(f"\nCliente {client_id}: {mensaje_inicial}", end='')
            nombre = input()
            cliente.send(nombre.encode())
            
            pregunta_rondas = cliente.recv(1024).decode()
            rondas_validas = False
            while not rondas_validas:
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(r"""

   _____      _   _   _                 
  / ____|    | | | | (_)                
 | (___   ___| |_| |_ _ _ __   __ _ ___ 
  \___ \ / _ \ __| __| | '_ \ / _` / __|
  ____) |  __/ |_| |_| | | | | (_| \__ \
 |_____/ \___|\__|\__|_|_| |_|\__, |___/
                               __/ |    
                              |___/     

                """)
                print(f"\nCliente {client_id}: {pregunta_rondas}", end='')
                rondas = input()

                if rondas.isdigit() and int(rondas) > 0:
                    rondas_validas = True
                else:
                    print(f"\nCliente {client_id}: Por favor ingresa un número válido de rondas.")
                    time.sleep(1.5)
            
            cliente.send(rondas.encode())

            for i in range(int(rondas)):
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(f"""
    ╔═══════════════════════════════════════╗
    ║              RONDA {i+1}/{rondas}                ║
    ╚═══════════════════════════════════════╝
                """)
                menu = cliente.recv(1024).decode()
                mostrar_opciones_juego()

                jugada = ""
                while jugada not in ['1', '2', '3']:
                    print(f"Opción: ", end='')
                    jugada = input()
                    if jugada not in ['1', '2', '3']:
                        print(f"\nCliente {client_id}: Opción incorrecta. Por favor, ingresa 1, 2 o 3.")
                
                cliente.send(jugada.encode())

                resultado = cliente.recv(1024).decode()

                try:
                    tu_jugada = resultado.split(', ')[0].split(': ')[1]
                    servidor_jugada = resultado.split(', ')[1].split(': ')[1]
                    ganador = resultado.split('. ')[1].split(': ')[1]
                    
                    limpiar_pantalla()
                    mostrar_resultado_ronda(tu_jugada, servidor_jugada, ganador)
                    
                except Exception as e:
                    print(f"\nError al procesar resultado: {e}")
                    print(f"Resultado recibido: {resultado}")
                
                if i < int(rondas) - 1:
                    input("\nPress Enter")

            resultado_final = cliente.recv(1024).decode()
            print(r"""

  _____                 _ _            _           
 |  __ \               | | |          | |          
 | |__) |___  ___ _   _| | |_ __ _  __| | ___  ___ 
 |  _  // _ \/ __| | | | | __/ _` |/ _` |/ _ \/ __|
 | | \ \  __/\__ \ |_| | | || (_| | (_| | (_) \__ \
 |_|  \_\___||___/\__,_|_|\__\__,_|\__,_|\___/|___/
                                                   
                                                   

            """)
            print(resultado_final)
            mostrar_linea_decorativa()
            
            input("\nPresiona Enter para volver al menú principal")
            
    except ConnectionRefusedError:
        limpiar_pantalla()
        print(r"""
   _____                      _                  _                                _                       _     _            
  / ____|                    | |                | |                              | |                     (_)   | |           
 | |     ___  _ __   ___  ___| |_ __ _ _ __   __| | ___     ___ ___  _ __     ___| |  ___  ___ _ ____   ___  __| | ___  _ __ 
 | |    / _ \| '_ \ / _ \/ __| __/ _` | '_ \ / _` |/ _ \   / __/ _ \| '_ \   / _ \ | / __|/ _ \ '__\ \ / / |/ _` |/ _ \| '__|
 | |___| (_) | | | |  __/ (__| || (_| | | | | (_| | (_) | | (_| (_) | | | | |  __/ | \__ \  __/ |   \ V /| | (_| | (_) | |   
  \_____\___/|_| |_|\___|\___|\__\__,_|_| |_|\__,_|\___/   \___\___/|_| |_|  \___|_| |___/\___|_|    \_/ |_|\__,_|\___/|_|   
  
        """)
        print(f"\nCliente {client_id} - Error: No se pudo conectar al servidor {server_ip}:{server_port}.")
        print("Verifica que el servidor esté en ejecución.")
        input("\nPresiona Enter para volver al menú principal")
    except Exception as e:
        limpiar_pantalla()
        print(r"""

  ______                     
 |  ____|                    
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|   
                             
                             

        """)
        print(f"\nCliente {client_id} - Error: {e}")
        input("\nPresiona Enter para volver al menú principal")

def cliente_juego_multijugador(client_id, server_ip, server_port):
    """Función para jugar contra otro cliente."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            limpiar_pantalla()
            mostrar_ascii_logo()
            print(r"""
   _____                      _                  _                                _                       _     _            
  / ____|                    | |                | |                              | |                     (_)   | |           
 | |     ___  _ __   ___  ___| |_ __ _ _ __   __| | ___     ___ ___  _ __     ___| |  ___  ___ _ ____   ___  __| | ___  _ __ 
 | |    / _ \| '_ \ / _ \/ __| __/ _` | '_ \ / _` |/ _ \   / __/ _ \| '_ \   / _ \ | / __|/ _ \ '__\ \ / / |/ _` |/ _ \| '__|
 | |___| (_) | | | |  __/ (__| || (_| | | | | (_| | (_) | | (_| (_) | | | | |  __/ | \__ \  __/ |   \ V /| | (_| | (_) | |   
  \_____\___/|_| |_|\___|\___|\__\__,_|_| |_|\__,_|\___/   \___\___/|_| |_|  \___|_| |___/\___|_|    \_/ |_|\__,_|\___/|_|   
            """)
            print(f"\nCliente {client_id}: Conectando a {server_ip}:{server_port}...")
            cliente.connect((server_ip, server_port))

            limpiar_pantalla()
            mostrar_ascii_logo()
            print(r"""
   _____                      _                  _                                _                       _     _            
  / ____|                    | |                | |                              | |                     (_)   | |           
 | |     ___  _ __   ___  ___| |_ __ _ _ __   __| | ___     ___ ___  _ __     ___| |  ___  ___ _ ____   ___  __| | ___  _ __ 
 | |    / _ \| '_ \ / _ \/ __| __/ _` | '_ \ / _` |/ _ \   / __/ _ \| '_ \   / _ \ | / __|/ _ \ '__\ \ / / |/ _` |/ _ \| '__|
 | |___| (_) | | | |  __/ (__| || (_| | | | | (_| | (_) | | (_| (_) | | | | |  __/ | \__ \  __/ |   \ V /| | (_| | (_) | |   
  \_____\___/|_| |_|\___|\___|\__\__,_|_| |_|\__,_|\___/   \___\___/|_| |_|  \___|_| |___/\___|_|    \_/ |_|\__,_|\___/|_|   
            """)
            print("\nIngresa tu nombre: ", end='')
            nombre = input()

            cliente.send(json.dumps({"tipo": "multijugador", "nombre": nombre}).encode())
            

            print("\nEsperando a que otro jugador se conecte...")
            print("(El servidor te emparejará con otro jugador)")
            print("Presiona Enter en cualquier momento para cancelar")

            cliente.setblocking(False)
            
            inicio = time.time()
            esperando = True
            while esperando and time.time() - inicio < 120:
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(r"""

  _____          ____                        
 |_   _|        / __ \                       
   | |  _ __   | |  | |_   _  ___ _   _  ___ 
   | | | '_ \  | |  | | | | |/ _ \ | | |/ _ \
  _| |_| | | | | |__| | |_| |  __/ |_| |  __/
 |_____|_| |_|  \___\_\\__,_|\___|\__,_|\___|
                                             
                                             

                """)
                puntos = '.' * (int(time.time() - inicio) % 4)
                print(f"\nEsperando a otro jugador{puntos}")
                print(f"Nombre: {nombre}")
                print("Presiona Enter para cancelar")
                

                try:
                    cliente.settimeout(0.1)
                    respuesta = cliente.recv(1024).decode()
                    if respuesta:

                        esperando = False
                        limpiar_pantalla()
                        mostrar_ascii_logo()
                        print(r"""

       _       _       _             _ 
      | |     (_)     (_)           | |
      | | ___  _ _ __  _ _ __   __ _| |
  _   | |/ _ \| | '_ \| | '_ \ / _` | |
 | |__| | (_) | | | | | | | | | (_| |_|
  \____/ \___/|_|_| |_|_|_| |_|\__, (_)
                                __/ |  
                               |___/   

                        """)
                        print("\n¡Jugador encontrado! Iniciando partida...")
                        print(f"Mensaje del servidor: {respuesta}")
                        time.sleep(1.5)
                        break
                except socket.timeout:
                    pass
                except BlockingIOError:
                    pass
                
                if os.name == 'nt':
                    import msvcrt
                    if msvcrt.kbhit():
                        if msvcrt.getch() == b'\r':
                            limpiar_pantalla()
                            mostrar_ascii_logo()
                            print(r"""

   ____                                                   _          _ 
  / __ \                                                 | |        | |
 | |  | |_   _  ___ _   _  ___    ___ __ _ _ __   ___ ___| | ___  __| |
 | |  | | | | |/ _ \ | | |/ _ \  / __/ _` | '_ \ / __/ _ \ |/ _ \/ _` |
 | |__| | |_| |  __/ |_| |  __/ | (_| (_| | | | | (_|  __/ |  __/ (_| |
  \___\_\\__,_|\___|\__,_|\___|  \___\__,_|_| |_|\___\___|_|\___|\__,_|
                                                                       
                                                                       

                            """)
                            print("\nCancelando búsqueda de jugador...")
                            cliente.close()
                            time.sleep(1.5)
                            return
                
                time.sleep(0.5)
            
            if esperando:
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(r"""

  _______ _                              _   
 |__   __(_)                            | |  
    | |   _ _ __ ___   ___    ___  _   _| |_ 
    | |  | | '_ ` _ \ / _ \  / _ \| | | | __|
    | |  | | | | | | |  __/ | (_) | |_| | |_ 
    |_|  |_|_| |_| |_|\___|  \___/ \__,_|\__|
                                             
                                             

                """)
                print("\nSe agotó el tiempo de espera. No se encontró otro jugador.")
                cliente.close()
                input("\nPresiona Enter para volver al menú principal")
                return
            
            cliente.setblocking(True)
            

            try:
                
                mensaje_rondas = cliente.recv(1024).decode()
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(r"""

   _____      _   _   _                 
  / ____|    | | | | (_)                
 | (___   ___| |_| |_ _ _ __   __ _ ___ 
  \___ \ / _ \ __| __| | '_ \ / _` / __|
  ____) |  __/ |_| |_| | | | | (_| \__ \
 |_____/ \___|\__|\__|_|_| |_|\__, |___/
                               __/ |    
                              |___/     

                """)
                print(f"\n{mensaje_rondas}")
                
                if "Tú decides" in mensaje_rondas:
           
                    rondas_validas = False
                    while not rondas_validas:
                        print("\nIngresa el número de rondas: ", end='')
                        rondas = input()
                        if rondas.isdigit() and int(rondas) > 0:
                            rondas_validas = True
                            num_rondas = int(rondas)
                        else:
                            print("\nPor favor ingresa un número válido de rondas.")
                    
                    cliente.send(rondas.encode())
                else:

                    print("\nEsperando el número de rondas...")

                    rondas = cliente.recv(1024).decode()
                    num_rondas = int(rondas)
                    print(f"\nSe jugarán {rondas} rondas")
                    time.sleep(1)
            

                for i in range(num_rondas):
                    limpiar_pantalla()
                    mostrar_ascii_logo()
                    print(f"""
    ╔═══════════════════════════════════════╗
    ║              RONDA {i+1}/{num_rondas}                ║
    ╚═══════════════════════════════════════╝
                    """)
                    

                    menu = cliente.recv(1024).decode()
                    mostrar_opciones_juego()
                    
                    jugada = ""
                    while jugada not in ['1', '2', '3']:
                        print(f"Opción: ", end='')
                        jugada = input()
                        if jugada not in ['1', '2', '3']:
                            print("\nOpción incorrecta. Por favor, ingresa 1, 2 o 3.")
                    
                    cliente.send(jugada.encode())
                    

                    limpiar_pantalla()
                    mostrar_ascii_logo()
                    print(r"""

 __          __   _ _   _                __                                                      _   
 \ \        / /  (_) | (_)              / _|                                                    | |  
  \ \  /\  / /_ _ _| |_ _ _ __   __ _  | |_ ___  _ __    ___  _ __  _ __   ___  _ __   ___ _ __ | |_ 
   \ \/  \/ / _` | | __| | '_ \ / _` | |  _/ _ \| '__|  / _ \| '_ \| '_ \ / _ \| '_ \ / _ \ '_ \| __|
    \  /\  / (_| | | |_| | | | | (_| | | || (_) | |    | (_) | |_) | |_) | (_) | | | |  __/ | | | |_ 
     \/  \/ \__,_|_|\__|_|_| |_|\__, | |_| \___/|_|     \___/| .__/| .__/ \___/|_| |_|\___|_| |_|\__|
                                 __/ |                       | |   | |                               
                                |___/                        |_|   |_|                               

                    """)
                    print("\nEsperando la jugada del oponente...")
                    

                    resultado = cliente.recv(1024).decode()
                    
                    limpiar_pantalla()
                    mostrar_ascii_logo()
                    print(f"""
    ╔═══════════════════════════════════════╗
    ║        RESULTADO DE LA RONDA {i+1}        ║
    ╚═══════════════════════════════════════╝
                    """)
                    print(resultado)
                    mostrar_linea_decorativa()
                    
                    if i < num_rondas - 1:
                        input("\nPresiona Enter")
                

                resultado_final = cliente.recv(1024).decode()
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(r"""

  _____                 _ _            _           
 |  __ \               | | |          | |          
 | |__) |___  ___ _   _| | |_ __ _  __| | ___  ___ 
 |  _  // _ \/ __| | | | | __/ _` |/ _` |/ _ \/ __|
 | | \ \  __/\__ \ |_| | | || (_| | (_| | (_) \__ \
 |_|  \_\___||___/\__,_|_|\__\__,_|\__,_|\___/|___/
                                                   
                                                   

                """)
                print(resultado_final)
                mostrar_linea_decorativa()
                
            except Exception as e:
                limpiar_pantalla()
                mostrar_ascii_logo()
                print(r"""

  ______                     
 |  ____|                    
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|   
                             
                             

                """)
                print(f"\nError durante el juego: {e}")
                print(f"Detalles: {str(e)}")
            
            input("\nPresiona Enter")
            
    except ConnectionRefusedError:
        limpiar_pantalla()
        mostrar_ascii_logo()
        print(r"""

  ______                     
 |  ____|                    
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|   
                             
                             

        """)
        print(f"\nError: No se pudo conectar al servidor {server_ip}:{server_port}.")
        print("Verifica que el servidor esté en ejecución.")
        input("\nPresiona Enter")
    except Exception as e:
        limpiar_pantalla()
        mostrar_ascii_logo()
        print(r"""

  ______                     
 |  ____|                    
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|   
                             
                             

        """)
        print(f"\nError: {e}")
        input("\nPresiona Enter para volver al menú principal")

def main():
    limpiar_pantalla()
    mostrar_ascii_logo()
    print(r"""

   _____                                     _   _   _                 
  / ____|                                   | | | | (_)                
 | (___   ___ _ ____   _____ _ __   ___  ___| |_| |_ _ _ __   __ _ ___ 
  \___ \ / _ \ '__\ \ / / _ \ '__| / __|/ _ \ __| __| | '_ \ / _` / __|
  ____) |  __/ |   \ V /  __/ |    \__ \  __/ |_| |_| | | | | (_| \__ \
 |_____/ \___|_|    \_/ \___|_|    |___/\___|\__|\__|_|_| |_|\__, |___/
                                                              __/ |    
                                                             |___/     

    """)
    ip_servidor = input("Introduce la dirección IP del servidor (vacío para localhost): ")
    if not ip_servidor:
        ip_servidor = 'localhost'
    
    puerto_str = input("Introduce el puerto del servidor (vacío para 65535): ")
    puerto_servidor = 65535  # Puerto
    if puerto_str and puerto_str.isdigit():
        puerto_servidor = int(puerto_str)
    
    mostrar_configuracion_servidor(ip_servidor, puerto_servidor)
    time.sleep(1)
    
    num_clientes = 0
    
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            mostrar_menu_modo_juego()
            modo = input("\nSelecciona el modo de juego: ")
            
            if modo == '1':
                num_clientes += 1
                cliente_juego_servidor(num_clientes, ip_servidor, puerto_servidor)
                
            elif modo == '2':
                num_clientes += 1
                cliente_juego_multijugador(num_clientes, ip_servidor, puerto_servidor)
                
            elif modo == '3':
                continue
            else:
                print("\nOpción inválida. Volviendo al menú principal...")
                time.sleep(1.5)
                
        elif opcion == '2':
            limpiar_pantalla()
            mostrar_ascii_logo()
            print(r"""

   _____                                     _   _   _                 
  / ____|                                   | | | | (_)                
 | (___   ___ _ ____   _____ _ __   ___  ___| |_| |_ _ _ __   __ _ ___ 
  \___ \ / _ \ '__\ \ / / _ \ '__| / __|/ _ \ __| __| | '_ \ / _` / __|
  ____) |  __/ |   \ V /  __/ |    \__ \  __/ |_| |_| | | | | (_| \__ \
 |_____/ \___|_|    \_/ \___|_|    |___/\___|\__|\__|_|_| |_|\__, |___/
                                                              __/ |    
                                                             |___/     

            """)
            nueva_ip = input("Introduce la dirección IP del servidor (vacío para localhost): ")
            if not nueva_ip:
                ip_servidor = 'localhost'
            else:
                ip_servidor = nueva_ip
            
            puerto_str = input(f"Introduce el puerto del servidor (vacío para {puerto_servidor}): ")
            if puerto_str and puerto_str.isdigit():
                puerto_servidor = int(puerto_str)
            
            mostrar_configuracion_servidor(ip_servidor, puerto_servidor)
            time.sleep(1.5)
            
        elif opcion == '3':
            limpiar_pantalla()
            mostrar_ascii_logo()
            print(r"""

  ____             
 |  _ \            
 | |_) |_   _  ___ 
 |  _ <| | | |/ _ \
 | |_) | |_| |  __/
 |____/ \__, |\___|
         __/ |     
        |___/      

            """)
            print("\nExit...")
            time.sleep(1.5)
            break
        else:
            print("\nOpción inválida. Por favor selecciona 1, 2 o 3.")
            time.sleep(1.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        limpiar_pantalla()
        mostrar_ascii_logo()
        print(r"""

  ______ _       _     _              _ 
 |  ____(_)     (_)   | |            | |
 | |__   _ _ __  _ ___| |__   ___  __| |
 |  __| | | '_ \| / __| '_ \ / _ \/ _` |
 | |    | | | | | \__ \ | | |  __/ (_| |
 |_|    |_|_| |_|_|___/_| |_|\___|\__,_|
                                        
                                        

        """)
        print("\n\nPrograma terminado por el usuario.")
        time.sleep(1)