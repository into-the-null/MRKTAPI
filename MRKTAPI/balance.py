from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def getBalance(authData: str = "") -> MRKTBalance:

    URL = API_URL + "balance"

    if authData == "":
        raise authDataError("MRKTAPI: getBalance(): Error: authData is required")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "getBalance")
    
    result = response.json()
    

    if "error" in result:
        raise accountError(f"MRKTAPI: getBalance(): Error: {result['error']}")
    
    return MRKTBalance(result) 