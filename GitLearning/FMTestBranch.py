import http.client

conn = http.client.HTTPSConnection("collectionapi.metmuseum.org")
payload = ''
headers = {
  'Cookie': 'incap_ses_1723_1662004=2f/hctJu+gdpDWkovFPpF6r7gGgAAAAATqX9V6nqSUNeEoGSyt9p0g==; visid_incap_1662004=NUsu9M5dQe6dQglJ7tSY5REjgGgAAAAAQUIPAAAAAACHApHYhaBxewyAOOr7yc+A'
}
conn.request("GET", "/public/collection/v1/departments", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))