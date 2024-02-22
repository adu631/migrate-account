import requests
import json

payload = {}
get_headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDgwNzk2MzgsImp0aSI6IjMyMWFjNTcxYWI2NmNhODIzMGI3MDYwMzY1OTM2YzljN2M3YTQyZTIxZWE0NWU3ZGIzM2RhYjc4Yjg0MjA2N2IiLCJpYXQiOjE3MDc5MDY4MzgsImlzcyI6ImFwaS5zcXVhZGNhc3QuY29tIiwibmJmIjoxNzA3OTA2ODM4LCJpZCI6IjYxMmY5YmJjNGFmYjE0MDAwNzMxNDU5MCIsImZpcnN0X25hbWUiOiJBa2FzaCIsImVtYWlsIjoiYWthc2hAc3F1YWRjYXN0LmNvbSIsInVzZXIiOm51bGwsInNzb19sb2dpbiI6ZmFsc2UsInNzb190b2tlbiI6IiIsIm9yZ2FuaXphdGlvbl9pZCI6IjVkMTM1MzU5MDA4NjA0MDAxMmVhODg5ZSIsIm9yZ2FuaXphdGlvbiI6bnVsbCwicmVmcmVzaF90b2tlbiI6IjdkZmYwNmEzZjQwM2VhNTg5Mzc2NzJjZDk4ZDU5MWUwMjJhMWI4OGUzN2Q2ZjJhYzZmYTU3YjdiYjQ0MjBmYjEzNDFlMzhiYTIwOTYxOWVjYmIzOTgxMTRkNTBmZmU3MTQ0MDNlMzY5Nzg2OGFmMWZmMDc3MDlhMTE4NDljOGUyIiwid2ViX3Rva2VuIjpmYWxzZSwiYXBpX3Rva2VuIjp0cnVlfQ.Fsin09O3f1Ysq8BMWp0G8Xacy_mJATpWkSRu4G9HI-E'
}
post_headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDgwNzgwNDAsImp0aSI6IjhkYTEwMzA2NWFkZWZmYTI3ZDI3ZmVmYTIzNjQ0Y2VmNzRhNDViMTYzODQ4NTM2OTRjZWRmZGNmOWRiNjFjYmMiLCJpYXQiOjE3MDc5MDUyNDAsImlzcyI6ImFwaS5zcXVhZGNhc3QuY29tIiwibmJmIjoxNzA3OTA1MjQwLCJpZCI6IjYxMmY5YmJjNGFmYjE0MDAwNzMxNDU5MCIsImZpcnN0X25hbWUiOiJBa2FzaCIsImVtYWlsIjoiYWthc2hAc3F1YWRjYXN0LmNvbSIsInVzZXIiOm51bGwsInNzb19sb2dpbiI6ZmFsc2UsInNzb190b2tlbiI6IiIsIm9yZ2FuaXphdGlvbl9pZCI6IjY1Y2M4NzA4OGE2MWI1NjZkZTQ3YTg0NSIsIm9yZ2FuaXphdGlvbiI6bnVsbCwicmVmcmVzaF90b2tlbiI6IjVlZmFkMGQyMDEzZTE0MTRjNTk0MGJmMWE3ZjAzNmMwN2NiMmZiMWE3MmQ3NjhhODk1YTU4Nzg5MjRkODRmZjUxM2E5ZmFmNjE1OTVmMWRiODhjNzhhZDNmOTBhOTkzMzNlNDRhNDlmOTU1NGI3ZTFjZDBlYjlkOTUxNzE3NjQwIiwid2ViX3Rva2VuIjpmYWxzZSwiYXBpX3Rva2VuIjp0cnVlfQ.hRkwN9zOriopzBuqHSi9l-CE0eX5C7wkZfhTo8YGtU8'
}
ep_id = '65cc8cde5e82dc787af1f2a3'

def get_all_users():
  url = "https://api.squadcast.com/v3/users"
  response = requests.request("GET", url, headers=get_headers, data=payload)
  res = response.json()
  return res


def get_all_services():
  url = "https://api.squadcast.com/v3/services?owner_id=612cdcf97115ff9a44a10357"
  response = requests.request("GET", url, headers=get_headers, data=payload)
  res = response.json()
  return res

def get_all_tagging_rules(service_id):
  url = "https://api.squadcast.com/v3/services/"+service_id+"/tagging-rules"
  response = requests.request("GET", url, headers=get_headers, data=payload)
  res = response.json()
  return res

def get_all_deduplication_rules(service_id):
  url = "https://api.squadcast.com/v3/services/"+service_id+"/deduplication-rules"
  response = requests.request("GET", url, headers=get_headers, data=payload)
  res = response.json()
  return res

def create_services(name,ep_id,email_prefix):
  url = "https://api.squadcast.com/v3/services"
  payload = json.dumps({
    "name": name,
    "escalation_policy_id": ep_id,
    "email_prefix": email_prefix
  })
  response = requests.request("POST", url, headers=post_headers, data=payload)
  res = response.json()
  return res

def create_tagging_rule(services_id, expression, tag, is_basic, basic_expression):
  url = "https://api.squadcast.com/v3/services/"+services_id+"/tagging-rules/new"

  payload = json.dumps({
    "rule": {
      "expression": expression,
      "tags": tag,
      "is_basic": is_basic,
      "basic_expression": basic_expression
    }
  })
  response = requests.request("POST", url, headers=post_headers, data=payload)
  res = response.json()
  print(res)

def create_deduplication_rule(services_id, expression, time_window, is_basic, basic_expression):
  url = "https://api.squadcast.com/v3/services/"+services_id+"/deduplication-rules/new"

  payload = json.dumps({
    "rule": {
      "expression": expression,
      "time_window": time_window,
      "is_basic": is_basic,
      "basic_expression": basic_expression,
      "time_unit":"hour"
    }
  })
  response = requests.request("POST", url, headers=post_headers, data=payload)
  res = response.json()
  print(res)



def clone():
  services = get_all_services()
  for service in services["data"]:
    email_prefix = service["email"].split("@")[0]
    created_service = create_services(service["name"], ep_id, email_prefix)
    tagging_rules = get_all_tagging_rules(service["id"])
    for t in tagging_rules["data"]['rules']:
      basic_expression = ''
      if 'basic_expression' in t:
        basic_expression = t['basic_expression']
      create_tagging_rule(created_service["data"]["id"], t['expression'], t['tags'], t['is_basic'], basic_expression)

clone()
