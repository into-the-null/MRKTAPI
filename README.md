# MRKTAPI

Библиотека для работы с MRKT - платформой для торговли NFT подарками в Telegram.

## Описание

MRKTAPI предоставляет удобный Python интерфейс для взаимодействия с API платформы Telegram Market. Библиотека позволяет искать, покупать, продавать подарки, управлять балансом.

## Установка

```bash
pip install MRKTAPI
```

## Быстрый старт

### Получение токена

Для работы с API необходимо получить токен аутентификации:

```python
import asyncio
from MRKTAPI.auth import update_auth

async def get_token():
    
    # Используя api_id и api_hash
    token = await update_auth(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH"
    )
    
    return token

    # Получаем токен
    token = asyncio.run(get_token())
    print(f"Токен получен: {token}")
```

### Основные операции

```python
import asyncio
from MRKTAPI import search, getBalance, buy, sale, getMyGifts

async def main():
    auth_data = "YOUR_TOKEN"
    
    # Получаем баланс
    balance = await getBalance(authData=auth_data)
    print(f"Баланс: {balance.hard} TON")
    
    # Ищем подарки
    gifts = await search(
        authData=auth_data,
        count=10,
        min_price=1.0,  # в TON
        max_price=10.0
    )
    
    for gift in gifts:
        print(f"Подарок: {gift.name}, Цена: {gift.price} TON")
    
    # Покупаем подарок
    if gifts:
        result = await buy(
            nft_id=gifts[0].id,
            price=gifts[0].price_nano,  # цена в нанотонах
            authData=auth_data
        )
        print("Покупка успешна!")
    
    # Получаем свои подарки
    my_gifts = await getMyGifts(authData=auth_data)
    print(f"У вас {len(my_gifts)} подарков")

asyncio.run(main())
```

## Основные функции

### Аутентификация
- `update_auth()` - получение токена для работы с API

### Баланс и торговля
- `getBalance(authData)` - получение баланса аккаунта
- `search(authData, **filters)` - поиск подарков на маркетплейсе
- `buy(nft_id, price, authData)` - покупка подарка
- `sale(nft_id, price, authData)` - выставление подарка на продажу
- `cancel(nft_ids, authData)` - отмена продажи подарков

### Управление подарками
- `getMyGifts(authData, **filters)` - получение списка своих подарков
- `giftsFloors(authData)` - получение минимальных цен коллекций
- `modelFloors(collection_name, authData)` - получение минимальных цен моделей

### Гивевеи
- `getGiveaways(giveaway_type, count, authData)` - получение списка гивевеев

### Утилиты
- `nanoToNormal(nano)` - конвертация нанотонов в TON
- `convertToNano(ton)` - конвертация TON в нанотоны
- `toShortName(name)` - сокращение названий
- `rarityPerMilleToPercent(per_mille)` - конвертация редкости

## Примеры использования

### Поиск подарков с фильтрами

```python
gifts = await search(
    authData=auth_data,
    count=20,
    collection_names=["Lol Pop"],
    model_names=["Satellite"],
    ordering="Price",
    low_to_high=True
)
```


### Получение минимальных цен

```python
# Минимальные цены всех коллекций
floors = await giftsFloors(auth_data)
print(f"Минимальная цена Collection1: {floors.floors['Collection1']} TON")

# Минимальные цены моделей в коллекции
model_floors = await modelFloors("Collection1", auth_data)
for model in model_floors.models:
    print(f"{model.name}: {model.floor_price} TON")
```


## Структуры данных

### MRKTGift
Объект подарка с полями:
- `id` - уникальный идентификатор
- `name` - название подарка
- `price` - цена в TON
- `price_nano` - цена в нанотонах
- `collection_name` - название коллекции
- `model_name` - название модели
- `backdrop_name` - название фона
- `symbol_name` - название символа
- `is_mintable` - можно ли минтить
- `is_new` - новый ли подарок

### MRKTBalance
Объект баланса с полями:
- `hard` - баланс в TON
- `hard_nano` - баланс в нанотонах


## Требования

- Python 3.8+
- asyncio
- curl_cffi
- Kurigram


## Поддержка

При возникновении проблем создавайте issue в репозитории проекта.
