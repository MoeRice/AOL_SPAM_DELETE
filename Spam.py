import imaplib

user = 'YOUREMAIL@AOL.COM'
password = 'ONETIMEPASSWORD'
imap_url = 'imap.aol.com'

con = imaplib.IMAP4_SSL(imap_url) #SSL connection
con.login(user, password)
con.select('"Bulk Mail"') #name of folder Ex. Inbox

typ, msg = con.search(None, 'All') #search all inbox
print(msg)
Email = msg[0].split()
print (Email)
while Email:
        for num in Email:
                try:
                        con.store(num, '+FLAGS', '\\Deleted')
                        typ, msg = con.search(None, 'All')
                        Email = msg[0].split()
                        print (Email)
                except:
                        pass
print('Done')
con.expunge()
