from pydantic import BaseModel


class sendMailBody(BaseModel):
    message: str
    email: str
    name: str
