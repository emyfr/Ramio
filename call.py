import requests


if __name__ == '__main__':
    r = requests.get('https://api.py.github.com/events')
    print(r.json)

