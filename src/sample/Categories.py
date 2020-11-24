import requests

class Categories:
    def __init__(self):
        self.r = requests.get(f'https://www.themealdb.com/api/json/v1/1/categories.php')

    def get_status_code(self):
        return self.r.status_code

    def get_len_of_categories(self):
        return len(self.r.json()["categories"])
