from app.models import *
from fastapi.responses import JSONResponse


def do_get_users(**kwargs):
    return JSONResponse([{'name': 'yamada taro'}])
