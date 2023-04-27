import requests

def get_cat_facts():
    r = requests.get('https://catfact.ninja/fact?max_length=140')
    data = r.json()
    return data['fact']