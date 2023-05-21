# NOTE: fastapi-codegenとopenalchemyの記法の相性の関係でbackrefが機能していない為手動設定している
# ちなみにmany-to-oneのrelationshipと外部キーはできてるっぽい（設定すると競合する）
from sqlalchemy.orm import relationship

from . import schema_gen as sg

class PatchedAffiliate(sg.Affiliate):
    purchase_rights = relationship("PatchedPurchaseRight", back_populates="affiliate")

class PatchedUser(sg.User):
    orders = relationship("PatchedOrder", back_populates="user")

class PatchedItem(sg.Item):
    pass

class PatchedOrder(sg.Order):
    order_items = relationship("PatchedOrderItem", back_populates="order")

class PatchedOrderItem(sg.OrderItem):
    pass

class PatchedPurchaseRight(sg.PurchaseRight):
    affiliate = relationship("PatchedAffiliate", back_populates="purchase_rights")

