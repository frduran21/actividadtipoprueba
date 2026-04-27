import os 
os.system("cls")

DESCUETNO_NINO = 0.50
DESCUENTO_ADULTO_MAYOR = 0.30
DESCUENTO_MARTES = 0.20
IVA = 0.10


try:  
    while True:
        nombre_usuario = str(input("INGRESE NOMBRE :")).lower()
        if len(nombre_usuario) >0:
            print(f"hola: {nombre_usuario}")
            break
    while True:
        edad_usuario = int(input("INGRESE EDAD :"))
        if 0<edad_usuario <100:
            break      
    while True: 
        cantidad_entradas = int(input("INGRESE CANITDAD DE ENTRADAS :"))
        cantidad_entradas >0
        break
        
    dia_funcion = str(input("INGRESE DIA DE LA FUNCION: ")).lower()
    if dia_funcion == "lunes":
            
    
    
            
    
except:
    print("error ")

