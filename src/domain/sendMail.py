import os
import resend
from .models import sendMailBody

resend.api_key = os.environ.get('RESEND_API_KEY')
EMAILTO = os.environ.get('TOSENDEMAIL')


def sendMail(content: sendMailBody):
    print(EMAILTO, os.environ.get('RESEND_API_KEY'))
    params = {
        "from": " Info Crunux <onboarding@resend.dev>",
        "to": EMAILTO,
        "subject": "Probando envio de email",
        "html": f"<strong>Probando envio de email</strong> <p>{content.message}</p>",
    }

    email = resend.Emails.send(params)
    print(email)
    return email
