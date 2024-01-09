import json
from Libs.Request import DoRequest
from Libs.ElaboraRisposta import GetDataFromResponse

Attivita = "Fatto niente"
Response = DoRequest(Attivita)

with open('Data\RiguardoLeOre\Codici Progetti SAP.json') as json_file:
    data = json.load(json_file)

print(GetDataFromResponse(Response, data))

(GetDataFromResponse(Response, data))