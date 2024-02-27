import requests
import json
get_user_token="965e4feaee2841f9d90c7a835f5c9875b3ec1cbba7ea20235aa9498ffce9434d1be03b993557faef7b4fdfc41b52f33a6d5c256aa8027525306e377b39842977"
post_user_token = "c09b4aefabfc5aee801b9bb1e157461644c2cfd66f2050d9d85db3242b2e53d638d21edadfc2146e78be570db78242e7a12748ac43678501df8cef6ddfd439d2"
payload = {}

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

def get_schedules():
    query = """
    query {
        schedules(filters: {
            teamID: "62b171a33318bc15fdbd5e11",
            scheduleIDs: [],
            participants: [],
            escalationPolicies: [],
            limit: 1,
            offset: 0
        }) {
            teamID,
            name,
            timeZone,
            orgID,
            description,
            rotations {
                name,
                color,
                startDate,
                period,
                changeParticipantsUnit,
                changeParticipantsFrequency,
                endDate,
                shiftTimeSlot{
                    startHour,
                    startMin,
                    duration
                }
                endsAfterIterations
            },
            owner {
                type,
                ID
            }
        }
    }
    """
    payload = {
        "query": query
    }
    url = "https://api.squadcast.com/v3/graphql"
    headers1 = {"Authorization": "Bearer " + str(bearer_token_get)}

    response = requests.post(url, headers=headers1, json=payload)
    #response = handle_request("POST",url,headers= headers1, data=payload)

    if response.status_code == 400:
        print(f"Error 400: {response.text}")

    return response.json()

print(get_schedules())
""""
def post_schedules():
   schedules= get_schedules()
   for x in schedules["data"]["schedules"]:
    x["teamID"]= "65d8fa20c0eb9fe5317375d3"
    x["owner"]["ID"]= "65d8fa20c0eb9fe5317375d3"
    x["owner"]["type"]= "team"
   mutation = schedules["data"]["schedules"]
   print(mutation)
   mutation_string = "mutation { createSchedule(input:{" + str(mutation) + " ){ID,name,rotations{ID,name,startDate,period,changeParticipantsUnit,changeParticipantsFrequency},timeZone}}"
   print(" string" +mutation_string)   
   headers1 = {"Authorization": "Bearer " + str(bearer_token_post)}
   url = "https://api.squadcast.com/v3/graphql"
   payload = {"query": mutation_string}
   response = requests.post(url, headers=headers1, json=payload)
   print(response.text)
   return response.json()

post_schedules()

#print(get_schedules())
"""
def post_schedules():
    schedules = get_schedules()
    for schedule in schedules["data"]["schedules"]:
        schedule["teamID"] = "65d8fa20c0eb9fe5317375d3"
        schedule["owner"]["ID"] = "65d8fa20c0eb9fe5317375d3"
        schedule["owner"]["type"] = "team"

    mutation = json.dumps(schedules["data"]["schedules"]).replace('"', '\\"')
    mutation_string = f'mutation {{ createSchedule(input: {mutation}) {{ ID, name, rotations {{ ID, name, startDate, period, changeParticipantsUnit, changeParticipantsFrequency, shiftTimeSlot {{ startHour, startMin, duration }} }} }} }}'

    headers1 = {"Authorization": "Bearer " + str(bearer_token_post)}
    url = "https://api.squadcast.com/v3/graphql"
    payload = {"query": mutation_string}
    response = requests.post(url, headers=headers1, json=payload)

    print(response.text)
    return response.json()

post_schedules()