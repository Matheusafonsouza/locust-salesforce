from os import getenv


SALESFORCE_BASE_URL = getenv("SALESFORCE_BASE_URL", "")
AUTHENTICATE = getenv("AUTHENTICATE", "")== "true"
AUTH_TOKEN = getenv("AUTH_TOKEN", "")
