import requests


payload={
    "name": "Anshuman",
    "job": "Software Engineer"
    }
resp=requests.post("https://reqres.in/api/users",data=payload)
print(resp)
print(resp.json())
assert resp.json()['job']=='Software Engineer'

