import random
import json
import smtplib
from pprint import pprint



with open('/root/getpocket') as data_file:
    data = json.load(data_file)

item_dict = data
a = random.choice(item_dict['list'].keys())

fromaddr = 'jason.brunk@gmail.com'
toaddrs  = 'jason.brunk@gmail.com'
msg = "\r\n".join([
  "From: jason.brunk@gmail.com",
  "To: jason.brunk@gmail.com",
  "Subject: " + item_dict["list"][a]["resolved_title"],
  "",
  item_dict["list"][a]["excerpt"] + "\n\n\nhttps://getpocket.com/beta/read/" + a
  ])
username = 'jason.brunk@gmail.com'
password = 'Love2Stacy%^'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.encode('utf-8').strip())
server.quit()