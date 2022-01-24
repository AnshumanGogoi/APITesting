import requests

resp=requests.get("https://reqres.in/api/users?delay=3", timeout=2)
print(resp.status_code)