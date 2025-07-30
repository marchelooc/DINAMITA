import requests 
import pytest
import jsonsch
import pytest
import requests
import jsonschema


@pytest.mark.smoke
def testObtenerListaDeTutoresActivosCorrectamente():
    url = "https://backend.clubinfinitychess.com/"
    endpoint = "agregarCurso"
    lista_url = url + endpoint
    payload = {
        "CODCURSO": "2027Curso",
        "CURSO": "Curso"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(lista_url, json=payload, headers=headers)
    assert response.status_code == 201
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "CODCURSO": {"type": "string"},
            "CURSO": {"type": "string"},
            "ESTADO": {"type": "string"}
        },
        "required": ["CODCURSO", "CURSO", "ESTADO"]
    }
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema no coincide: {err}")