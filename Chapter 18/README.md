## 1. What is the protocol for sending email? For checking and receiving email?

`SMTP` - sending email<br />
`IMAP` - receiving email

## 2. What four smtplib functions/methods must you call to log in to an SMTP server?

```
smtplib.SMTP()
smtplib.ehlo()
smtp.starttls()
```

## 3. What two imapclient functions/methods must you call to log in to an IMAP server?

```
imapclient.IMAPClient()
imapObj.login()
```

## 4. What kind of argument do you pass to imapObj.search() ?

We can pass IMAP search key strings in the list argument to imapObj.search()
method.<br />
These include:
* 'ALL',
* 'BEFORE _date_','ON _date_', 'SINCE _date_'
* 'SUBJECT _string_' , 'BODY _string_' , 'TEXT _string_'
* 'FROM _string_' , 'TO _string_' , 'CC _string_' , 'BCC _string_'
* 'LARGER _N_' , 'SMALLER _N_'
* 'NOT _search-key_'
* 'OR _search-key1 search-key2_'
* 'SEEN' , 'UNSEEN'
* 'ANSWERED' , 'UNANSWERED'
* 'DELETED' , 'UNDELETED'
* 'DRAFT' , 'UNDRAFT'
* 'FLAGGED' , 'UNFLAGGED'


## 5. What do you do if your code gets an error message that says got more than 10000 bytes ?

By default Python sets the size limit to 10,000 bytes. Therefore we increase the limit. We assign `imaplib._MAXLINE` to a larger value like 10000000.<br />
`imaplib._MAXLINE = 10000000`

## 6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?

The pyzmail module

## 7. When using the Gmail API, what are the credentials.json and token.json files?

The credentials.json file contains the Client ID and Client Secret information.<br />
A token.json file give your Python scripts access to the Gmail account you entered.<br />
In short, these files give access to your Gmail account.

## 8. In the Gmail API, what’s the difference between “thread” and “message” objects?

Thread and Message objects represent conversation threads and individual emails, respectively. A Thread object has a messages attribute that holds a list of Message objects.

## 9. Using ezgmail.search() , how can you find emails that have file attachments?

`ezgmail.search('has:attachment')`

## 10. What three pieces of information do you need from Twilio before you can send text messages?

1. SID number
2. Authentication token number
3. Your Twilio phone number

