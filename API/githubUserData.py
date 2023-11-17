import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print("GitHub User Data:")
        print(f"Name: {user_data['name']}")
        print(f"Followers count: {user_data['followers']}")
        print(f"Public Repositories count: {user_data['public_repos']}")
    else:
        print("Error")

get_github_user('shoryagoyal')