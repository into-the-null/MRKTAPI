from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def returnGifts(nft_ids: list = [], authData: str = "") -> list:

    URL = API_URL + "gifts/return"

    if not authData:
        raise authDataError("MRKTAPI: returnGifts(): Error: authData is required")
    if not isinstance(nft_ids, list) or not nft_ids:
        raise tradingError("MRKTAPI: returnGifts(): Error: nft_ids must be a non-empty list")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}
    PAYLOAD = {"ids": nft_ids}

    response = await fetch(method="POST", url=URL, json=PAYLOAD, headers=HEADERS, impersonate="chrome110")
    requestExceptionHandler(response, "returnGifts")

    result = response.json()
    if not isinstance(result, list):
        raise requestError(f"MRKTAPI: returnGifts(): Error: Unexpected response: {result}")

    return result
