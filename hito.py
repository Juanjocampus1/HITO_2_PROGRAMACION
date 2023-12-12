import random
import time
from colorama import Fore, Style, init
from pyfiglet import Figlet
import matplotlib.pyplot as plt

init(autoreset=True)

"""
{Fore.RED}
{Fore.BLUE}
{Fore.GREEN}
{Fore.MAGENTA}
{Fore.CYAN}
{Fore.YELLOW}

{Style.RESET_ALL}
"""

class GeneradorArray:
    @staticmethod
    def generar_array_aleatorio(longitud):
        if longitud <= 0:
            raise ValueError(f"{Fore.YELLOW}La longitud debe ser un número positivo.{Style.RESET_ALL}")
        return random.sample(range(1, longitud * 2), longitud)

    @staticmethod
    def mostrar_array(array):
        print(f"{Fore.MAGENTA}Array: {array}{Style.RESET_ALL}")

class Operaciones:
    @staticmethod
    def ordenacion_burbuja(array):
        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    print(f"{Fore.MAGENTA}Paso {i * (n - 1) + j + 1}: {array}{Style.RESET_ALL}")

    @staticmethod
    def ordenacion_insercion(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
            print(f"{Fore.MAGENTA}Paso {i}: {array}{Style.RESET_ALL}")

    @staticmethod
    def ordenacion_shell(array):
        n = len(array)
        brecha = n // 2
        while brecha > 0:
            for i in range(brecha, n):
                temp = array[i]
                j = i
                while j >= brecha and array[j - brecha] > temp:
                    array[j] = array[j - brecha]
                    j -= brecha
                array[j] = temp
            brecha //= 2
            print(f"{Fore.MAGENTA}Paso: {array}{Style.RESET_ALL}")


    @staticmethod
    def ordenacion_seleccion(array):
        for i in range(len(array)):
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            print(f"{Fore.MAGENTA}Paso {i}: {array}{Style.RESET_ALL}")


    @staticmethod
    def busqueda_binaria(array, elemento):
        inicio = 0
        fin = len(array) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            if array[medio] == elemento:
                return medio
            elif elemento > array[medio]:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None

    @staticmethod
    def ejecutar_comparativa(array):
        tiempos = {'Burbuja': 0, 'Insercion': 0, 'Shell': 0, 'Seleccion': 0}

        # Ordenación Burbuja
        inicio = time.time()
        Operaciones.ordenacion_burbuja(array.copy())
        tiempos['Burbuja'] = time.time() - inicio

        # Ordenación Inserción
        inicio = time.time()
        Operaciones.ordenacion_insercion(array.copy())
        tiempos['Insercion'] = time.time() - inicio

        # Ordenación Shell
        inicio = time.time()
        Operaciones.ordenacion_shell(array.copy())
        tiempos['Shell'] = time.time() - inicio

        # Ordenación Selección
        inicio = time.time()
        Operaciones.ordenacion_seleccion(array.copy())
        tiempos['Seleccion'] = time.time() - inicio

        return tiempos


def print_ascii_title(title_text):
    fig = Figlet()
    titulo = fig.renderText(title_text)

    colored_title = ""
    for line in titulo.split('\n'):
        colored_title += f"{Fore.YELLOW}{line}{Style.RESET_ALL}\n"

    print(colored_title)

def mostrar_grafico(tiempos):
    metodos = list(tiempos.keys())
    valores = list(tiempos.values())

    plt.figure(figsize=(10, 6))
    plt.bar(metodos, valores, color=['red', 'blue', 'green', 'purple'])

    plt.xlabel('Método de Ordenación')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparativa de Tiempos de Ejecución')
    plt.show()

def main():
    global inicio, array_ordenado
    print_ascii_title("ORDENAMIENTO")

    generador = GeneradorArray()
    array_aleatorio = None

    while True:
        if array_aleatorio is None:
            print(f"{Fore.LIGHTGREEN_EX}           =========={Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}           ||{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}MENU{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}           ========== \n{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}================================={Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTRED_EX}1. Generar Array Aleatorio. {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}2. Salir.                   {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}================================={Style.RESET_ALL}")
            opcion = input(f"{Fore.LIGHTCYAN_EX}\n~$ {Style.RESET_ALL}")

            if opcion == "1":
                longitud = int(input(f"{Fore.LIGHTMAGENTA_EX}Ingrese la longitud del array: {Style.RESET_ALL}"))
                array_aleatorio = generador.generar_array_aleatorio(longitud)
                print(f"{Fore.MAGENTA}Array Original ({longitud} elementos): {Style.RESET_ALL}", array_aleatorio)
            elif opcion == "2":
                print(f"{Fore.LIGHTRED_EX}Saliendo del programa{Style.RESET_ALL}")
                break
        else:
            print(f"{Fore.LIGHTGREEN_EX}           =========={Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}           ||{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}MENU{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}           ========== \n{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}================================={Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}1. Ordenación Burbuja.{Style.RESET_ALL}      {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTRED_EX}2. Ordenación Inserción.{Style.RESET_ALL}    {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}3. Ordenación Shell.{Style.RESET_ALL}        {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}4. Ordenación Selección.{Style.RESET_ALL}    {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}5. Búsqueda Binaria.{Style.RESET_ALL}        {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}6. prueba de rendimiento.{Style.RESET_ALL}   {Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL} {Fore.LIGHTMAGENTA_EX}7. Volver al Menú Principal.{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}||{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}================================={Style.RESET_ALL}")
            opcion = input(f"{Fore.LIGHTCYAN_EX}\n~$ {Style.RESET_ALL}")

            if opcion in {"1", "2", "3", "4", "5", "6"}:
                array_copia = array_aleatorio.copy()

                if opcion == "7":
                    array_aleatorio = None
                    continue

                if opcion == "1":
                    print(f"{Fore.MAGENTA}Ordenación Burbuja:{Style.RESET_ALL}")
                    inicio = time.time()
                    Operaciones.ordenacion_burbuja(array_copia)
                    array_ordenado = array_copia.copy()
                elif opcion == "2":
                    print(f"{Fore.MAGENTA}Ordenación Inserción:{Style.RESET_ALL}")
                    inicio = time.time()
                    Operaciones.ordenacion_insercion(array_copia)
                    array_ordenado = array_copia.copy()
                elif opcion == "3":
                    print(f"{Fore.MAGENTA}Ordenación Shell:{Style.RESET_ALL}")
                    inicio = time.time()
                    Operaciones.ordenacion_shell(array_copia)
                    array_ordenado = array_copia.copy()
                elif opcion == "4":
                    print(f"{Fore.MAGENTA}Ordención Selección:{Style.RESET_ALL}")
                    inicio = time.time()
                    Operaciones.ordenacion_seleccion(array_copia)
                    array_ordenado = array_copia.copy()

                elif opcion == "5":
                    if array_ordenado is None:
                        print(f"{Fore.YELLOW}Primero debes ordenar el array.{Style.RESET_ALL}")
                        continue

                    elemento_buscar = int(input(f"{Fore.LIGHTMAGENTA_EX}Ingrese el elemento a buscar: {Style.RESET_ALL}"))
                    inicio_busqueda = time.time()
                    resultado_binaria = Operaciones.busqueda_binaria(array_ordenado, elemento_buscar)
                    fin_busqueda = time.time()

                    if resultado_binaria is None:
                        print(f"{Fore.YELLOW}El elemento {elemento_buscar} no se encuentra en el vector.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.BLUE}El elemento {elemento_buscar} se encuentra en la posición {resultado_binaria} del array ordenado.{Style.RESET_ALL}")

                    tiempo_busqueda = fin_busqueda - inicio_busqueda
                    print(f"{Fore.LIGHTMAGENTA_EX}Tiempo de Ejecución (Búsqueda Binaria): {tiempo_busqueda} segundos{Style.RESET_ALL}")

                elif opcion == "6":
                    if array_aleatorio is None:
                        print(f"{Fore.YELLOW}Primero debes generar un array.{Style.RESET_ALL}")
                        continue

                    print(f"{Fore.LIGHTGREEN_EX}Ejecutando comparativa de tiempos...{Style.RESET_ALL}")
                    tiempos = Operaciones.ejecutar_comparativa(array_aleatorio)
                    mostrar_grafico(tiempos)

            elif opcion == "7":
                print(f"{Fore.LIGHTYELLOW_EX}Saliendo al Menú Principal.{Style.RESET_ALL}")
                array_aleatorio = None

            else:
                print(f"{Fore.LIGHTRED_EX}Opción no válida. Por favor, elige una opción válida.{Style.RESET_ALL}")