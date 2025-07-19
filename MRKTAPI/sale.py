from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def sale(nft_id: str = "", price: int = 0, authData: str = "") -> dict:

    URL = API_URL + "gifts/sale"

    if authData == "":
        raise authDataError("MRKTAPI: sale(): Error: authData is required")
    if not nft_id:
        raise tradingError("MRKTAPI: sale(): Error: nft_id is required")
    if not isinstance(price, int) or price <= 0:
        raise tradingError("MRKTAPI: sale(): Error: price error")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    PAYLOAD = {
        "Ids": [nft_id],
        "price": price
    }

    response = await fetch(method="POST", url=URL, json=PAYLOAD, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "sale")

    return response.json() 