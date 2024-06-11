from fastapi import APIRouter
import os
import pwd

from dbs_assignment.config import settings

router = APIRouter()


@router.get("/v1/hello")
async def hello():
    return {
        'hello': settings.NAME
    }


@router.get("/v1/whoami")
async def whoami():
    return {
        'login': pwd.getpwuid(os.geteuid()).pw_name
    }
