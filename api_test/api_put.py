import requests

payload={
    "name": "Anshuman",
    "job": "Software Engineer"
    }
resp=requests.put("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
#print(resp.headers.get("Content-Type"))