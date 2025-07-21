from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def getBalance(authData: str = "") -> int:
    URL_BALANCE = API_URL + "balance"
    HEADER_AUTH = {**HEADERS_MAIN, "Authorization": authData}

    if not authData:
        print("MRKTAPI: getBalance(): Error: authData is required")
        raise authDataError("MRKTAPI: getBalance(): Error: authData is required")

    try:
        response = await fetch(method="GET", url=URL_BALANCE, headers=HEADER_AUTH, impersonate="chrome110")
        requestExceptionHandler(response, "getBalance")
        result = response.json()
    except Exception as e:
        print(f"MRKTAPI: getBalance(): Exception: {e}")
        raise

    if "error" in result:
        raise accountError(f"MRKTAPI: getBalance(): Error: {result['error']}")

    hard = result.get("hard")
    if hard is None:
        print("MRKTAPI: getBalance(): Error: 'hard' not found in response")
        raise accountError("MRKTAPI: getBalance(): Error: 'hard' not found in response")

    return hard 