#Programa de registro de fumigaciones
#Inicializar contadores
total_hogares = 12
roedores = 0
insectos = 0
hongos = 0
hogares_procesados = 0

print("=== Sistema de Registro de Fumigaciones ===")
print("\nTipos de fumigación disponibles:")
print("1. Roedores - Para el control de ratas y ratones")
print("2. Insectos - Para el control de cucarachas, hormigas y otros insectos")
print("3. Hongos - Para el control de moho y hongos")

while hogares_procesados < total_hogares:
    print(f"\nHogar #{hogares_procesados + 1}")

    while True:
        tipo_fumigacion = input("Ingrese el tipo de fumigación (1-3): ")
        if tipo_fumigacion in ['1', '2', '3']:
            break
        print("Opción no válida. Por favor ingrese 1, 2 o 3.")

    if tipo_fumigacion == '1':
        roedores += 1
        print("Se registró fumigación contra roedores")
    elif tipo_fumigacion == '2':
        insectos += 1
        print("Se registró fumigación contra insectos")
    else:
        hongos += 1
        print("Se registró fumigación contra hongos")

    hogares_procesados += 1
