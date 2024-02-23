import requests
import json
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

for i in range(10):
  print("Hello, World!")

print((((1+2)*3)/4)**5)

#print("The average size is: " + str(average)) #implicit conversion
bearer_token_post= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDg4OTU5MDksImp0aSI6IjIzMzM3MjIyNDhiNDE3NmRhNGY0ODhjYTE2YTM4MzcwZmIyYTI1NjBiY2IyZGI0M2NiNDM4YWUxNzI3MDhmMWMiLCJpYXQiOjE3MDg3MjMxMDksImlzcyI6ImFwaS5zcXVhZGNhc3QuY29tIiwibmJmIjoxNzA4NzIzMTA5LCJpZCI6IjY1ZDhmYTE0YzBlYjlmZTUzMTczNzVjZCIsImZpcnN0X25hbWUiOiJCYXJyeSAiLCJlbWFpbCI6InNxdWFkQHNxdWFkMi5jb20iLCJ1c2VyIjpudWxsLCJzc29fbG9naW4iOmZhbHNlLCJzc29fdG9rZW4iOiIiLCJvcmdhbml6YXRpb25faWQiOiI2NWQ4ZmEyMGMwZWI5ZmU1MzE3Mzc1Y2UiLCJvcmdhbml6YXRpb24iOm51bGwsInJlZnJlc2hfdG9rZW4iOiJhYmQ3NDNjZDkwYTJkZDBhN2NkMjJmMjRlNGU3YmY0MDY2NmVjZWUzM2E3NmY2ZmQ1ODg2MTEwOWJhYzdjMDgzMzllN2MwZDdmMDhhNWFiZjlmMGYxZjVlOTdiOWI4M2NjMzk0OTVjYzQyMjIxNzkwMDNlZTViNzk0ZjM5Y2JmOCIsIndlYl90b2tlbiI6ZmFsc2UsImFwaV90b2tlbiI6dHJ1ZX0.1ek8I76Chcu4lNn7DZ_fSvn50HkJ1Ju2YCmECNtG3EA"

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
  response = requests.request("POST", url, headers=headers1, data=payload)
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

post_users("aditya@squadcast.com","user","Aditya","Anil")