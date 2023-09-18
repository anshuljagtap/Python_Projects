from typing import Final
import requests

API_KEY: Final[str] = '6cbe41d8e11b42919b0b9266bfb045f9a5ed2'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shotern_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortlink']
            print('Link:', short_link)

        else:
            print('Error status ->',url_data['status'])


def main():
    input_link = str(input('Enter a link:'))
    shotern_link(input_link)

if __name__ == '__main__':
    main()