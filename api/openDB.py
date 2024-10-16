import requests

class OpenDB():
    base_url = 'https://api.openbrewerydb.org/v1/breweries'

    def get_brewery_by_id(self, id):
        url = self.base_url + f'/{id}'

        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            return str(e)

    def get_brewery_by_name(self, name):
        url = self.base_url + f'?by_name={name}&per_page=10'  

        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            return str(e)

    def get_breweries_by_city(self, city):
        url = self.base_url + f'?by_city={city}&per_page=5'

        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            return str(e)

    def get_random_brewery(self):
        pass