def verificar_edad(edad, mayor_edad):
    resultado_edad = edad >= mayor_edad
    return resultado_edad

if __name__ == "__main__":
    resultado = verificar_edad(22, 18)
    print("Es mayor de edad:", resultado)