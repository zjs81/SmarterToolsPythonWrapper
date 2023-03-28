This Python library is a simple and easy-to-use wrapper for the SmarterMail API. It covers various API endpoints and allows you to manage SmarterMail accounts and services programmatically.

Installation
You can install the library using pip:
```
pip install smartermail-api
```
https://pypi.org/project/smartermail-api/

Usage
To use the SmarterMail API wrapper, first import the library and create an instance of the SMAPI class with your SmarterMail credentials:

```python
import smapi

api = smapi.SMAPI("username", "password", "http://smurl.com")
```
Examples
Here are some examples of how to use the SmarterMail API wrapper:

System Admin Only Calls
```python
# Get user details
user_details = api.get_user("admin@example.com")

# Get domain details
domain_details = api.get_domain("example.com")

# Export domains list
domains_list = api.export_domains_list()

# Export domains list to file
api.export_domains_list_to_file("test.csv")
```
Domain Admin Only Calls
```python
# Get domain
domain = api.get_domain()

# Get domain permissions
permissions = api.get_domain_permissions()

# Get total domain users
total_users = api.get_total_domain_users()

# Get alias
alias = api.get_alias("testing")

# Get domain account list count
account_list_count = api.domain_account_list_count()
```

License
This project is licensed under the Apache License 2.0. See the LICENSE file for more information.

Support & Contribution
If you encounter any issues or have feature requests, please feel free to open an issue on GitHub. Contributions are also welcome! Simply create a pull request with your changes, and I will review it as soon as possible.

Enjoy using the SmarterMail API wrapper!
