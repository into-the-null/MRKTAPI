"""
MRKTAPI - Библиотека для работы с Telegram Market API

Библиотека предоставляет удобный интерфейс для взаимодействия с API
платформы Telegram Market (TGMKT) для торговли NFT подарками.

Основные возможности:
- Поиск и покупка подарков
- Управление своими подарками
- Работа с гивевеями
- Получение баланса
- Конвертация цен

Пример использования:
    import asyncio
    from MRKTAPI.search import search
    from MRKTAPI.balance import getBalance
    
    async def main():
        balance = await getBalance(authData="Bearer YOUR_TOKEN")
        gifts = await search(token="Bearer YOUR_TOKEN", count=10)
        
    asyncio.run(main())
"""

__version__ = "1.0.0"
__author__ = "MRKTAPI Developer"
__description__ = "Библиотека для работы с Telegram Market API"

# Основные функции
from .search import search
from .buy import buy
from .sale import sale
from .cancel import cancel
from .myGifts import getMyGifts
from .createGiveaway import createGiveaway
from .getGiveaway import getGiveaways
from .balance import getBalance

# Классы объектов
from .classes.Objects import (
    MRKTGift,
    MRKTGiveaway,
    MRKTBalance,
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
    nanoToNormal,
    convertToNano,
    toShortName,
    rarityPerMilleToPercent,
    cap,
    listToURL
)

__all__ = [
    # Основные функции
    "search",
    "buy", 
    "sale",
    "cancel",
    "getMyGifts",
    "createGiveaway",
    "getGiveaways",
    "getBalance",
    
    # Классы объектов
    "MRKTGift",
    "MRKTGiveaway", 
    "MRKTBalance",
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
    "nanoToNormal",
    "convertToNano",
    "toShortName",
    "rarityPerMilleToPercent",
    "cap",
    "listToURL"
] 