import requests

r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=Spicy')

print(r.json()['meals'][0]['strMeal'])
# print(r.status_code)
# if name in r.json()['meals'][0]['strMeal']:
#     return True


class SearchByName:
    def __init__(self, name):
        self.r = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
        self.name = name

    def get_status_code(self):
        return self.r.status_code

    def check_if_correct_meal(self):
        if self.name in r.json()['meals'][0]['strMeal']:
            return True
        else:
            return False
