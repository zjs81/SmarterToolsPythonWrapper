import requests
global auth
import time
class SMAPI:
    
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
    

    def auth(self):
        global auth
        username = self.username
        password = self.password
        url = self.url
        authurl = url + "/api/v1/auth/authenticate-user"
        myobj = {'username': username, 'password':password}
        x = requests.post(authurl, data = myobj)
        auth = str(x.text)
        auth = auth.split(",")
        auth = auth[11]
        auth = auth.split(":")
        auth = auth[1]
        auth = auth.replace("""\"""", "")
        
        
    def GetUser(self,input_email):
        global auth
        url = self.url + "/api/v1/settings/domain/user/" + input_email +""
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
    
    
    def GetDomain(self):
        global auth
        url = self.url + "/api/v1/settings/domain/data"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
    def GetDomainPermissions(self):
    
        global auth
        url = self.url + "/api/v1/settings/domain/permissions"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
    def GetTotalDomainUsers(self):
    
        global auth
        url = self.url + "/api/v1/settings/domain/total-server-users"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
    def GetAlias(self,aliasname):
    
        global auth
        url = self.url + "/api/v1/settings/domain/alias/" + aliasname + ""
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
    def DomainAccountListCount(self):
    
        global auth
        url = self.url + "/api/v1/settings/domain/account-list-counts"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
    def SystemDomainDetails(self,input_domain):
    
        global auth
        url = self.url + "/api/v1/settings/sysadmin/domain/" + input_domain + ""

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())   


    def SystemExportDomainsList(self):
    
        global auth
        url = self.url + "/api/v1/settings/sysadmin/export-domains-list"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)


    def SystemExportDomainsListToFile(self,filename):
    
        global auth
        url = self.url + "/api/v1/settings/sysadmin/export-domains-list"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, headers = header)
        x.encoding = x.apparent_encoding
        try:
            file = open(filename, "x")
        except:
            pass
        file = open(filename, "w")
        file.write("%s = %s\n" %("x", x.text))

        file.close()
        return(x.text)           
        
