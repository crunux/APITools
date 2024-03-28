from fastapi import FastAPI
import uvicorn

import routers.router_sendmail as router_sendmail

app = FastAPI(title="API Tools - Crunux",
              description="API to use kinds different endpoints for personal used", version="0.0.1")

app.include_router(router_sendmail.router, prefix="/api/v1")


@app.get("/")
async def read_root():
    return {"api_status": "working"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
