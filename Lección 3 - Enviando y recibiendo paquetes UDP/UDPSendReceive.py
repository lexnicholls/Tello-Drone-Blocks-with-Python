# Este script es un ejemplo que demuestra como enviar/recibir comandos desde/hacia Tello
# Este script hace parte del curso de programación de drones Tello
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Importar los modulos para el socket y el tiempo
import socket
import time

# IP y puerto de Tello
tello_address = ('192.168.10.1', 8889)

# Crear una conexión UDP a la cual le enviaremos el comando
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Seremos explicitos y asignaremos un puerto en nuestra maquina al cual Tello enviará los mensajes
sock.bind(('', 9000))

# Función para enviar mensajes a Tello
def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Enviando mensaje: " + message)
  except Exception as e:
    print("Error enviando: " + str(e))

# Función que escuchará los mensajes de Tello y los imprimirá en la pantalla
def receive():
  try:
    response, ip_address = sock.recvfrom(128)
    print("Mensaje recibido: " + response.decode(encoding='utf-8') + " desde Tello con dirección IP: " + str(ip_address))
  except Exception as e:
    print("Error recibiendo: " + str(e))


# Enviar a Tello en el modo de comandos
send("command")

# Recibir una respuesta de Tello
receive()

# Retrasar 3 segundos antes de enviar el siguiente comando
time.sleep(3)

# Preguntar a Tello por el estado de la bateria
send("battery?")

# Recibir la respuesta de la bateria de Tello
receive()

# Cerrar el socket UDP
sock.close()