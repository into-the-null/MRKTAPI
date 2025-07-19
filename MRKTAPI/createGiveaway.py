from .classes.Objects import *
from .classes.Exceptions import *
from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler

async def createGiveaway(
    gifts: list = None,
    preview_gift: str = "",
    duration: str = "",
    is_private: bool = True,
    ticket_price_nano: int = 0,
    is_channel_boost_required: bool = True,
    is_for_premium: bool = True,
    is_for_active_traders: bool = False,
    channels: list = None,
    prize_pool_type: int = 0,
    authData: str = ""
) -> MRKTGiveaway:

    URL = API_URL + "giveaways/create"

    if authData == "":
        raise authDataError("MRKTAPI: createGiveaway(): Error: authData is required")
    if not gifts or not isinstance(gifts, list) or len(gifts) == 0:
        raise tradingError("MRKTAPI: createGiveaway(): Error: gifts is required and must be a non-empty list")
    if not preview_gift:
        raise tradingError("MRKTAPI: createGiveaway(): Error: preview_gift is required")
    if not channels or not isinstance(channels, list):
        raise tradingError("MRKTAPI: createGiveaway(): Error: channels is required and must be a non-empty list")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    PAYLOAD = {
        "isPrivate": is_private,
        "ticketPriceNanoTons": ticket_price_nano,
        "isChanelBoostRequired": is_channel_boost_required,
        "isForPremium": is_for_premium,
        "isForActiveTraders": is_for_active_traders,
        "chanels": channels,
        "gifts": gifts,
        "previewGift": preview_gift,
        "duration": duration,
        "prizePoolType": prize_pool_type
    }

    response = await fetch(method="POST", url=URL, json=PAYLOAD, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "createGiveaway")

    result = response.json()
    
    if not result.get("isOk"):
        errors = []
        if result.get("isWrongDuration"):
            errors.append("неправильная длительность")
        if result.get("isWrongGiftsCount"):
            errors.append("неправильное количество подарков")
        if result.get("isWrorngPrice"):
            errors.append("неправильная цена билета")
        if result.get("wrongChanels"):
            errors.append(f"неправильные каналы: {result.get('wrongChanels')}")
        
        error_msg = ", ".join(errors) if errors else "неизвестная ошибка"
        raise tradingError(f"MRKTAPI: createGiveaway(): Error: {error_msg}")

    # Получаем созданный гивевей
    giveaway_id = result.get("giveawayId") or result.get("id")
    if giveaway_id:
        # Получаем полную информацию о созданном гивевее
        from .getGiveaway import getGiveaways
        my_giveaways, _ = await getGiveaways(
            giveaway_type="Mine",
            count=1,
            token=authData
        )
        
        # Ищем созданный гивевей
        for giveaway in my_giveaways:
            if giveaway.id == giveaway_id:
                return giveaway
    
    # Если не удалось получить объект, возвращаем сырые данные
    return result
