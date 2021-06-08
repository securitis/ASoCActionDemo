The demo script is an api wrapper around the Altoro Mutual API. It comes with a script to grab the account balances for a user and then write them to a file.

The vulnerabilities are:

Import of Pickle:
Since pickle isnt used, this line can just be deleted to remove the issue.

Hard Coded Credentials:
Use the commented method of reading the credentials in from a config file.

(user,password) = altoro.readCredsFromConfig("config.txt")
This line will read the username and password from a file and not have them hardcoded in the script.

OS Injection:
The altoro_api.py has a method called "file_exists" which makes a "dir" os call and then checks if a given filename is in the output.

To remediate the OS Injection, use the built in python method os.path.isfile(<filename>) to check if a file exists