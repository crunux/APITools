from .models import sendMailBody


def emailTemplate(content: sendMailBody):
    return f"""
    <div style="margin: 0; padding: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; background-color: #f2f2f2;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #ffffff; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="color: #219ebc;">Hello Joan Cruz, Email Sended from crunux.me</h1>
            </div>
            <div style="padding: 20px;">
                <p>Hello, my name is {content.name}, Email: {content.email}</p>
                <p>{content.message}</p>
                <p>Say Goodbye, {content.name}</p>
                <p>Thanks!</p>
            </div>
            <div style="text-align: center; margin-top: 20px; color: #777777; font-size: 14px;">
                <p>This email was send from crunux.me to contact with you.!</p>
            </div>
        </div>
    </div>
    """
