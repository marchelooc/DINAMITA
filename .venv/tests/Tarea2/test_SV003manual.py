#ID: SV003

#Título: Agregar un item a un patch inexistente para generar un error 404.

#Descripción: El usuario debe obtener intentar agregar un objeto con un patch inexistente usando POST.

#Precondiciones:
#Postman debe estar instalado.

#Ambiente:
# URL: https://api.restful-api.dev/

#Pasos:
#1	Abrir Postman.
#2	Seleccionar POST
#3	En el campo URL, ingresar: https://api.restful-api.dev/objectss (el patch objects esta mal escrito intencionalmente con doble s al final "objectss")
#4  Llenar el body del request.
#5	Hacer clic en "Send".
#6	Verificar que el resultado sea un estado 404.

#Resultado esperado:
#La respuesta de la API al request muestra que la direccion no puede ser encontrada.

#Prioridad: 5 Baja