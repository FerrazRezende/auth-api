from jinja2 import Environment, FileSystemLoader
from settings import MAIL_PASS, MAIL_USER
from fastapi import HTTPException
import smtplib
import os




def send_email(recipient: str, reset_code: str) -> None:

    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'template')))
    template = env.get_template('mail.html')

    message_body = template.render(reset_code=reset_code)

    formatted_message = f"Subject: 'Your Password Reset Code'\nContent-Type: text/html\n\n{message_body}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MAIL_USER, MAIL_PASS)
        server.sendmail(MAIL_USER, recipient, formatted_message)
        server.quit()

    except smtplib.SMTPAuthenticationError as ex:
        raise HTTPException(status_code=403, detail="Authentication failed. Check your credentials.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")