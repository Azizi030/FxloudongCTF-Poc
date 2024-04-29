import requests

url = 'http://139.9.194.250:998/api.php'

def get_code():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }
    response = requests.get(url, headers=headers)
    return response.text

def get_qx():
    if get_code() == '1':
        return True
    else:
        return False

