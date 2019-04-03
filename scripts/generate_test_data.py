import json
import os

import requests


DEFAULT_BASE_URL = 'https://testscoring.herokuapp.com'


def login(base_url, username, password):
    url = f'{base_url}/api/auth/'
    data = {
        'username': username,
        'password': password,
    }

    response = requests.post(url, data)
    response.raise_for_status()

    return response.json()['token']


def get_test(base_url, token, test_id):
    url = f'{base_url}/api/testing/v1/tests/{test_id}/'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def get_scores(base_url, token, test_id):
    url = f'{base_url}/api/testing/v1/tests/{test_id}/scores/'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def main():
    username = os.getenv('USERNAME')
    if not username:
        print("Please set USERNAME env variable")
        return -1
    password = os.getenv('PASSWORD')
    if not password:
        print("Please set PASSWORD env variable")
        return -1

    test_id = os.getenv('TESTID')
    if not test_id:
        print("Please set TESTID env variable")
        return -1

    base_url = os.getenv('BASE_URL', DEFAULT_BASE_URL)

    token = login(base_url, username, password)
    test = get_test(base_url, token, test_id)
    scores = get_scores(base_url, token, test_id)

    with open(f'test_{test_id}_test.py', 'w') as outfile:
        outfile.write("test = ")
        json.dump(test, outfile)

    with open(f'test_{test_id}_scores.py', 'w') as outfile:
        outfile.write("scores = ")
        json.dump(scores, outfile)


if __name__ == '__main__':
    main()
