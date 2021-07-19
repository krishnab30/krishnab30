import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'krishnabalasubramanian24@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('We know Python yeaaahh!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('krishnareigns14@gmail.com', 'romanreigns14')
  smtp.send_message(email)
  print('all good boss!')



