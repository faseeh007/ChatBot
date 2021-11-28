import requests
import json


class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "a642464e88msh49d25f5f2bedc8bp159e46jsn91cfe8734c45"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases'), result.get('deaths'), result.get('tests')

    def makeApiRequestForIndianStates(self):
        '''
        url = "https://covid19-data.p.rapidapi.com/india"
        headers = {
            'x-rapidapi-host': "covid19-data.p.rapidapi.com",
            'x-rapidapi-key': "a642464e88msh49d25f5f2bedc8bp159e46jsn91cfe8734c45"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        # result = js.get('list')
        return js
        '''
        url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewise"

        headers = {
            'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com",
            'x-rapidapi-key': "a642464e88msh49d25f5f2bedc8bp159e46jsn91cfe8734c45"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.status_code)
        js = json.loads(response.text)
        print("******", js)
        # result = js.get('list')
        return js
    #'''
        
    def makeApiWorldwide(self):

        url = "https://coronavirus-map.p.rapidapi.com/v1/summary/latest"

        headers = {
            'x-rapidapi-host': "coronavirus-map.p.rapidapi.com",
            'x-rapidapi-key': "a642464e88msh49d25f5f2bedc8bp159e46jsn91cfe8734c45"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js['data']['summary']

        return result
