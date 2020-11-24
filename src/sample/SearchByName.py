import requests


class SearchByName:
    def __init__(self, name):
        self.r = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
        self.name = name

    def get_status_code(self):
        return self.r.status_code

    def check_if_correct_meal(self):
        if self.name in self.r.json()['meals'][0]['strMeal']:
            return True
        else:
            return False

