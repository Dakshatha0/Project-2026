import json
import requests

def get_user_data(data):
    users = [
    "Dakshatha0",
    "microsoft",
    "google"
    ]
    for user in users:
        github_url = f'https://api.github.com/users/{user}'
        try:
            response = requests.get(github_url)
            if response.status_code == 200:
                response = response.json()
                load_previous_data(data, user, response)
            else:
                print(f"Error: {response.status_code}. User not found")
        except requests.exceptions.RequestException:
            print("Cannot connect to Github")

def load_previous_data(data, user, response):
    curr_followers = response["followers"]
    print(f'{user} currently has {curr_followers} followers')
    if user in data:
        print(f'{user} exists in the json file')
        data_followers = data[user]["followers"]
        if data_followers != curr_followers:
            compare_data(data, user, data_followers, curr_followers)
    else:
        print("User does not exist in database")
        data[user] = {
            "followers":curr_followers
        }
        with open("watchlist_data.json", 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

def compare_data(data, user, data_followers, curr_followers):
    if data_followers == curr_followers:
        print("Followers count remains the same")
    elif curr_followers > data_followers:
        print(f'{user} gained {curr_followers - data_followers} followers')
    else:
        print(f'{user} lost {data_followers - curr_followers} followers')
    save_data(data, user, curr_followers, data_followers)

def save_data(data, user, curr_followers, data_followers):
    data[user]["followers"] = curr_followers
    with open("watchlist_data.json", 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    notify_changes(user, curr_followers, data_followers)

def notify_changes(user, curr_followers, data_followers):
    print(f'''
        ALERT:
            {user} follower count changed
            Old: {data_followers}
            New: {curr_followers}
    ''')

if __name__ == "__main__":
    try:
        with open("watchlist_data.json", "r") as jsonfile:
            data = json.load(jsonfile)
    except FileNotFoundError:
        print("File not found")
        data = {}
    get_user_data(data)
        