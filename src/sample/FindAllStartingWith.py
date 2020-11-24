import requests


class FindAllStartingWith:
    def __init__(self, start_with):
        self.r = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={start_with}')
        self.start_with = start_with

    def get_status_code(self):
        return self.r.status_code

    def get_list_of_names(self):
        meals_names = [i['strMeal'] for i in self.r.json()['meals']]
        return meals_names
