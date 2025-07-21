from ..utils.functions import rarityPerMilleToPercent, cap

class MRKTGift:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id", None)

    @property
    def giftId(self):
        return self.__dict__.get("giftId", None)

    @property
    def name(self):
        return self.__dict__.get("name", None)

    @property
    def title(self):
        return self.__dict__.get("title", None)

    @property
    def price(self):
        return self.__dict__.get("salePrice", 0)

    @property
    def collectionName(self):
        return self.__dict__.get("collectionName", None)

    @property
    def model(self):
        return self.__dict__.get("modelName", None)

    @property
    def modelRarity(self):
        value = self.__dict__.get("modelRarityPerMille")
        return rarityPerMilleToPercent(value) if value is not None else None

    @property
    def symbol(self):
        return self.__dict__.get("symbolName", None)

    @property
    def symbolRarity(self):
        value = self.__dict__.get("symbolRarityPerMille")
        return rarityPerMilleToPercent(value) if value is not None else None

    @property
    def backdrop(self):
        return self.__dict__.get("backdropName", None)

    @property
    def backdropRarity(self):
        value = self.__dict__.get("backdropRarityPerMille")
        return rarityPerMilleToPercent(value) if value is not None else None

    @property
    def isOnSale(self):
        return bool(self.__dict__.get("isOnSale"))

    @property
    def isOnAuction(self):
        return bool(self.__dict__.get("isOnAuction"))

    @property
    def isLocked(self):
        return bool(self.__dict__.get("isLocked"))

    @property
    def isMine(self):
        return bool(self.__dict__.get("isMine"))

    @property
    def isGiveawayReceived(self):
        return bool(self.__dict__.get("isGiveawayReceived"))

    @property
    def isListed(self):
        return bool(self.__dict__.get("isListed"))

    @property
    def premarketStatus(self):
        return self.__dict__.get("premarketStatus", None)

    @property
    def salesCount(self):
        return self.__dict__.get("salesCount", 0)

    @property
    def tgId(self):
        return self.__dict__.get("number", None)

    @property
    def exportDate(self):
        return self.__dict__.get("exportDate", None)

    @property
    def unlockDate(self):
        return self.__dict__.get("unlockDate", None)
    

class MRKTGiveaway:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id", None)

    @property
    def createdAt(self):
        return self.__dict__.get("createdAt", None)

    @property
    def endAt(self):
        return self.__dict__.get("endAt", None)

    @property
    def ticketPrice(self):
        return self.__dict__.get("ticketPriceNanoTons", 0)

    @property
    def isChannelBoostRequired(self):
        return bool(self.__dict__.get("isChanelBoostRequired"))

    @property
    def isForPremium(self):
        return bool(self.__dict__.get("isForPremium"))

    @property
    def isForActiveTraders(self):
        return bool(self.__dict__.get("isForActiveTraders"))

    @property
    def channels(self):
        return self.__dict__.get("chanels", [])

    @property
    def duration(self):
        return self.__dict__.get("duration", None)

    @property
    def isMine(self):
        return bool(self.__dict__.get("isMine"))

    @property
    def previewGift(self):
        gift_data = self.__dict__.get("previewGift", {})
        return MRKTGift(gift_data) if gift_data else None

    @property
    def participantsCount(self):
        return self.__dict__.get("participantsCount", 0)

    @property
    def myTicketsCount(self):
        return self.__dict__.get("myTicketsCount", 0)

    @property
    def validationStatus(self):
        return self.__dict__.get("validationStatus", None)

    @property
    def giftsCount(self):
        return self.__dict__.get("giftsCount", 0)

    @property
    def totalTickets(self):
        return self.__dict__.get("totalTickets", 0)

    @property
    def winners(self):
        return self.__dict__.get("winners", [])

    @property
    def revenue(self):
        return self.__dict__.get("revenue", None)

    @property
    def badge(self):
        return self.__dict__.get("badge", None)

    @property
    def prizePoolType(self):
        return self.__dict__.get("prizePoolType", None)

    @property
    def isFree(self):
        return self.ticketPrice == 0

    @property
    def isPaid(self):
        return self.ticketPrice > 0

    @property
    def isActive(self):
        from datetime import datetime
        if not self.endAt:
            return False
        try:
            end_time = datetime.fromisoformat(self.endAt.replace('Z', '+00:00'))
            return end_time > datetime.now(end_time.tzinfo)
        except:
            return False

    @property
    def canParticipate(self):
        return self.isActive and self.validationStatus == "Validated"


class GiftsFloors:
    def __init__(self, data: dict):
        self._data = data

    def toDict(self):
        return self._data

    def floor(self, giftShortName: str):
        return float(self._data.get(giftShortName, 0.0))
    

class ModelFloors:
    def __init__(self, data: list):
        self._floors = {}
        for item in data:
            name = item.get("modelName")
            price = "floorPriceNanoTons"
            if name:
                self._floors[name] = price

    def toDict(self):
        return self._floors

    def floor(self, model_name: str):
        return float(self._floors.get(model_name, 0.0))

    @property
    def models(self):
        return list(self._floors.keys())
