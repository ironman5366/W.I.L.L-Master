import os
import getpass

signing_key = input("Signing key:")
db_url = input("DB url:")
db_username = input("DB username:")
db_password = getpass.getpass("DB password:")

env_data = {
    "SIGNING_KEY": signing_key,
    "DB_URL": db_url,
    "DB_USERNAME": db_username,
    "DB_PASSWORD": db_password
}

env_file = open("core.env", 'w')
for k,v in env_data.items():
    env_file.write("{0}={1}\n".format(k,v))

env_file.close()

print ("Done! You can now start the instances with docker-compose up. Afterwords, please delete core.env for security")
