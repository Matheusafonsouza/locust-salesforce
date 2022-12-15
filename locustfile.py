from locust import HttpUser, task, between

from fixtures.record import account_payload
from fixtures.auth import auth_payload
from settings import SALESFORCE_BASE_URL, AUTH_TOKEN, AUTHENTICATE


class SalesforceCreateRecordComposeRestApiUser(HttpUser):
    wait_time = between(1, 2.5)

    def get_headers(self):
        token = None
        params = auth_payload

        if not AUTHENTICATE:
            token = AUTH_TOKEN
        else:
            try:
                response = self.client.post(
                    f"{SALESFORCE_BASE_URL}/services/oauth2/token",
                    params=params
                )
                print(response.json())
                token = response.json().get("access_token")
            except:
                print(response.text())

        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    @task
    def create_record(self):
        payload = account_payload

        try:
            response = self.client.post(
                f"{SALESFORCE_BASE_URL}/services/data/v56.0/composite/tree/Account/", 
                headers=self.get_headers(),
                json=payload
            )
            print(response.json())
        except:
            print(response.text)
