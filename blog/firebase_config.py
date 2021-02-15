import os
import pyrebase
from dotenv import load_dotenv

load_dotenv()
config = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "projectId": os.getenv("projectId"),
    "storageBucket": os.getenv("storageBucket"),
    "messagingSenderId": os.getenv("messagingSenderId"),
    "appId": os.getenv("appId"),
    "measurementId": os.getenv("measurementId"),
    "databaseURL": os.getenv("databaseURL"),

}
# print("your api key is ",os.getenv('apiKey'))
firebase = pyrebase.initialize_app(config)
