import requests

def test_007_obtener_resultados_busqueda_con_miracle(): 

    url = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=miracle"

    
    headers = {
    'Cookie': 'incap_ses_1725_1662004=zL9FT4zcgjvnDlMet27wF2mwgmgAAAAA05JkvHdN7Ppke/vk05vFpA==; visid_incap_1662004=mlhY9ZsMR4+wXnQr9Hdn9WmwgmgAAAAAQUIPAAAAAAB94TtuPC4jPof+On9wLYe5'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)