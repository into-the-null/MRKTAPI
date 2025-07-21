from .utils.other import API_URL, HEADERS_MAIN
from .classes.Objects import GiftsFloors
from .classes.Exceptions import authDataError, giftsError
from .handlers import fetch, requestExceptionHandler


async def giftsFloors(authData: str = "") -> GiftsFloors:

    URL = API_URL + "gifts/collections"

    if authData == "":
        raise authDataError("MRKT API: giftsFloors(): Error: authData is required")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "giftsFloors")

    data = response.json()

    floors_dict = {
        gift["name"]: gift["floorPriceNanoTons"]
        for gift in data
    }

    return GiftsFloors(floors_dict)