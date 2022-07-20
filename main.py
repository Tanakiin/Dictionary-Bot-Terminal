import requests


print('''----------------\nDictionary Bot\n----------------''')

x = 1
while x == 1:
    word = input("\nWhat word would you like to define?\n")

    if not word:
        print('Error ⚠\nNo input given\n')
        continue
    else:
        pass

    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = response.json()

    if isinstance(data, list) == False:
        print("Error ⚠\nWord not found\n")
        continue
    else:
        wdata = data[0]
        phonetics = "N/A"
        for i in wdata['phonetics']:
            try:
                if i['text']:
                    phonetics = i['text']
            except:
                pass
        audio = ""
        for i in wdata['phonetics']:
            try:
                if i['audio']:
                    audio = i['audio']
            except:
                pass
        
        out_def = {}
        meanings = len(wdata['meanings'])
        for k in range(meanings):
            meaning = wdata['meanings'][k]
            definitions = "\n- ".join(["", *[i['definition'] for i in meaning['definitions']]])
            synonyms = ", ".join(wdata['meanings'][k]['synonyms'])
            if synonyms == "":
                out_def[meaning['partOfSpeech']] = [definitions]
            else:
                out_def[meaning['partOfSpeech']] = [definitions, synonyms]
        print('\n')

        for i in out_def:
            if len(out_def[i]) > 1:
                print(i.capitalize()+"\n----------\n")
                print("Definition:\n"+out_def[i][0]+"\n")
                print("Synonyms: "+out_def[i][1]+"\n")
            else:
                print(i.capitalize()+"\n----------\n")
                print("Definition:\n"+out_def[i][0]+"\n")

        while True:  
            prompt = input("\nWould you like to continue? (Y/N)\n").lower()
            if prompt == 'n':
                x = 0
                break
            elif prompt == 'y':
                break
            else:
                print('Error ⚠\nNot a Valid Option\n')
                continue
          
print('\nThank you for using DictionaryBot!')
