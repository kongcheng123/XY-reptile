import configparser

cf = configparser.ConfigParser()
cf.read("../db.conf")

db_host = cf.get("db", "db_user")
print(db_host)