import requests
import json


class SMAPI:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.auth = self.authenticate()
        self.auth_impersonate = None

    def authenticate(self):
        """
        Authenticate the user and store the access token.
        """
        auth_url = f"{self.url}/api/v1/auth/authenticate-user"
        auth_data = {"username": self.username, "password": self.password}
        response = requests.post(auth_url, json=auth_data)
        access_info = response.json()
        return access_info["accessToken"]

    def _get(self, endpoint, path_params="", alt_auth=False, other_headers=None):
        """
        Helper function to perform GET requests.

        Parameters
        ----------
        endpoint:
            The endpoint.
        path_params:
            The path params. Defaults to an empty string.
        alt_auth: bool
            Defaults to False. Set to True to use current impersonated user.
        """
        url = f"{self.url}{endpoint}{path_params}"
        if alt_auth:
            if not self.auth_impersonate:
                raise ValueError(
                    "No impersonate token. Need to `impersonate_user()` first."
                )
            headers = {"Authorization": f"Bearer {self.auth_impersonate}"}
        else:
            headers = {"Authorization": f"Bearer {self.auth}"}
        if other_headers and type(other_headers) is dict:
            headers.update(other_headers)

        response = requests.get(url, headers=headers)
        return response.json()

    def _post(
        self, endpoint, path_params="", alt_auth=False, other_headers=None, data=None
    ):
        """
        Helper function to perform POSt requests.

        Parameters
        ----------
        endpoint:
            The endpoint.
        path_params:
            The path params. Defaults to an empty string.
        alt_auth: bool
            Defaults to False. Set to True to use current impersonated user.
        data: dict
            Defaults to empty dict. Data to be posted

        """
        if not data:
            data = {}

        url = f"{self.url}{endpoint}{path_params}"
        if alt_auth:
            if not self.auth_impersonate:
                raise ValueError(
                    "No impersonate token. Need to `impersonate_user()` first."
                )
            headers = {"Authorization": f"Bearer {self.auth_impersonate}"}
        else:
            headers = {"Authorization": f"Bearer {self.auth}"}
        if other_headers and type(other_headers) is dict:
            headers.update(other_headers)

        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def get_user(self, input_email):
        """
        Get user data by email.
        """
        data = {"email": input_email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        url = f"{self.url}/api/v1/settings/sysadmin/get-user"
        return requests.post(url, json=data, headers=headers).json()

    def get_domain(self, domain: str, return_type: str = "inner"):
        """
        Get domain data.

        Parameters
        ----------
        domain: str
            The domain name in SmarterMail.
        return_type: str
            Default value is "inner" and will return a dict of the domain info.
            Set to anything else, returns the JSON response as dict.

        """
        domain_admins = self.get_domain_admins(domain=domain)
        self.impersonate_user(domain_admins[0])
        response = self._get("/api/v1/settings/domain/data", alt_auth=True)
        if return_type == "inner":
            response_inner_dict = response["domainData"]
            return response_inner_dict
        else:
            return response

    def get_domain_permissions(self):
        """
        Get domain permissions.
        """
        return self._get("/api/v1/settings/domain/permissions")

    def get_total_domain_users(self):
        """
        Get the total number of domain users.
        """
        return self._get("/api/v1/settings/domain/total-server-users")

    def get_alias(self, alias_name):
        """
        Get domain alias data.
        """
        return self._get("/api/v1/settings/domain/alias/", alias_name)

    def domain_account_list_count(self):
        """
        Get domain account list counts.
        """
        return self._get("/api/v1/settings/domain/account-list-counts")

    def system_domain_details(self, input_domain):
        """
        Get system domain details.
        """
        return self._get("/api/v1/settings/sysadmin/domain/", input_domain)

    def system_export_domains_list(self):
        """
        Export domains list.
        """
        url = f"{self.url}/api/v1/settings/sysadmin/export-domains-list"
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def system_export_domains_list_to_file(self, filename):
        """
        Export domains list and save to a file.
        """
        content = self.system_export_domains_list()
        with open(filename, "w") as file:
            file.write(f"x = {content}\n")
        return content

    def get_all_mailing_lists(self):
        """
        Get all mailing lists.
        """
        return self._get("/api/v1/settings/domain/mailing-lists/list")

    def remove_subscribers_mailing_list(self, input_mailing_list_id, email):
        """
        Remove subscribers from a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/subscriber-remove"
        data = {"data": email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def add_banned_user_mailing_list(self, input_mailing_list_id, email):
        """
        Add a banned user to a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/banned-user-add"
        data = {"data": email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def add_digest_subscribers(self, input_mailing_list_id, email):
        """
        Add digest subscribers to a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/digest-subscriber-add"
        data = {"data": email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def remove_subscribers_mailing_list_all(self, input_mailing_list_id):
        """
        Remove all subscribers from a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/subscriber-remove-all"
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def edit_subscriber_mailing_lists(
        self, input_subscriber_email, input_mailing_list_id, input_mailing_list_id2
    ):
        """
        Edit subscriber mailing list information.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/subscribers/{input_subscriber_email}/edit/{input_mailing_list_id}"
        data = {"subscribedLists": input_mailing_list_id2}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def get_subscriber_mailing_list(
        self, input_mailing_list_id, input_subscriber_email
    ):
        """
        Get subscriber mailing list information.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/subscribers/{input_subscriber_email}/{input_mailing_list_id}"
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def opt_in_user(self, input_data, input_post):
        """
        Opt in a user to a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/optin/{input_data}"
        data = {"data": input_post}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    def remove_digest_subscribers(self, input_mailing_list_id, sub_email):
        """
        Remove digest subscribers from a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/digest-subscriber-remove"
        data = {"data": sub_email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    def add_digest_subscribers(self, input_mailing_list_id, sub_email):
        """
        Add digest subscribers to a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/digest-subscriber-add"
        data = {"data": sub_email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    def remove_digest_subscribers_all(self, input_mailing_list_id):
        """
        Remove all digest subscribers from a mailing list.
        """
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailing_list_id}/digest-subscriber-remove-all"
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, headers=headers)
        return response.json()

    def send_message(self, email_from, email_to, subject, body):
        """
        Send a message using the mail API.
        """
        url = f"{self.url}/api/v1/mail/message-put"
        data = {
            "from": email_from,
            "subject": subject,
            "to": email_to,
            "messagePlainText": body,
        }
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def restore_folders(self, folder, email, recursive):
        """
        Restore folders for a given email.
        """
        url = f"{self.url}/api/v1/settings/sysadmin/restore-folders"
        data = {
            "restorations": [{"folder": folder, "email": email, "recursive": recursive}]
        }
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def get_user_folder(self, folder):
        """
        Get a user folder.
        """
        url = f"{self.url}/api/v1/folders/folder"
        data = {"folder": folder}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def list_mail_folders_users(self):
        """
        List mail folders for users.
        """
        url = f"{self.url}/api/v1/folders/list-email-folders"
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def system_admin_impersonate_user(self, email):
        """
        Impersonate a user as a system administrator.
        """
        url = f"{self.url}/api/v1/settings/domain/impersonate-user"
        data = {"email": email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        text = response.text.replace("true", '"true"').replace("null", '"null"')
        result = eval(text)
        self.auth = result["impersonateAccessToken"]
        return self.auth

    def impersonate_user(self, email: str):
        """
        Impersonate a user.
        """
        url = f"{self.url}/api/v1/settings/domain/impersonate-user"
        data = {"email": email}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        text = response.text.replace("true", '"true"').replace("null", '"null"')
        result = eval(text)
        self.auth_impersonate = result["impersonateAccessToken"]
        return None

    def get_domain_admins(self, domain: str, return_type="inner"):
        """
        Get domain admins.

        Parameters
        ----------
        domain: str
            The domain name in SmarterMail.
        return_type: str
            Default value is "inner" and will return a list of the domain admin
            email addresses. Set to anything else, returns `response.text`

        """
        url = f"{self.url}/api/v1/settings/sysadmin/domain-admins/{domain}"
        data = {"domain": domain}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.get(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        if response.ok and return_type == "inner":
            response_dict = json.loads(response.text)
            response_inner_dict = response_dict["domainAdmins"]
            return response_inner_dict
        else:
            return response.text

    def list_users_domain(self):
        """
        List users in a domain.
        """
        url = f"{self.url}/api/v1/settings/domain/list-users"
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def edit_folder_user(self, folder, new_folder):
        """
        Edit a user folder.
        """
        url = f"{self.url}/api/v1/folders/folder-patch"
        data = {"newFolder": new_folder, "folder": folder}
        headers = {"Authorization": f"Bearer {self.auth}"}
        response = requests.post(url, json=data, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text

    def get_github(self):
        """
        Get GitHub repo
        """
        print(
            "Visit https://github.com/zjs81/SmarterToolsPythonWrapper Thanks for using this wrapper! "
        )
