""" 
ID: SV001

Título: Obtener una lista de IDs de los objetos del departamento 1.

Descripción: El usuario debe obtener la cantidad y una lista de IDs del departamento 1.

Precondiciones:
Ninguna

Ambiente:
página web: https://metmuseum.github.io/

Pasos:
1 Abrir Postman.
2 Crear un nuevo request con método GET.
3 En el campo URL, ingresar: https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1
4 Hacer clic en "Send".
5 Verificar que el srvidor devuelva un estado 200.
6 Verificar que la respuesta sea un entero y un arreglo.

Resultado esperado:
La respuesta de la API al request muestra los siguientes valores:
•	“total”: 18966.
•	“objectIDs”: [505, 506…] 

Post condicion:
Ninguna

Prioridad: Alta

Categoria: Smoke

"""
