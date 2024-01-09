from Params.params import Getkey
#fa la richiesta all'api di LLama
def DoRequest(Attivita):
    from llamaapi import LlamaAPI
    llama = LlamaAPI(Getkey())

    api_request_json = {
        "messages":[{"role": "user", "content": '''
        dato il seguente json e un input da utente che indica l'attività che ha svolto in giornata, ritorna solo il dato che potrebbe indicare meglio la sua attività,
        non argomentare, ritorna solo il dato tra #..#, il json è:{
        "data":{
            "TMG Text Translator":{
                "Progetto":"Y100-PRJ012",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I020",
                "Ts":""
            },
            "Cap6Maker":{
                "Progetto":"Y100-PRJ013",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I020",
                "Ts":""
            },
            "MesInterface":{
                "Progetto":"Y100-PRJ014",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I020",
                "Ts":""
            },
            "Pannelli Unified":{
                "Progetto":"Y100-PRJ015",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I020",
                "Ts":""
            },
            "Energy Meter":{
                "Progetto":"Y100-PRJ018",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I020",
                "Ts":""
            },
            "Assistenza Generica Cliente":{
                "Progetto":"9018",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I018",
                "Ts":""
            },
            "Corsi di formazione":{
                "Progetto":"9013",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I018",
                "Ts":""
            },
            "Supporto altri reparti (colleghi)":{
                "Progetto":"9015",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"",
                "Causa":"I015",
                "Ts":""
            },
            "Progetto Optix P&G Polonia":{
                "Progetto":"4071277",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"10",
                "Causa":"N013",
                "Ts":""
            },
            "Supervisione Generale":{
                "Progetto":"4055977",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"10",
                "Causa":"N013",
                "Ts":""
            },
            "Collaudo Supervisione Tecnobox":{
                "Progetto":"4068932",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"20",
                "Causa":"N006",
                "Ts":""
            },
            "Sviluppo SW Supervisione Tecnobox":{
                "Progetto":"4068932",
                "Ordine Destinatario":"",
                "Network":"",
                "Operazione":"10",
                "Causa":"N013",
                "Ts":""
            }
        }
    },

    l'input dell'utente è:''' + Attivita}],

        }

    response = llama.run(api_request_json)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(Getkey())