import requests
import json

get_user_token="b4a2de906b0c2c69e88bcc4f56add43685f7eeccf13bab79bdc324499403137ad3c1b450044856628814fed6688da2b77fe285ec32c22fd7852f78674a5d39a3"
post_user_token ="b4a2de906b0c2c69e88bcc4f56add43685f7eeccf13bab79bdc324499403137ad3c1b450044856628814fed6688da2b77fe285ec32c22fd7852f78674a5d39a3"
payload = {}
ep_id = '65dce450f5a538ebb592836d'

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
print(bearer_token_post)


def get_all_services():
  url = "https://api.squadcast.com/v3/services?owner_id=612cdcf97115ff9a44a10357"
  headers = {"Authorization": f"Bearer {bearer_token_get}"}
  response = requests.request("GET", url, headers=headers, data=payload)
  res = response.json()
  return res

def get_all_tagging_rules(service_id):
  url = "https://api.squadcast.com/v3/services/"+service_id+"/tagging-rules"
  headers = {"Authorization": f"Bearer {bearer_token_get}"}
  response = requests.request("GET", url, headers=headers, data=payload)
  res = response.json()
  return res

def get_all_deduplication_rules(service_id):
  url = "https://api.squadcast.com/v3/services/"+service_id+"/deduplication-rules"
  headers = {"Authorization": f"Bearer {bearer_token_get}"}
  response = requests.request("GET", url, headers=headers, data=payload)
  res = response.json()
  return res

def create_services(name,ep_id,email_prefix):
  url = "https://api.squadcast.com/v3/services"
  payload = json.dumps({
    "name": name +" GE",
    "escalation_policy_id": ep_id,
    "email_prefix": email_prefix,
    "owner_id": "65dcdef5f5a538ebb59281cc"
  })
  headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {bearer_token_post}"}
  response = requests.request("POST", url, headers=headers, data=payload)
  res = response.json()
  print(res)
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
  headers = {"Authorization": f"Bearer {bearer_token_post}"}
  response = requests.request("POST", url, headers=headers, data=payload)
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
  headers = {"Authorization": f"Bearer {bearer_token_post}"}
  response = requests.request("POST", url, headers=headers, data=payload)
  res = response.json()
  print(res)



def clone():
  services = get_all_services()
  for service in services["data"]:
    print(service)
    #email_prefix = service["email"].split("@")[0]
    email_prefix = service["id"]
    created_service = create_services(service["name"], ep_id, email_prefix)
    print(created_service)
    tagging_rules = get_all_tagging_rules(service["id"])
    for t in tagging_rules["data"]['rules']:
      basic_expression = ''
      if 'basic_expression' in t:
        basic_expression = t['basic_expression']
        create_tagging_rule(created_service["data"]["id"], t['expression'], t['tags'], t['is_basic'], basic_expression)

clone()
