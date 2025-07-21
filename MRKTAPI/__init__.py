"""
MRKTAPI - Библиотека для работы с Telegram Market API

Библиотека предоставляет удобный интерфейс для взаимодействия с API
платформы Telegram Market (MRKT) для торговли NFT подарками.

Основные возможности:
- Поиск и покупка подарков
- Управление своими подарками
- Получение баланса
- Конвертация цен

Пример использования:
    import asyncio
    from MRKTAPI.search import search
    from MRKTAPI.balance import getBalance
    
    async def main():
        balance = await getBalance(authData="")
        gifts = await search(authData="", count=10)
        
    asyncio.run(main())
"""

# Основные функции
from .search import search
from .buy import buy
from .sale import sale
from .cancel import cancel
from .myGifts import getMyGifts
from .getGiveaway import getGiveaways
from .balance import getBalance
from .giftsFloors import giftsFloors
from .modelFloors import modelFloors
from .return_gift import returnGifts

# Классы объектов
from .classes.Objects import (
    MRKTGift,
    GiftsFloors,
    ModelFloors
)

# Исключения
from .classes.Exceptions import (
    authDataError,
    accountError,
    requestError,
    connectionError,
    floorsError,
    giftsError,
    tradingError
)

# Утилиты
from .utils.functions import (
    rarityPerMilleToPercent,
    cap
)

__all__ = [
    # Основные функции
    "search",
    "buy", 
    "sale",
    "cancel",
    "getMyGifts",
    "getGiveaways",
    "getBalance",
    "giftsFloors",
    "modelFloors",
    "returnGifts",
    
    # Классы объектов
    "MRKTGift",
    "GiftsFloors",
    "ModelFloors",
    
    # Исключения
    "authDataError",
    "accountError", 
    "requestError",
    "connectionError",
    "floorsError",
    "giftsError",
    "tradingError",
    
    # Утилиты
    "rarityPerMilleToPercent",
    "cap"
] 