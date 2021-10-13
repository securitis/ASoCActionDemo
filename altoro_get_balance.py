import altoro_api as altoro
import sys
#import pickle
import hashlib
import os

#user = "jsmith"
#password = "demo1234"
#(user,password) = altoro.readCredsFromConfig("config.txt")

print("Logging in...", end="")
if(altoro.login(user, password)==False):
    print("False")
    print("Error logging in... exiting")
    sys.exit(1)

print("Successful")

hash = hashlib.md5(altoro.auth_token.encode('ascii'))
print("Authorization Token Hash:" + str(hash.hexdigest()))

output = ""
print("Getting Account Balances")
accounts = altoro.get_accounts()

print("Account Name\t\tAccount Number\t\tBalance")
for account in accounts['Accounts']:
    details = altoro.get_account(account['id'])
    output += str(details) + "\n"
    print(account['Name']+"\t\t"+account['id']+"\t\t"+details['balance'])

print("Logging out..." + str(altoro.logout()))

print("Writing Balances to File")

#remove the old balance file
#if(os.path.isfile("balances.txt")):
if(altoro.file_exists("","balances.txt")):
    print("Removing old balance file")
    os.remove("balances.txt")
balanceFile = open("balances.txt", "w")
balanceFile.write(output)
balanceFile.close()
print("Done")
