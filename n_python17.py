import re
url = input("URL : ").strip()
# if match:= re.search(r"^.+//(.+)&",url):
#     username=match.group(1)
#     print(f"Username: {username}")
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
# print(f"Username: {username}")
if matches:= re.search(r"^(?:https?://)?(?:www\.)?twitter\.(?:com|org)/{[a-z0-9_]})$",url,re.IGNORECASE):
    print(f"Username: {matches.group(1)}")

