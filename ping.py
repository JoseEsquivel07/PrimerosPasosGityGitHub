import subprocess
import threading
import time
def ping(host):
    while True:
        # Ejecutar el comando de ping
        process = subprocess.Popen(['ping', '-n', '1', '-w', '1000', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Esperar a que termine el comando de ping
        process.wait()

        # Obtener el código de salida
        return_code = process.returncode

        # Comprobar si el host está "up" o "down" basándose en el código de salida
        if return_code == 0:
            print(f"{host} está UP")
        else:
            print(f"{host} está DOWN")

        # Esperar 3 segundos antes de la siguiente ejecución
        time.sleep(30)
def send_ping_to_ips(ips):
    threads = []

    # Crear un hilo para cada IP
    for ip in ips:
        thread = threading.Thread(target=ping, args=(ip,))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()


# Ejemplo de uso
ips = ['10.69.98.196', '10.92.23.70', '10.107.25.76', '10.69.98.212', '10.116.232.140']
send_ping_to_ips(ips)