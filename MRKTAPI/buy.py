from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def buy(nft_id: str = "", price: int = 0, authData: str = "") -> dict:
    URL = API_URL + "gifts/buy"

    if authData == "":
        raise authDataError("MRKTAPI: buy(): Error: authData is required")
    if not nft_id:
        raise tradingError("MRKTAPI: buy(): Error: nft_id is required")
    if not isinstance(price, int) or price <= 0:
        raise tradingError("MRKTAPI: buy(): Error: price error")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    PAYLOAD = {
        "ids": [nft_id],
        "prices": {
            nft_id: price
        }
    }

    response = await fetch(method="POST", url=URL, json=PAYLOAD, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "buy")
    
    result = response.json()
    
    if not result or not isinstance(result, list) or len(result) == 0:
        # Проверяем баланс для диагностики
        try:
            from .balance import getBalance
            balance = await getBalance(authData)
            hard_balance = balance.hard
            
            if hard_balance < price:
                raise tradingError(f"MRKTAPI: buy(): Error: Insufficient funds. Balance: {hard_balance} nano, Required: {price} nano")
        except Exception:
            pass
        
        raise tradingError("MRKTAPI: buy(): Error: Purchase failed - empty response")
    
    gift_data = result[0]
    if not gift_data.get("type") == "gift" or not gift_data.get("userGift"):
        raise tradingError("MRKTAPI: buy(): Error: Purchase failed - invalid response format")
    
    user_gift = gift_data.get("userGift", {})
    if not user_gift.get("isMine"):
        raise tradingError("MRKTAPI: buy(): Error: Purchase failed - gift not owned")

    return result
