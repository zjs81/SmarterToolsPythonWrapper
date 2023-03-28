from smapi import SMAPI

me = SMAPI("admin","adminpassword","https://mail.mailserver.com")



# System Admin Only Calls
print(me.get_user("admin@domain.com"))
print(me.system_domain_details("domain.com"))
print(me.system_export_domains_list())
print(me.system_export_domains_list_to_file("test.csv"))

me = SMAPI("admin@domain","pass","https://mail.domain.com")

#Domain Admin Only Calls
print(me.get_domain())
print(me.get_domain_permissions())
print(me.get_total_domain_users())
print(me.get_alias("testing"))
print(me.domain_account_list_count())
