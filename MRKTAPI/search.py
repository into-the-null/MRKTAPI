from .utils.other import API_URL, HEADERS_MAIN, SORTS
from .classes.Objects import MRKTGift
from .classes.Exceptions import authDataError, giftsError
from .handlers import fetch, requestExceptionHandler
from .utils.functions import convertToNano
from urllib.parse import quote_plus

async def search(
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
    ordering="None",
    low_to_high=False,
    is_premarket=False,
    query=None,
    token="",
    promoted_first=False
) -> list[MRKTGift]:


    if not token:
        raise authDataError("MRKT API: search(): Error: token is required")

    if count > 20:
        raise giftsError("MRKT API: search(): Error: max count is 20")

    # Проверка типов фильтров
    def check_and_list(val, name):
        if val is None:
            return []
        if isinstance(val, str):
            return [val]
        if isinstance(val, list):
            return val
        raise giftsError(f"MRKT API: search(): Error: {name} must be a string or list, got {type(val).__name__}")

    collection_names = check_and_list(collection_names, "collection_names")
    model_names = check_and_list(model_names, "model_names")
    backdrop_names = check_and_list(backdrop_names, "backdrop_names")
    symbol_names = check_and_list(symbol_names, "symbol_names")


    min_price_nano = convertToNano(min_price) if min_price is not None else None
    max_price_nano = convertToNano(max_price) if max_price is not None else None

    json_data = {
        "count": count,
        "cursor": cursor,
        "collectionNames": collection_names,
        "modelNames": model_names,
        "backdropNames": backdrop_names,
        "symbolNames": symbol_names,
        "minPrice": min_price_nano,
        "maxPrice": max_price_nano,
        "mintable": mintable,
        "number": number,
        "ordering": ordering,
        "lowToHigh": low_to_high,
        "isPremarket": is_premarket,
        "query": query,
        "promotedFirst": promoted_first
    }

    URL = API_URL + "gifts/saling"
    HEADERS = {**HEADERS_MAIN, "Authorization": token}

    response = await fetch(method="POST", url=URL, headers=HEADERS, json=json_data, impersonate="chrome110")
    requestExceptionHandler(response, "search")

    return [MRKTGift(gift) for gift in response.json().get("gifts", [])]
