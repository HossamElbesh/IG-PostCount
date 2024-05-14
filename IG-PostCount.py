import re, requests

username = input("Enter Username: ")
req = requests.get(f"https://www.instagram.com/{username}/")
pagesource = req.text
postcount = re.search(r"Following, (.+?) Posts", pagesource).group(1)
print(f"Post Count: {postcount}")