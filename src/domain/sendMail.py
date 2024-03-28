import os
import resend
from .models import sendMailBody
from .emailTemplate import emailTemplate


RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
EMAILTO = os.environ.get('TOSENDEMAIL')

resend.api_key = RESEND_API_KEY


def sendMail(content: sendMailBody):
    params = {
        "from": "Info Crunux <onboarding@resend.dev>",
        "to": EMAILTO,
        "subject": f"{content.name} want contact with you.!",
        "html": emailTemplate(content),
    }

    email = resend.Emails.send(params)
    return email
