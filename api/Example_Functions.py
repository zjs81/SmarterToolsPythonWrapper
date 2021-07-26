import smapi

me = smapi.SMAPI("admin","admin","http://smurl.com")

me.auth()

#System Admin Only Calls
me.GetUser("admin@example.com")
#me.SystemDomainDetails("example.com")
#me.SystemExportDomainsList()
#me.SystemExportDomainsListToFile("test.csv")
#Domain Admin Only Calls
#me.GetDomain()
#me.GetDomainPermissions()
#me.GetTotalDomainUsers()
#me.GetAlias("testing")
#me.DomainAccountListCount()
