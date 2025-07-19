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
    def gift_id(self):
        return self.__dict__.get("giftId", None)

    @property
    def name(self):
        return self.__dict__.get("name", None)

    @property
    def title(self):
        return self.__dict__.get("title", None)

    @property
    def sale_price(self):
        return self.__dict__.get("salePrice", 0)

    @property
    def collection_name(self):
        return self.__dict__.get("collectionName", None)

    @property
    def model(self):
        return self.__dict__.get("modelName", None)

    @property
    def model_rarity(self):
        value = self.__dict__.get("modelRarityPerMille")
        return rarityPerMilleToPercent(value) if value is not None else None

    @property
    def symbol(self):
        return self.__dict__.get("symbolName", None)

    @property
    def symbol_rarity(self):
        value = self.__dict__.get("symbolRarityPerMille")
        return rarityPerMilleToPercent(value) if value is not None else None

    @property
    def backdrop(self):
        return self.__dict__.get("backdropName", None)

    @property
    def backdrop_rarity(self):
        value = self.__dict__.get("backdropRarityPerMille")
        return rarityPerMilleToPercent(value) if value is not None else None

    @property
    def is_on_sale(self):
        return bool(self.__dict__.get("isOnSale"))

    @property
    def is_on_auction(self):
        return bool(self.__dict__.get("isOnAuction"))

    @property
    def is_locked(self):
        return bool(self.__dict__.get("isLocked"))

    @property
    def is_mine(self):
        return bool(self.__dict__.get("isMine"))

    @property
    def is_giveaway_received(self):
        return bool(self.__dict__.get("isGiveawayReceived"))

    @property
    def is_listed(self):
        return bool(self.__dict__.get("isListed"))

    @property
    def premarket_status(self):
        return self.__dict__.get("premarketStatus", None)

    @property
    def sales_count(self):
        return self.__dict__.get("salesCount", 0)

    @property
    def tg_id(self):
        return self.__dict__.get("number", None)

    @property
    def export_date(self):
        return self.__dict__.get("exportDate", None)

    @property
    def received_date(self):
        return self.__dict__.get("receivedDate", None)

    @property
    def max_upgraded_count(self):
        return self.__dict__.get("maxUpgradedCount", 0)

    @property
    def total_upgraded_count(self):
        return self.__dict__.get("totalUpgradedCount", 0)

    @property
    def promote_end_at(self):
        return self.__dict__.get("promoteEndAt", None)

    @property
    def next_resale_date(self):
        return self.__dict__.get("nextResaleDate", None)

    @property
    def next_transfer_date(self):
        return self.__dict__.get("nextTransferDate", None)

    @property
    def unlock_date(self):
        return self.__dict__.get("unlockDate", None)

    @property
    def is_on_platform(self):
        return bool(self.__dict__.get("isOnPlatform"))

    @property
    def is_locked_for_resale(self):
        return self.is_locked or self.is_giveaway_received

    @property
    def can_be_sold(self):
        return self.is_mine and not self.is_locked_for_resale and not self.is_on_sale

    @property
    def can_be_transferred(self):
        return self.is_mine and not self.is_locked_for_resale

    @property
    def can_be_given(self):
        return self.is_mine and not self.is_locked_for_resale
    

class MRKTGiveaway:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id", None)

    @property
    def created_at(self):
        return self.__dict__.get("createdAt", None)

    @property
    def end_at(self):
        return self.__dict__.get("endAt", None)

    @property
    def ticket_price_nano(self):
        return self.__dict__.get("ticketPriceNanoTons", 0)

    @property
    def is_channel_boost_required(self):
        return bool(self.__dict__.get("isChanelBoostRequired"))

    @property
    def is_for_premium(self):
        return bool(self.__dict__.get("isForPremium"))

    @property
    def is_for_active_traders(self):
        return bool(self.__dict__.get("isForActiveTraders"))

    @property
    def channels(self):
        return self.__dict__.get("chanels", [])

    @property
    def duration(self):
        return self.__dict__.get("duration", None)

    @property
    def is_mine(self):
        return bool(self.__dict__.get("isMine"))

    @property
    def preview_gift(self):
        gift_data = self.__dict__.get("previewGift", {})
        return MRKTGift(gift_data) if gift_data else None

    @property
    def participants_count(self):
        return self.__dict__.get("participantsCount", 0)

    @property
    def my_tickets_count(self):
        return self.__dict__.get("myTicketsCount", 0)

    @property
    def validation_status(self):
        return self.__dict__.get("validationStatus", None)

    @property
    def gifts_count(self):
        return self.__dict__.get("giftsCount", 0)

    @property
    def total_tickets(self):
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
    def prize_pool_type(self):
        return self.__dict__.get("prizePoolType", None)

    @property
    def is_free(self):
        return self.ticket_price_nano == 0

    @property
    def is_paid(self):
        return self.ticket_price_nano > 0

    @property
    def is_active(self):
        from datetime import datetime
        if not self.end_at:
            return False
        try:
            end_time = datetime.fromisoformat(self.end_at.replace('Z', '+00:00'))
            return end_time > datetime.now(end_time.tzinfo)
        except:
            return False

    @property
    def can_participate(self):
        return self.is_active and self.validation_status == "Validated"


class GiftsFloors:
    def __init__(self, data: dict):
        self._data = data

    def to_dict(self):
        return self._data

    def floor(self, gift_short_name: str):
        return float(self._data.get(gift_short_name, 0.0))
    

class ModelFloors:
    def __init__(self, data: list):
        self._floors = {}
        for item in data:
            name = item.get("modelName")
            price = "floorPriceNanoTons"
            if name:
                self._floors[name] = price

    def to_dict(self):
        return self._floors

    def floor(self, model_name: str):
        return float(self._floors.get(model_name, 0.0))

    @property
    def models(self):
        return list(self._floors.keys())


class MRKTBalance:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def soft(self):
        return self.__dict__.get("soft", 0)

    @property
    def hard(self):
        return self.__dict__.get("hard", 0)

    @property
    def total_hard(self):
        return self.__dict__.get("totalHard", 0)

    @property
    def stars(self):
        return self.__dict__.get("stars", 0)

    @property
    def stars_for_withdraw(self):
        return self.__dict__.get("starsFotWithdraw", 0)

    @property
    def friends_count(self):
        return self.__dict__.get("friendsCount", 0)

    def hard_normal(self):
        """Конвертирует hard баланс из nano в USD"""
        from ..utils.functions import nanoToNormal
        return float(nanoToNormal(self.hard))

    def total_hard_normal(self):
        """Конвертирует totalHard баланс из nano в USD"""
        from ..utils.functions import nanoToNormal
        return float(nanoToNormal(self.total_hard))
