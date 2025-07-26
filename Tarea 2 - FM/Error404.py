import pytest
import requests

# ID: 001

# Prioridad: Media
# Categoria: Smoke

@pytest.mark.smoke
@pytest.mark.negative
# Titulo: Obtener los departamentos
def Obtener_los_departamentos():

  # Descripción: El usuario debe obtener todos los departamentos
  # Ambiente: Acceso al metmuseum.com
  url = "https://collectionapi.metmuseum.org/public/collection/v1/department"

  # Pasos
  # 1 Seleccionar el método GET
  # 2 Llamar a los departamentos
  headers = {
    'Cookie': 'incap_ses_1723_1662004=uYagdooFDnG/SjQrvFPpFxoPhGgAAAAAPYkCp9LRotFr2nlI3vc1fA==; visid_incap_1662004=NUsu9M5dQe6dQglJ7tSY5REjgGgAAAAAQUIPAAAAAACHApHYhaBxewyAOOr7yc+A'
  }

  # 3 Click en el botón Send
  response = requests.request("GET", url, headers=headers, data=payload)

  # 4 Verificar que el estado correcto sea 404
  assert response.status_code == 404

  print(response.text)
