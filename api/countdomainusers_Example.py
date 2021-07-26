import smapi
import csv


me = smapi.SMAPI("admin","admin","http://smurl.com")

me.auth()

me.SystemExportDomainsListToFile("test.csv")

domains = open("test.csv", "r")
read_file = csv.reader(domains,dialect='excel')
TotalUsers = 0
for s in read_file:
    
    try:
        
        if "x = Name" == s[0]:
            pass
        else:
            d = s[0]
            z = me.SystemDomainDetails(d)
            z = str(z)
            z = z.split(",")
            print(z[4])
            z=z[4].split(":")
            z = z[1]
            z = int(z)
            TotalUsers = TotalUsers + z
            
            
    except:
        pass
print(TotalUsers)
domains.close()
   
