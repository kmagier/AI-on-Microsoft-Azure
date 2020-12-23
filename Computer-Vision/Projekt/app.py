import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import string

headers = {
    'Content-Type': 'application/json',
    'Prediction-Key': '<prediction-key-here>',
}

body = "{'Url' : '" + 'https://static.fajnyzwierzak.pl/media/uploads/media_image/auto/entry-content/701/desktop/nowofunland.jpg' + "' }"

try:
    conn = http.client.HTTPSConnection('westeurope.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v3.0/Prediction/<model-id>/classify/iterations/<iteration>/url", body, headers)
    response = conn.getresponse()
    data = response.read()
    data_string = data.decode('utf-8')
    json_data=json.loads(data_string)
    #print(json_data)
    if json_data:
        for i in range(0,5):
            value = json_data['predictions'][i]['probability']
            race = json_data['predictions'][i]['tagName']
            print(f'Race - {race.capitalize()} with probability {value*100}%')
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    