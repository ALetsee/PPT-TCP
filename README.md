
# Cliente y Servidor de Piedra, Papel o Tijera en TCP

Este proyecto implementa un cliente y un servidor en la terminal para un juego de Piedra, Papel o Tijera que funciona en red. Permite a los jugadores conectarse a un servidor para jugar contra la máquina o contra otros jugadores en tiempo real.

## Características del Cliente

- **Interfaz de usuario ASCII**: Utiliza gráficos ASCII para crear una experiencia visual agradable en la consola.
- **Menús interactivos**: Proporciona menús claros y fáciles de usar para navegar entre las diferentes opciones de juego.
- **Dos modos de juego**:
  - **Contra el servidor**: Juega directamente contra la lógica del servidor.
  - **Multijugador**: Permite jugar contra otros clientes conectados al mismo servidor.
- **Personalización de la conexión**: Permite configurar la dirección IP y el puerto del servidor.
- **Partidas personalizables**: Los jugadores pueden elegir el número de rondas para cada partida.
- **Efectos visuales**: Incluye pantallas de espera animadas y efectos visuales para los resultados.

### Funcionamiento del Cliente

#### Conexión al servidor

El cliente establece una conexión TCP con el servidor en la dirección IP y puerto especificados. Si la conexión falla, muestra un mensaje de error adecuado.

#### Modo contra el servidor

1. El cliente envía un mensaje indicando que quiere jugar contra el servidor.
2. Se solicita al jugador su nombre.
3. El servidor pregunta por el número de rondas a jugar.
4. En cada ronda:
   - El cliente muestra un menú para elegir entre piedra (1), papel (2) o tijera (3).
   - El servidor recibe la jugada y determina el resultado.
   - Se muestra el resultado de la ronda con gráficos ASCII.
5. Al final de todas las rondas, se muestra el resultado general de la partida.

#### Modo multijugador

1. El cliente envía un mensaje indicando que quiere jugar en modo multijugador.
2. El cliente espera a ser emparejado con otro jugador (se puede cancelar la espera).
3. Una vez emparejado, uno de los jugadores elige el número de rondas.
4. El juego procede de manera similar al modo contra el servidor.
5. Se añaden pantallas de espera mientras el oponente hace su jugada.

## Características del Servidor

- **Gestión de conexiones**: Manejo de conexiones TCP con los clientes y tratamiento de errores.
- **Modo contra el servidor**: Permite a los clientes jugar contra la lógica del servidor.
- **Modo multijugador**: Empareja a los clientes para jugar entre sí.
- **Monitor de estado**: Muestra el estado de los clientes en espera y las partidas en curso.

### Funcionamiento del Servidor

#### Conexión de clientes

El servidor acepta conexiones de clientes en la dirección IP y puerto especificados. Permite a los clientes elegir entre jugar contra el servidor o en modo multijugador.

#### Modo contra el servidor

1. El servidor solicita el nombre del jugador y el número de rondas a jugar.
2. En cada ronda:
   - El servidor recibe la jugada del cliente y genera su propia jugada aleatoria.
   - Se determina el ganador de la ronda y se muestra el resultado con gráficos ASCII.
3. Al final de todas las rondas, se muestra el resultado general de la partida.

#### Modo multijugador

1. El servidor empareja a los clientes en espera.
2. Uno de los jugadores elige el número de rondas.
3. En cada ronda:
   - Ambos jugadores envían sus jugadas al servidor.
   - Se determina el ganador de la ronda y se muestra el resultado con gráficos ASCII.
4. Al final de todas las rondas, se muestra el resultado general de la partida.

## Requisitos

- **Python 3.x**
- **Módulos estándar**: `socket`, `os`, `threading`, `time`, `json`

## Uso

1. Asegúrate de que el servidor esté en funcionamiento.
2. Ejecuta el cliente: `python cliente.py`
3. Configura la IP y puerto del servidor si es necesario.
4. Selecciona el modo de juego y ¡diviértete!

Resultado esperado:

https://github.com/user-attachments/assets/8383f2c8-15e9-438d-a399-d455c9fa6dd0
