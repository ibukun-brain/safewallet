import json
import requests

from django.conf import settings


class WalletAPI:

    def __init__(self, secret_key=None, public_key=None):
        self.url = "https://api.flutterwave.com/v3"
        self.sandbox = "https://api.flutterwave.com/v3"
        self.secret_key = settings.FLUTTERWAVE_SECRET_KEY
        self.public_key = settings.FLUTTERWAVE_PUBLIC_KEY

    def check_balance(self):
        url = self.sandbox + "/self/balance"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "Currency": "NGN",
            "SecretKey": self.secret_key
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp

    def check_transactions(self, date_from, date_to, transaction_type=1):
        url = self.sandbox + "/self/transactions"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "skip": 0,
            "take": 10,
            "dateFrom": date_from,
            "dateTo": date_to,
            "transactionType": transaction_type,
            "secretKey": self.secret_key,
            "currency": "NGN"
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp

    def bank_account_transfer(
            self,
            bank_code,
            account_number,
            account_name,
            amount,
            narration,
            transaction_id):
        url = self.sandbox + "/transfer/bank/account"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "SecretKey": self.secret_key,
            "BankCode": bank_code,
            "AccountNumber": account_number,
            "AccountName": account_name,
            "TransactionReference": transaction_id,
            "Amount": amount,
            "Narration": narration
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp

    def sub_wallets(self):
        url = self.sandbox + "/self/users"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def create_user_wallet(self, account_name, email, mobilenumber, country):
        url = self.url + "/payout-subaccounts/"
        headers = {
            'Authorization': "Bearer " + self.secret_key,
            "Content-Type": "application/json"}
        payload = {
            "account_name": account_name,
            "mobilenumber": mobilenumber,
            "email": email,
            "country": country,
        }
        print("payload:", payload)
        print("payload json:", json.dumps(payload))

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text)
        print(resp)
        return resp

    def retrieve_user_nuban(self, phone_number):
        url = self.sandbox + "/wallet/nuban"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": phone_number,
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def set_user_password(self, phone_number, password):
        url = self.sandbox + "/wallet/password"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": phone_number,
            "password": password,
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def set_user_pin(self, phone_number, transactionPin):
        url = self.sandbox + "/wallet/pin"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": phone_number,
            "transactionPin": transactionPin,
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def check_user_transactions(
            self,
            phone_number,
            date_from,
            date_to,
            transaction_type=1,
            transaction_pin=None):
        url = self.sandbox + "/wallet/transactions"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "skip": 0,
            "take": 10,
            "dateFrom": date_from,
            "dateTo": date_to,
            "transactionType": transaction_type,
            "phoneNumber": phone_number,
            "transactionPin": transaction_pin,
            "currency": "NGN",
            "secretKey": self.secret_key
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def get_user_by_phone(self, phone_number):
        url = self.sandbox + "/wallet/getuser"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": phone_number,
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def get_user_by_email(self, email):
        url = self.sandbox + "/wallet/getuser"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "email": email,
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def get_user_balance(self, phone_number):
        url = self.sandbox + "/wallet/balance"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": phone_number,
            "currency": "NGN",
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def update_user_bvn(
        self,
        first_name,
        last_name,
        email,
        bvn,
        phone_number,
    ):
        url = self.sandbox + "/wallet/updatebvn"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "FirstName": first_name,
            "LastName": last_name,
            "Bvn": bvn,
            "PhoneNumber": phone_number,
            "Email": email,
            "SecretKey": self.secret_key
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def get_user_transaction_details(self, transaction_id):
        """
        Get transaction details about wallet to bank transfer
        transaction_id: a unique transaction id to be generated by developer
        """

        url = self.sandbox + "transfer/bank/details"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "SecretKey": self.secret_key,
            "TransactionReference": transaction_id
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp

    def credit_user(self, transaction_id, phone_number, amount):
        """
        Use this to perform a debit on a sub wallet and credit the main wallet
        transaction_id: a unique transaction id to be generated by developer
        """

        url = self.sandbox + "/wallet/credit"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "transactionReference": transaction_id,
            "amount": amount,
            "phoneNumber": phone_number,
            "secretKey": self.secret_key
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp

    def debit_user(self, transaction_id, phone_number, amount):
        """
        Use this to perform a debit on a sub wallet and credit the main wallet
        transaction_id: a unique transaction id to be generated by developer
        """

        url = self.sandbox + "/wallet/debit"
        headers = {
            'Authorization': "Bearer " + self.public_key,
            "Content-Type": "application/json"
        }
        payload = {
            "transactionReference": transaction_id,
            "amount": amount,
            "phoneNumber": phone_number,
            "secretKey": self.secret_key
        }

        try:
            r = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=60
            )
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp
