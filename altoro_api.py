import requests
import json
import subprocess

base_url = "http://demo.testfire.net/api"
auth_token = ""

def login(username, password):
    global auth_token
    data = {
        "username": username,
        "password": password
    }
    r = requests.post(base_url + "/login", data=json.dumps(data))
    if(r.status_code==200):
        auth_token = r.json()["Authorization"]
        return True
    return False

def logout():
    global auth_token
    headers = {
        "Authorization": auth_token
    }
    r = requests.get(base_url + "/logout", headers=headers)
    if r.status_code == 200:
        auth_token = ""
        return True
    return False

def check_login():
    global auth_token
    headers = {
        "Authorization": auth_token
    }
    r = requests.get(base_url + "/login", headers=headers)
    if r.status_code == 200:
        return True
    return False

def get_accounts():
    global auth_token
    headers = {
        "Authorization": auth_token
    }
    r = requests.get(base_url + "/account", headers=headers)
    if r.status_code == 200:
        return r.json()
    return {}

def get_account(account_no):
    global auth_token
    headers = {
        "Authorization": auth_token
    }
    r = requests.get(base_url + "/account/"+str(account_no), headers=headers)
    if r.status_code == 200:
        return r.json()
    return {}

def get_transactions(account_no):
    global auth_token
    headers = {
        "Authorization": auth_token
    }
    r = requests.get(base_url + "/account/"+str(account_no)+"/transactions", headers=headers)
    if r.status_code == 200:
        return r.json()
    return {}

def transfer(from_account, to_account, amount):
    global auth_token
    headers = {
        "Authorization": auth_token
    }
    data = {
        "toAccount": "\""+to_account+"\"",
        "fromAccount": "\""+from_account+"\"",
        "transferAmount": "\""+amount+"\""
    }
    r = requests.post(base_url + "/transfer", headers=headers, data=data)
    if r.status_code == 200:
        return True
    print("Code: " +str(r.status_code))
    return False

def readCredsFromConfig(config_file):
    config = open(config_file)
    user = config.readline().strip()
    passwd = config.readline().strip()
    return (user,passwd)

def file_exists(dir_path, file_name):
    p = subprocess.Popen(["dir", dir_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if(file_name in str(output)):
        return True
    return False
