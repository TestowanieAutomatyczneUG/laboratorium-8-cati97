import requests

r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata')

print(r.json())
# print(r.status_code)


class SearchByName:
    def __init__(self, name):
        self.r = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')

    def get_status_code(self):
        return self.r.status_code
