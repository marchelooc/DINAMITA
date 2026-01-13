#ID: SV002

#Título: Agregar un item sin body, para generar un error 400.

#Descripción: El usuario debe obtener intentar agregar un objeto sin body en el POST.

#Precondiciones:
#Postman debe estar instalado.

#Ambiente:
# URL: https://api.restful-api.dev/

#Pasos:
#1	Abrir Postman.
#2	Seleccionar POST
#3	En el campo URL, ingresar: https://api.restful-api.dev/objects
#4  En el body del request dejarlo en blanco.
#5	Hacer clic en "Send".
#6	Verificar que el resultado sea un estado 400.

#Resultado esperado:
#La respuesta de la API al request muestra que los valores para añadir no pueden ser encontrados.

#Prioridad: 3 Media