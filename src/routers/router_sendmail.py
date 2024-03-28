from fastapi import APIRouter, HTTPException, status
from domain import sendMailBody, sendMail


router = APIRouter()


@router.post("/sendmail", tags=["sendmail"])
async def sendmail(content: sendMailBody):
    print(content, "1")
    try:
        response = sendMail(content)
        print(content, "2")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Mail not sent {e}")
    return {"message": "Mail sent", "response": response}
