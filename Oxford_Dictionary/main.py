import requests

app_id = 'Replace with your app_id'
app_key = 'Replace with your app_key'
headers = {'app_id': app_id, 'app_key': app_key}
language = 'en'
word_id = 'happy'

#  finds the available words
url_name = 'https://od-api.oxforddictionaries.com:443/api/v1/search/' + language + '?q=' + word_id.lower() + '&prefix=false'
r_name = requests.get(url_name, headers=headers)

if r_name:
    name_json = r_name.json()
    name_list = []
    for name in name_json['results']:
        name_list.append(name['word'])
    print("You searched for the word : " + word_id)
    print("___________________________________________________________________\n")
    print("Following are the list of words available for the search : " + word_id)
    print("_____________________________________________________________________")
    for i in name_list:
        print(i)
else:
    print("No matches found.. \n Please try again with different word")


# finds the meaning of the word
url_mean = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
r_mean = requests.get(url_mean, headers=headers)

if r_mean:
    mean_json = r_mean.json()
    mean_list = []

    for result in mean_json['results']:
        for lexicalEntry in result['lexicalEntries']:
            for entry in lexicalEntry['entries']:
                for sense in entry['senses']:
                    mean_list.append(sense['definitions'][0])

    print("___________________________________________________________________\n")
    print("Following are the list of meanings available for the search : " + word_id)
    print("_____________________________________________________________________")
    for i in mean_list:
        print(i)
else:
    print("No matches found.. \n Please try again with different word")
