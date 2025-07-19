from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def cancel(nft_ids: list = None, authData: str = "") -> dict:


    URL = API_URL + "gifts/sale/cancel"

    if authData == "":
        raise authDataError("MRKTAPI: cancel(): Error: authData is required")
    if not nft_ids or not isinstance(nft_ids, list) or len(nft_ids) == 0:
        raise tradingError("MRKTAPI: cancel(): Error: nft_ids is required and must be a non-empty list")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    PAYLOAD = {
        "ids": nft_ids
    }

    response = await fetch(method="POST", url=URL, json=PAYLOAD, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "cancel")

    return response.json() 