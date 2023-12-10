import psutil
import wmi

def obtener_porcentaje_uso_cpu():
    uso_cpu = psutil.cpu_percent(interval=1)

    print(f"Uso del CPU: {uso_cpu}%")

    if uso_cpu > 40:
            print("¡Alerta! El uso del CPU supera el 40%.")
    
    return uso_cpu

def obtener_porcentaje_uso_memoria():
    porcentaje_uso_memoria = psutil.virtual_memory().percent

    print(f"Porcentaje de uso de la memoria: {porcentaje_uso_memoria}%")
    
    return porcentaje_uso_memoria

def mostrar_rendimiento_red():
    interfaces_red = psutil.net_io_counters(pernic=True)

    print("Rendimiento de la red:")
    for interfaz, datos in interfaces_red.items():
        print(f"  Interfaz: {interfaz}")
        print(f"    Bytes enviados: {datos.bytes_sent / (1024 ** 2):.2f} MB")
        print(f"    Bytes recibidos: {datos.bytes_recv / (1024 ** 2):.2f} MB")
        print(f"    Paquetes enviados: {datos.packets_sent}")
        print(f"    Paquetes recibidos: {datos.packets_recv}")
        print()  

def mostrar_temperatura_cpu_windows():
    try:
        conexion_wmi = wmi.WMI()

        temperaturas_cpu = conexion_wmi.Win32_TemperatureProbe()

        if not temperaturas_cpu:
            print("No se pudo obtener información de temperatura del CPU.")
            return

        print("Temperaturas del CPU:")
        for temperatura in temperaturas_cpu:
            print(f"  Temperatura: {temperatura.CurrentReading}°C")
            print(f"  Límite superior: {temperatura.MaxReadable}°C")
            print(f"  Límite inferior: {temperatura.MinReadable}°C")
            print()

    except Exception as e:
        print(f"Error al obtener la temperatura del CPU en Windows: {e}")


if __name__ == "__main__":
    obtener_porcentaje_uso_cpu()

    obtener_porcentaje_uso_memoria()

    mostrar_rendimiento_red()

    mostrar_temperatura_cpu_windows()