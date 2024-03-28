from fastapi import APIRouter, HTTPException, status
from domain import sendMailBody, sendMail

router = APIRouter()


@router.post("/sendmail", tags=["sendmail"])
async def sendmail(content: sendMailBody):
    try:
        response = sendMail(content)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Mail not sent.")
    return {"message": "Mail sent", "response": response}
