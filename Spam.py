import imaplib

user = 'YOUREMAIL@AOL.COM'
password = 'ONETIMEPASSWORD'
imap_url = 'imap.aol.com'

con = imaplib.IMAP4_SSL(imap_url) #SSL connection
con.login(user, password)
con.select("Bulk Mail") #Spam Folder

typ, msg = con.search(None, 'All')
print(msg[0])
for num in msg[0].split():
        con.store(num, '+FLAGS', '\\Deleted $Junk')
        

con.expunge()

