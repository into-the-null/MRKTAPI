from .utils.other import API_URL, HEADERS_MAIN
from .classes.Objects import ModelFloors
from .classes.Exceptions import authDataError, floorsError
from .handlers import fetch, requestExceptionHandler

async def modelFloors(collection_name: str = "", authData: str = "") -> ModelFloors:
    URL = API_URL + "gifts/models"

    if not authData:
        raise authDataError("MRKT API: modelFloors(): Error: authData is required")
    if not collection_name or not isinstance(collection_name, str):
        raise floorsError("MRKT API: modelFloors(): Error: collection_name is required and must be a string")

    payload = {"collections": [collection_name]}
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="POST", url=URL, headers=HEADERS, json=payload, impersonate="chrome110")
    requestExceptionHandler(response, "modelFloors")

    data = response.json()
    return ModelFloors(data)