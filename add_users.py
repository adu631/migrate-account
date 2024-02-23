import requests
import json
get_user_token="965e4feaee2841f9d90c7a835f5c9875b3ec1cbba7ea20235aa9498ffce9434d1be03b993557faef7b4fdfc41b52f33a6d5c256aa8027525306e377b39842977"
post_user_token = "c09b4aefabfc5aee801b9bb1e157461644c2cfd66f2050d9d85db3242b2e53d638d21edadfc2146e78be570db78242e7a12748ac43678501df8cef6ddfd439d2"
payload = {}
"""get_headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDgwNzk2MzgsImp0aSI6IjMyMWFjNTcxYWI2NmNhODIzMGI3MDYwMzY1OTM2YzljN2M3YTQyZTIxZWE0NWU3ZGIzM2RhYjc4Yjg0MjA2N2IiLCJpYXQiOjE3MDc5MDY4MzgsImlzcyI6ImFwaS5zcXVhZGNhc3QuY29tIiwibmJmIjoxNzA3OTA2ODM4LCJpZCI6IjYxMmY5YmJjNGFmYjE0MDAwNzMxNDU5MCIsImZpcnN0X25hbWUiOiJBa2FzaCIsImVtYWlsIjoiYWthc2hAc3F1YWRjYXN0LmNvbSIsInVzZXIiOm51bGwsInNzb19sb2dpbiI6ZmFsc2UsInNzb190b2tlbiI6IiIsIm9yZ2FuaXphdGlvbl9pZCI6IjVkMTM1MzU5MDA4NjA0MDAxMmVhODg5ZSIsIm9yZ2FuaXphdGlvbiI6bnVsbCwicmVmcmVzaF90b2tlbiI6IjdkZmYwNmEzZjQwM2VhNTg5Mzc2NzJjZDk4ZDU5MWUwMjJhMWI4OGUzN2Q2ZjJhYzZmYTU3YjdiYjQ0MjBmYjEzNDFlMzhiYTIwOTYxOWVjYmIzOTgxMTRkNTBmZmU3MTQ0MDNlMzY5Nzg2OGFmMWZmMDc3MDlhMTE4NDljOGUyIiwid2ViX3Rva2VuIjpmYWxzZSwiYXBpX3Rva2VuIjp0cnVlfQ.Fsin09O3f1Ysq8BMWp0G8Xacy_mJATpWkSRu4G9HI-E'
}
post_headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDgwNzgwNDAsImp0aSI6IjhkYTEwMzA2NWFkZWZmYTI3ZDI3ZmVmYTIzNjQ0Y2VmNzRhNDViMTYzODQ4NTM2OTRjZWRmZGNmOWRiNjFjYmMiLCJpYXQiOjE3MDc5MDUyNDAsImlzcyI6ImFwaS5zcXVhZGNhc3QuY29tIiwibmJmIjoxNzA3OTA1MjQwLCJpZCI6IjYxMmY5YmJjNGFmYjE0MDAwNzMxNDU5MCIsImZpcnN0X25hbWUiOiJBa2FzaCIsImVtYWlsIjoiYWthc2hAc3F1YWRjYXN0LmNvbSIsInVzZXIiOm51bGwsInNzb19sb2dpbiI6ZmFsc2UsInNzb190b2tlbiI6IiIsIm9yZ2FuaXphdGlvbl9pZCI6IjY1Y2M4NzA4OGE2MWI1NjZkZTQ3YTg0NSIsIm9yZ2FuaXphdGlvbiI6bnVsbCwicmVmcmVzaF90b2tlbiI6IjVlZmFkMGQyMDEzZTE0MTRjNTk0MGJmMWE3ZjAzNmMwN2NiMmZiMWE3MmQ3NjhhODk1YTU4Nzg5MjRkODRmZjUxM2E5ZmFmNjE1OTVmMWRiODhjNzhhZDNmOTBhOTkzMzNlNDRhNDlmOTU1NGI3ZTFjZDBlYjlkOTUxNzE3NjQwIiwid2ViX3Rva2VuIjpmYWxzZSwiYXBpX3Rva2VuIjp0cnVlfQ.hRkwN9zOriopzBuqHSi9l-CE0eX5C7wkZfhTo8YGtU8'
}"""

def handle_request(method, url, headers, data):
    try:
        response = requests.request(method, url, headers=headers, data=data)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def get_auth_token():
  url = "https://auth.squadcast.com/oauth/access-token"
  response = handle_request("GET", url, headers = {"X-Refresh-Token": str(get_user_token)}, data=payload)
  return response

def post_auth_token():
  url = "https://auth.squadcast.com/oauth/access-token"
  response = handle_request("GET", url, headers = {"X-Refresh-Token": str(post_user_token)}, data=payload)
  return response

token = get_auth_token()
bearer_token_get = token["data"]["access_token"]
#print(bearer_token_get)

token = post_auth_token()
bearer_token_post = token["data"]["access_token"]
#print(bearer_token_post)
#print(bearer_token_post)

def get_users():
  url = "https://api.squadcast.com/v3/users"
  response = handle_request("GET", url, headers = {'Authorization': "Bearer "+str(bearer_token_get)},data=payload)
  return response

get_users1 = get_users()

#for x in get_users1["data"]:
  #print (get_users1["data"][x])

def get_team():
  url = "https://api.squadcast.com/v3/teams/:teamID"
  response = requests.request("GET", url, headers = {'Authorization': "Bearer "+str(bearer_token_get)})
  res = response.json()
  return res

def post_users(email, role, firstname, lastname):
  url = "https://api.squadcast.com/v3/users"
  if(role=="account_owner"):
    roles= "user"
  else:
    roles = role
  payload = {
    "email": email,
    "role": roles,
    "first_name": firstname,
    "last_name": lastname           
             }
  headers1 = {'Authorization': "Bearer "+str(bearer_token_post),'Content-Type': 'application/json'}
  #handle_request("POST", url, headers=headers1,data=payload)
  try:
    response = requests.request("POST", url, headers=headers1, json=payload)
    response.raise_for_status()
    print(response.text)  # Print the raw response
    res = response.json()
    print(res)
  except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    res = response.json()
  print(res)
  """response = requests.request("POST", url, headers=headers1, data=payload)
  res = response.json()
  print(res)"""
  

def migrate_users():
  users = get_users()
  for x in users["data"]:
    email = x["email"]
    role  = x["role"]
    firstname = x["first_name"]
    lastname = x["last_name"]
    print(email+" "+role+" "+firstname+" "+lastname)
    post_users(email, role, firstname, lastname)

migrate_users()
    


   

  
#print( get_users1)
