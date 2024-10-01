nombre = "Alonso"
apellido = "Ojeda"

saludo = "Hola "+ nombre + " " + apellido + ", Como estas? "
print(saludo)

respuesta = "Bien y tu?"
print(respuesta)

def suma(*num):
    return sum(num)

print(suma(2,5))