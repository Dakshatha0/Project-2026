import requests
import json

def get_user():
    username = input("Enter github username: ")
    user_details = f'https://api.github.com/users/{username}'
    print(user_details)
    try:
        response = requests.get(user_details)
    except requests.exceptions.RequestException:
        print("Cannot connect to Github")

    if response.status_code == 200:
        result = response.json()
        display_user(result)
    else:
        print(f"Error: {response.status_code}. User not found")

def display_user(result):
    print('Username: ' + result["login"])
    print('Name: ' + result["name"])
    print('Followers: ' + str(result["followers"]))
    print('Following: ' + str(result["following"]))
    print('Public Repositories: ' + str(result["public_repos"]))
    print('Profile URL: ' + result["html_url"])

if __name__ == "__main__":
    get_user()
