import psutil
import time

def monitorear_cpu():
    while True:
        # Obtener el porcentaje de uso del CPU
        uso_cpu = psutil.cpu_percent(interval=1)

        # Imprimir el porcentaje de uso del CPU
        print(f"Uso del CPU: {uso_cpu}%")

        # Verificar si el uso del CPU supera el 40%
        if uso_cpu > 40:
            # Aquí puedes enviar un mensaje, por ejemplo, imprimir en la consola
            print("¡Alerta! El uso del CPU supera el 40%.")

        # Esperar un breve periodo antes de la siguiente lectura
        time.sleep(1)

if __name__ == "__main__":
    monitorear_cpu()
