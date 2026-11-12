stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'limpieza':[]}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [],'limpieza':[]}

def inicializar():
     for categoria in stock_productos:
         stock_productos[categoria] = []
     for categoria in stock_cantidades:
         stock_cantidades[categoria] = []
def cargar_stock():
    categoria = input("Ingrese la categoría (enlatados, frutas, congelados, limpieza): ")
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    stock_productos[categoria].append(producto)
    stock_cantidades[categoria].append(cantidad)
def mostrar_stock():
     for categoria in stock_productos:
        print(categoria)
        for i in range(len(stock_productos[categoria])):
            print(stock_productos[categoria][i], ":", stock_cantidades[categoria][i])
def contar(opcion_contar):
     print("Cantidad de productos:", len(opcion_contar))
     print("Suma de las cantidades:", sum(opcion_contar))