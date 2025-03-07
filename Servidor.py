import socket
import threading
import random
import json
import time

clientes_esperando = []
lock_clientes = threading.Lock() 

def manejar_cliente_servidor(cliente, direccion):
    """Maneja un juego entre un cliente y el servidor (CPU)"""
    try:
        cliente.send("Ingresa tu nombre: ".encode())
        nombre = cliente.recv(1024).decode()
    
        cliente.send("¿Cuántas rondas quieres jugar? ".encode())
        rondas = cliente.recv(1024).decode()
        
        puntos_cliente = 0
        puntos_servidor = 0
        
        opciones = {
            '1': 'Piedra',
            '2': 'Papel',
            '3': 'Tijera'
        }
        
        for i in range(int(rondas)):
            menu = f"""
Ronda {i+1} de {rondas}
Puntuación: {nombre} {puntos_cliente} - {puntos_servidor} Servidor

Elige tu jugada:
1. Piedra
2. Papel
3. Tijera
Tu elección: """
            
            cliente.send(menu.encode())
            jugada_cliente = cliente.recv(1024).decode()
            
            jugada_servidor = str(random.randint(1, 3))
            
            ganador = "Empate"
            if jugada_cliente != jugada_servidor:
                if (jugada_cliente == '1' and jugada_servidor == '3') or \
                   (jugada_cliente == '2' and jugada_servidor == '1') or \
                   (jugada_cliente == '3' and jugada_servidor == '2'):
                    ganador = "Cliente"
                    puntos_cliente += 1
                else:
                    ganador = "Servidor"
                    puntos_servidor += 1
            
            resultado = f"Tu elección: {opciones[jugada_cliente]}, Servidor: {opciones[jugada_servidor]}. Ganador: {ganador}"
            cliente.send(resultado.encode())
        
        if puntos_cliente > puntos_servidor:
            ganador_final = f"¡Felicidades {nombre}! Has ganado el juego."
        elif puntos_servidor > puntos_cliente:
            ganador_final = f"El servidor ha ganado el juego.!"
        else:
            ganador_final = f"¡Empate final! {nombre} {puntos_cliente} - {puntos_servidor} Servidor"
        
        resultado_final = f"Puntuación final:\n{nombre}: {puntos_cliente}\nServidor: {puntos_servidor}\n\n{ganador_final}"
        cliente.send(resultado_final.encode())
        
    except Exception as e:
        print(f"Error con el cliente {direccion}: {e}")
    finally:
        cliente.close()
        print(f"Conexión cerrada con {direccion}")

def manejar_juego_multijugador(cliente1, dir1, nombre1, cliente2, dir2, nombre2):
    """Maneja un juego entre dos clientes"""
    try:
        print(f"Iniciando juego multijugador entre {nombre1} y {nombre2}")
        
      
        cliente1.send(f"¡Oponente encontrado! Jugarás contra {nombre2}".encode())
        cliente2.send(f"¡Oponente encontrado! Jugarás contra {nombre1}".encode())
        time.sleep(1) 
        
   
        cliente1.send(f"Tú decides las rondas. ¿Cuántas rondas quieres jugar?".encode())
        rondas = cliente1.recv(1024).decode()
        
 
        cliente2.send(f"{nombre1} ha elegido jugar {rondas} rondas.".encode())
        time.sleep(0.5)  
        
      
        cliente2.send(f"{rondas}".encode())
        time.sleep(0.5)  
        
        puntos_cliente1 = 0
        puntos_cliente2 = 0
        
        opciones = {
            '1': 'Piedra',
            '2': 'Papel',
            '3': 'Tijera'
        }
        
        for i in range(int(rondas)):
     
            menu1 = f"""
Ronda {i+1} de {rondas}
Puntuación: {nombre1} {puntos_cliente1} - {puntos_cliente2} {nombre2}

Elige tu jugada:
1. Piedra
2. Papel
3. Tijera
Tu elección: """

            menu2 = f"""
Ronda {i+1} de {rondas}
Puntuación: {nombre2} {puntos_cliente2} - {puntos_cliente1} {nombre1}

Elige tu jugada:
1. Piedra
2. Papel
3. Tijera
Tu elección: """
            

            cliente1.send(menu1.encode())
            cliente2.send(menu2.encode())
            

            jugada_cliente1 = cliente1.recv(1024).decode()
            jugada_cliente2 = cliente2.recv(1024).decode()
            

            ganador = "Empate"
            if jugada_cliente1 != jugada_cliente2:
                if (jugada_cliente1 == '1' and jugada_cliente2 == '3') or \
                   (jugada_cliente1 == '2' and jugada_cliente2 == '1') or \
                   (jugada_cliente1 == '3' and jugada_cliente2 == '2'):
                    ganador = nombre1
                    puntos_cliente1 += 1
                else:
                    ganador = nombre2
                    puntos_cliente2 += 1
            

            resultado1 = f"Tu elección: {opciones[jugada_cliente1]}, {nombre2}: {opciones[jugada_cliente2]}. Ganador: {ganador}"
            resultado2 = f"Tu elección: {opciones[jugada_cliente2]}, {nombre1}: {opciones[jugada_cliente1]}. Ganador: {ganador}"
            
            cliente1.send(resultado1.encode())
            cliente2.send(resultado2.encode())
            

            time.sleep(0.5)
        

        if puntos_cliente1 > puntos_cliente2:
            ganador_final1 = f"¡Felicidades! Has ganado el juego contra {nombre2}."
            ganador_final2 = f"{nombre1} ha ganado el juego."
        elif puntos_cliente2 > puntos_cliente1:
            ganador_final1 = f"{nombre2} ha ganado el juego."
            ganador_final2 = f"¡Felicidades! Has ganado el juego contra {nombre1}."
        else:
            ganador_final1 = ganador_final2 = f"¡Empate final!"
        
        resultado_final1 = f"Puntuación final:\n{nombre1}: {puntos_cliente1}\n{nombre2}: {puntos_cliente2}\n\n{ganador_final1}"
        resultado_final2 = f"Puntuación final:\n{nombre2}: {puntos_cliente2}\n{nombre1}: {puntos_cliente1}\n\n{ganador_final2}"
        
        cliente1.send(resultado_final1.encode())
        cliente2.send(resultado_final2.encode())
        
    except Exception as e:
        print(f"Error en el juego multijugador: {e}")
     
        try:
            mensaje_error = f"Error en la partida: {str(e)}"
            cliente1.send(mensaje_error.encode())
            cliente2.send(mensaje_error.encode())
        except:
            pass
    finally:
        try:
            cliente1.close()
            cliente2.close()
        except:
            pass
        print(f"Juego multijugador entre {nombre1} y {nombre2} finalizado")

def manejar_cliente(cliente, direccion):
    """Función principal para manejar la conexión inicial de un cliente"""
    try:
    
        datos_iniciales = cliente.recv(1024).decode()
        try:
    
            datos = json.loads(datos_iniciales)
            tipo_juego = datos.get("tipo", "servidor")
            
            if tipo_juego == "servidor":
                manejar_cliente_servidor(cliente, direccion)
            elif tipo_juego == "multijugador":
                nombre = datos.get("nombre", f"Jugador_{direccion[1]}")
                
                with lock_clientes:
             
                    if clientes_esperando:
                    
                        cliente_esperando, dir_esperando, nombre_esperando = clientes_esperando.pop(0)
                   
                        thread = threading.Thread(
                            target=manejar_juego_multijugador,
                            args=(cliente_esperando, dir_esperando, nombre_esperando, cliente, direccion, nombre)
                        )
                        thread.daemon = True
                        thread.start()
                    else:
    
                        clientes_esperando.append((cliente, direccion, nombre))
                        print(f"Cliente {nombre} en espera de un oponente...")
   
            
        except json.JSONDecodeError:

            manejar_cliente_servidor(cliente, direccion)
    except Exception as e:
        print(f"Error con el cliente {direccion}: {e}")
        cliente.close()

def iniciar_servidor():
    server_ip = input("Introduce la dirección IP para el servidor (vacío para todas las interfaces): ")
    if not server_ip:
        server_ip = '0.0.0.0' 
    

    puerto_str = input("Introduce el puerto del servidor (vacío para 65535): ")
    puerto = 65535  # Puerto por defecto
    if puerto_str and puerto_str.isdigit():
        puerto = int(puerto_str)
        
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        servidor.bind((server_ip, puerto))
        servidor.listen(5)
        
        host_name = socket.gethostname()
        ip_addresses = socket.gethostbyname_ex(host_name)[2]
        print(f"\nServidor iniciado en {server_ip}:{puerto}")
        if server_ip == '0.0.0.0':
            print("Direcciones IP disponibles para los clientes:")
            for ip in ip_addresses:
                print(f"  - {ip}:{puerto}")
        
        print("\nEsperando conexiones...")
        

        def mostrar_estado():
            while True:
                time.sleep(10) 
                with lock_clientes:
                    if clientes_esperando:
                        print(f"\nClientes esperando ({len(clientes_esperando)}):")
                        for i, (_, _, nombre) in enumerate(clientes_esperando):
                            print(f"  {i+1}. {nombre}")
        
        estado_thread = threading.Thread(target=mostrar_estado)
        estado_thread.daemon = True
        estado_thread.start()
        
        while True:
            cliente, direccion = servidor.accept()
            print(f"Conexión establecida con {direccion}")
            thread = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
            thread.daemon = True
            thread.start()
            
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    except Exception as e:
        print(f"\nError al iniciar el servidor: {e}")
    finally:
        try:
            servidor.close()
            print("Servidor cerrado correctamente.")
        except:
            pass

if __name__ == '__main__':
    iniciar_servidor()