import requests
r=requests.get("http://www.youtube.com")
r.status_code
r.headers
# print(r)