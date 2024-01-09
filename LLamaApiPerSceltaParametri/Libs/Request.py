from Params.params import Getkey
import json
#fa la richiesta all'api di LLama
def DoRequest(Attivita):
    from llamaapi import LlamaAPI
    llama = LlamaAPI(Getkey())

    #read the data from the json file
    with open("json.json") as json_file:
        data = json.load(json_file)

    text = '''dato il seguente json e un input da utente che indica l'attività che ha svolto in giornata, ritorna solo il dato che potrebbe indicare meglio la sua attività,
        non argomentare, ritorna solo il dato tra #..#, il json è:''' + str(data) + '''l'input dell'utente è:''' + Attivita

    api_request_json = {
        "messages":[{"role": "user", "content": text}],
        }

    response = llama.run(api_request_json)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(Getkey())