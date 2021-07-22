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
        
    def GetAllMailingLists(self):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/list"
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
        
    def RemoveSubscribersMailingList(self,input_mailingListId,email):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/subscriber-remove"
        

        myobjs = {"data":email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
        
    def AddBannedUserMailingList(self,input_mailingListId,email):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/banned-user-add"
        

        myobjs = {"data":email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def AddDigestSubscribers(self,input_mailingListId,email):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/digest-subscriber-add"
        

        myobjs = {'data':email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def RemoveSubscribersMailingListALL(self,input_mailingListId):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/subscriber-remove-all"
        

        #myobjs = {"data":email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url,  headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def EditSubscriberMailinglists(self,input_subscriberEmail,input_mailingListId,input_mailingListId2):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/subscribers/" + input_subscriberEmail + "/edit/" + input_mailingListId + ""
        

        myobjs = {'subscribedLists':"input_mailingListId2"}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def GetSubscriberMailingList(self,input_mailingListId,input_subscriberEmail):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/subscribers/" + input_subscriberEmail + "/" + input_mailingListId + ""
        

        myobjs = {""}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.get(url, headers = header)
        return(x.json())
        
        
        
         
    def OptInUser(self,input_data,input_post):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/optin/" + input_data + ""
        

        myobjs = {"data":input_post}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        return(x.json())
        
        
        
        
    def OptInUser(self,input_data,input_post):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/optin/" + input_data + ""
        

        myobjs = {"data":input_post}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        return(x.json())
        
        
        
    def RemoveDigestSubscribers(self,input_mailingListId,sub_email):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/digest-subscriber-remove"
        

        myobjs = {"data":sub_email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        return(x.json()) 


    def AddDigestSubscribers(self,input_mailingListId,sub_email):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/digest-subscriber-add"
        

        myobjs = {"data":sub_email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        return(x.json())
        
        
    def RemoveDigestSubscribersALL(self,input_mailingListId):
    
        global auth
        url = self.url + "/api/v1/settings/domain/mailing-lists/" + input_mailingListId + "/digest-subscriber-remove-all"
        

        #myobjs = {"data":sub_email}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, headers = header)
        return(x.json())      
        
    def SendMessage(self,email_from,email_to,subject,body):
    
        global auth
        url = self.url + "/api/v1/mail/message-put"
        

        myobjs = {"from":email_from,"subject":subject,"to":email_to,"messagePlainText":body}
        header = {'Authorization' : 'Bearer ' + auth}
        x = requests.post(url, data = myobjs, headers = header)
        x.encoding = x.apparent_encoding
        return(x.text)
