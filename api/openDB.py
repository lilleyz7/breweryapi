import requests

class OpenDB():
    base_url = 'https://api.openbrewerydb.org/v1/breweries'

    def get_brewery_by_id(self, id):
        url = self.base_url + f'/{id}'

        try:
            response = requests.get(url)
            json = response.json()
            data = {
                'brew_id': json['id'],
                'name': json['name'],
                'brewery_type': json['brewery_type'],
                'street': json['street'],
                'city': json['city'],
                'state': json['state'],
                'phone': json['phone'],
                'website_url': json['website_url'],
            }
            return data
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
        url = self.base_url + f'?by_city={city}&per_page=50'

        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            return str(e)

    def get_random_brewery(self):
        pass