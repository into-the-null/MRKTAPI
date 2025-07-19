from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def getMyGifts(
    count=20,
    cursor="",
    collection_names=None,
    model_names=None,
    backdrop_names=None,
    symbol_names=None,
    min_price=None,
    max_price=None,
    mintable=None,
    number=None,
    ordering="Price",
    low_to_high=True,
    is_new=None,
    is_premarket=None,
    query=None,
    is_listed=False,
    authData=""
) -> list[MRKTGift]:

    if not authData:
        raise authDataError("MRKTAPI: getMyGifts(): Error: authData is required")

    if count > 20:
        raise giftsError("MRKTAPI: getMyGifts(): Error: max count is 20")

    def check_and_list(val, name):
        if val is None:
            return []
        if isinstance(val, str):
            return [val]
        if isinstance(val, list):
            return val
        raise giftsError(f"MRKTAPI: getMyGifts(): Error: {name} must be a string or list, got {type(val).__name__}")

    collection_names = check_and_list(collection_names, "collection_names")
    model_names = check_and_list(model_names, "model_names")
    backdrop_names = check_and_list(backdrop_names, "backdrop_names")
    symbol_names = check_and_list(symbol_names, "symbol_names")

    json_data = {
        "isListed": is_listed,
        "count": count,
        "cursor": cursor,
        "collectionNames": collection_names,
        "modelNames": model_names,
        "backdropNames": backdrop_names,
        "symbolNames": symbol_names,
        "minPrice": min_price,
        "maxPrice": max_price,
        "mintable": mintable,
        "number": number,
        "isNew": is_new,
        "isPremarket": is_premarket,
        "ordering": ordering,
        "lowToHigh": low_to_high,
        "query": query
    }

    URL = API_URL + "gifts"
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="POST", url=URL, headers=HEADERS, json=json_data, impersonate="chrome110")
    requestExceptionHandler(response, "getMyGifts")

    return [MRKTGift(gift) for gift in response.json().get("gifts", [])]