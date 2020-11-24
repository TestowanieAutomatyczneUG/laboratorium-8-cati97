import requests

class MealDetailsById:
    def __init__(self, id):
        self.r = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
        self.id = id

    def get_status_code(self):
        return self.r.status_code

    def check_if_correct_meal(self):
        if str(self.id) == self.r.json()['meals'][0]['idMeal']:
            return True
        else:
            return False