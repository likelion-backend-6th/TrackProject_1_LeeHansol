import requests

username = 'admin'
password = '1234'

base_url = 'http://127.0.0.1:8000/api/'
# retrieve all courses
r = requests.get(f'{base_url}books/')
items = r.json()

available_items = ', '.join([item['title'] for item in items])
print(f'Available items: {available_items}')

for item in items:
    item_id = item['id']
    item_title = item['title']

    r = requests.post(f'{base_url}books/{item_id}/rental/',
                      auth=(username, password))

    if r.status_code == 200:
        print(f'Successfully rented {item_title}')