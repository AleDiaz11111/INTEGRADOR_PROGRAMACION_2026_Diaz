import Menu
import Gestion_de_Stock
import subprocess
def main():
    Gestion_de_Stock.inicializar()
    opcion = Menu.B_Menu()
    if opcion == 1:
        Gestion_de_Stock.cargar_stock()
    elif opcion == 2:
        Gestion_de_Stock.mostrar_stock()
    elif opcion == 3:
        opcion_contar = input("que producto desea contar? ")
        Gestion_de_Stock.contar(opcion_contar)
        
        # pedir la categoría y llamar a Gestion_stock.contar(...)
        ...

if __name__ == "__main__":
    subprocess.run("cls",shell=True)
    main()