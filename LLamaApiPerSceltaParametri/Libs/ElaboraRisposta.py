from difflib import SequenceMatcher
#compara la risposta dell'api con il json e ritorna il valore corrispondente, si basa sul rapporto di similarità quindi non è perfetto ma funziona
def GetDataFromResponse(input_string, dictionary):
    input_string = input_string.split('"')[1]
    best_match = None
    best_ratio = 0

    for key, value in dictionary['data'].items():
        ratio = SequenceMatcher(None, input_string, key).ratio()
        
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = key

    if best_ratio > 0.7:
        #return the dict value of the best match
        return dictionary['data'][best_match]
    else:
        return None
