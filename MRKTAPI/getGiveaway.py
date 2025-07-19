from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def getGiveaways(
    giveaway_type: str = "Free",
    count: int = 20,
    cursor: str = "",
    token: str = ""
) -> tuple[list[MRKTGiveaway], str]:

    if not token:
        raise authDataError("MRKTAPI: getGiveaways(): Error: token is required")

    if count > 20:
        raise giftsError("MRKTAPI: getGiveaways(): Error: max count is 20")

    valid_types = ["Free", "Paid", "Mine", "Joined"]
    if giveaway_type not in valid_types:
        raise giftsError(f"MRKTAPI: getGiveaways(): Error: type must be one of {valid_types}")

    URL = API_URL + f"giveaways?type={giveaway_type}&count={count}&cursor={cursor}"
    HEADERS = {**HEADERS_MAIN, "Authorization": token}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")
    requestExceptionHandler(response, "getGiveaways")

    data = response.json()
    
    giveaways = [MRKTGiveaway(giveaway) for giveaway in data.get("items", [])]
    next_cursor = data.get("nextCursor", "")
    
    return giveaways, next_cursor 