path_archivos = "/home/gallardo-uba/Documents/UBA/GuiasPracticas-ALGO1/Guias/Guia_8/archivos/"



def agregarProducto(inventario: dict[str:tuple[float,int]], nombre: str, precio: float, cantidad: int):
    if nombre in inventario:
        print("Ya esta en el inventario")
    else:
        inventario.update({nombre: [precio, cantidad]})
        
def actualizarStock(inventario: dict[str:tuple[float,int]], nombre: str, cantidad: int):
    if nombre in inventario:
        inventario.update({nombre: [inventario.get(nombre)[0], cantidad]})
    else:
        print("no existe el producto asi que no se puede actualizar")
        
def actualizarPrecios(inventario: dict[str:tuple[float,int]], nombre: str, precio: float):
    if nombre in inventario:
        inventario.update({nombre: [precio, inventario.get(nombre)[1]]})
    else:
        print("no existe el producto asi que no se puede actualizar")
        
def calcularValorInventario(inventario: dict[str:tuple[float,int]]) -> float:
    precio_total = 0
    
    for x in inventario.values():
        precio_total += x[0] * x[1]
    
    return precio_total