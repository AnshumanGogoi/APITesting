import requests

#p={"page":2}
resp = requests.get("https://reqres.in/api/users?page=2")

#Or
#resp=requests.get("https://reqres.in/api/users?",params=p)

json_response=resp.json()
print(json_response['total'])
assert json_response['total']==12
print(json_response['total_pages'])
assert json_response['total_pages']==2
print(json_response["data"][0]["email"])
print(json_response["data"][0]["first_name"])
print(json_response["data"][0]["last_name"])
print(json_response["data"][0]["avatar"])
print(json_response["support"]["url"])
print(json_response["support"]["text"])



#print(resp)
#code=resp.status_code
#assert  code==200, "code does not match"

#print(resp.text)
#print(resp.content)
#print(resp.json())
#print(resp.cookies)
#print(resp.headers)
#print(resp.encoding)
#print(resp.url)
