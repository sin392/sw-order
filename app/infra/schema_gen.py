"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models

Base = models.Base  # type: ignore


class _UserDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: str
    first_name: str
    last_name: str
    tel: str
    created_at: str
    updated_at: str


class UserDict(_UserDictBase, total=False):
    """TypedDict for properties that are not required."""

    email: typing.Optional[str]
    affiliate: typing.Optional["AffiliateDict"]
    orders: typing.Sequence[typing.Dict[str, typing.Union[int, float, str, bool]]]


class TUser(typing.Protocol):
    """
    SQLAlchemy model protocol.

    担当者

    Attrs:
        id: ユーザID
        first_name: 名
        last_name: 姓
        tel: 電話番号
        email: メールアドレス
        created_at: 作成日
        updated_at: 更新日
        affiliate: The affiliate of the User.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[str]'
    first_name: 'sqlalchemy.Column[str]'
    last_name: 'sqlalchemy.Column[str]'
    tel: 'sqlalchemy.Column[str]'
    email: 'sqlalchemy.Column[typing.Optional[str]]'
    created_at: 'sqlalchemy.Column[datetime.datetime]'
    updated_at: 'sqlalchemy.Column[datetime.datetime]'
    affiliate: 'sqlalchemy.Column[typing.Optional["TAffiliate"]]'

    def __init__(self, id: str, first_name: str, last_name: str, tel: str, created_at: datetime.datetime, updated_at: datetime.datetime, email: typing.Optional[str] = None, affiliate: typing.Optional["TAffiliate"] = None) -> None:
        """
        Construct.

        Args:
            id: ユーザID
            first_name: 名
            last_name: 姓
            tel: 電話番号
            email: メールアドレス
            created_at: 作成日
            updated_at: 更新日
            affiliate: The affiliate of the User.

        """
        ...

    @classmethod
    def from_dict(cls, id: str, first_name: str, last_name: str, tel: str, created_at: datetime.datetime, updated_at: datetime.datetime, email: typing.Optional[str] = None, affiliate: typing.Optional["AffiliateDict"] = None) -> "TUser":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: ユーザID
            first_name: 名
            last_name: 姓
            tel: 電話番号
            email: メールアドレス
            created_at: 作成日
            updated_at: 更新日
            affiliate: The affiliate of the User.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TUser":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> UserDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


User: typing.Type[TUser] = models.User  # type: ignore


class _AffiliateDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: str
    name: str
    postcode: str
    address: str
    tel: str
    created_at: str
    updated_at: str


class AffiliateDict(_AffiliateDictBase, total=False):
    """TypedDict for properties that are not required."""

    fax: typing.Optional[str]
    email: typing.Optional[str]
    users: typing.Sequence[typing.Dict[str, typing.Union[int, float, str, bool]]]
    orders: typing.Sequence[typing.Dict[str, typing.Union[int, float, str, bool]]]


class TAffiliate(typing.Protocol):
    """
    SQLAlchemy model protocol.

    加盟組織

    Attrs:
        id: 加盟組織ID
        name: 組織名
        postcode: 郵便番号
        address: 住所
        tel: 電話番号
        fax: FAX番号
        email: メールアドレス
        created_at: 作成日
        updated_at: 更新日

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[str]'
    name: 'sqlalchemy.Column[str]'
    postcode: 'sqlalchemy.Column[str]'
    address: 'sqlalchemy.Column[str]'
    tel: 'sqlalchemy.Column[str]'
    fax: 'sqlalchemy.Column[typing.Optional[str]]'
    email: 'sqlalchemy.Column[typing.Optional[str]]'
    created_at: 'sqlalchemy.Column[datetime.datetime]'
    updated_at: 'sqlalchemy.Column[datetime.datetime]'

    def __init__(self, id: str, name: str, postcode: str, address: str, tel: str, created_at: datetime.datetime, updated_at: datetime.datetime, fax: typing.Optional[str] = None, email: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            id: 加盟組織ID
            name: 組織名
            postcode: 郵便番号
            address: 住所
            tel: 電話番号
            fax: FAX番号
            email: メールアドレス
            created_at: 作成日
            updated_at: 更新日

        """
        ...

    @classmethod
    def from_dict(cls, id: str, name: str, postcode: str, address: str, tel: str, created_at: datetime.datetime, updated_at: datetime.datetime, fax: typing.Optional[str] = None, email: typing.Optional[str] = None) -> "TAffiliate":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: 加盟組織ID
            name: 組織名
            postcode: 郵便番号
            address: 住所
            tel: 電話番号
            fax: FAX番号
            email: メールアドレス
            created_at: 作成日
            updated_at: 更新日

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TAffiliate":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> AffiliateDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Affiliate: typing.Type[TAffiliate] = models.Affiliate  # type: ignore


class _ItemDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: str
    name: str
    category: int
    type: int
    unit_price: int
    created_at: str
    updated_at: str


class ItemDict(_ItemDictBase, total=False):
    """TypedDict for properties that are not required."""

    description: typing.Optional[str]
    img_src: typing.Optional[str]
    sales_start: typing.Optional[str]
    sales_end: typing.Optional[str]


class TItem(typing.Protocol):
    """
    SQLAlchemy model protocol.

    商品

    Attrs:
        id: 商品ID
        name: 商品名
        description: 商品説明
        img_src: The img_src of the Item.
        category: カテゴリ(0:缶バッジ, -1:その他)
        type: タイプ(0:通常, 1:限定, -1:その他)
        unit_price: 単価
        sales_start: 作成日
        sales_end: 作成日
        created_at: 作成日
        updated_at: 更新日

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[str]'
    name: 'sqlalchemy.Column[str]'
    description: 'sqlalchemy.Column[typing.Optional[str]]'
    img_src: 'sqlalchemy.Column[typing.Optional[str]]'
    category: 'sqlalchemy.Column[int]'
    type: 'sqlalchemy.Column[int]'
    unit_price: 'sqlalchemy.Column[int]'
    sales_start: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    sales_end: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    created_at: 'sqlalchemy.Column[datetime.datetime]'
    updated_at: 'sqlalchemy.Column[datetime.datetime]'

    def __init__(self, id: str, name: str, category: int, type: int, unit_price: int, created_at: datetime.datetime, updated_at: datetime.datetime, description: typing.Optional[str] = None, img_src: typing.Optional[str] = None, sales_start: typing.Optional[datetime.datetime] = None, sales_end: typing.Optional[datetime.datetime] = None) -> None:
        """
        Construct.

        Args:
            id: 商品ID
            name: 商品名
            description: 商品説明
            img_src: The img_src of the Item.
            category: カテゴリ(0:缶バッジ, -1:その他)
            type: タイプ(0:通常, 1:限定, -1:その他)
            unit_price: 単価
            sales_start: 作成日
            sales_end: 作成日
            created_at: 作成日
            updated_at: 更新日

        """
        ...

    @classmethod
    def from_dict(cls, id: str, name: str, category: int, type: int, unit_price: int, created_at: datetime.datetime, updated_at: datetime.datetime, description: typing.Optional[str] = None, img_src: typing.Optional[str] = None, sales_start: typing.Optional[datetime.datetime] = None, sales_end: typing.Optional[datetime.datetime] = None) -> "TItem":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: 商品ID
            name: 商品名
            description: 商品説明
            img_src: The img_src of the Item.
            category: カテゴリ(0:缶バッジ, -1:その他)
            type: タイプ(0:通常, 1:限定, -1:その他)
            unit_price: 単価
            sales_start: 作成日
            sales_end: 作成日
            created_at: 作成日
            updated_at: 更新日

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TItem":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> ItemDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Item: typing.Type[TItem] = models.Item  # type: ignore


class _OrderDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: str
    postcode: str
    address: str
    approved_flag: bool
    created_at: str
    updated_at: str
    affiliate: "AffiliateDict"
    user: "UserDict"


class OrderDict(_OrderDictBase, total=False):
    """TypedDict for properties that are not required."""

    order_items: typing.Sequence[typing.Dict[str, typing.Union[int, float, str, bool]]]


class TOrder(typing.Protocol):
    """
    SQLAlchemy model protocol.

    注文

    Attrs:
        id: 注文ID
        postcode: 届け先郵便番号
        address: 届け先住所
        approved_flag: 承認フラグ
        created_at: 作成日
        updated_at: 更新日
        affiliate: The affiliate of the Order.
        user: The user of the Order.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[str]'
    postcode: 'sqlalchemy.Column[str]'
    address: 'sqlalchemy.Column[str]'
    approved_flag: 'sqlalchemy.Column[bool]'
    created_at: 'sqlalchemy.Column[datetime.datetime]'
    updated_at: 'sqlalchemy.Column[datetime.datetime]'
    affiliate: 'sqlalchemy.Column["TAffiliate"]'
    user: 'sqlalchemy.Column["TUser"]'

    def __init__(self, id: str, postcode: str, address: str, approved_flag: bool, created_at: datetime.datetime, updated_at: datetime.datetime, affiliate: "TAffiliate", user: "TUser") -> None:
        """
        Construct.

        Args:
            id: 注文ID
            postcode: 届け先郵便番号
            address: 届け先住所
            approved_flag: 承認フラグ
            created_at: 作成日
            updated_at: 更新日
            affiliate: The affiliate of the Order.
            user: The user of the Order.

        """
        ...

    @classmethod
    def from_dict(cls, id: str, postcode: str, address: str, approved_flag: bool, created_at: datetime.datetime, updated_at: datetime.datetime, affiliate: "AffiliateDict", user: "UserDict") -> "TOrder":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: 注文ID
            postcode: 届け先郵便番号
            address: 届け先住所
            approved_flag: 承認フラグ
            created_at: 作成日
            updated_at: 更新日
            affiliate: The affiliate of the Order.
            user: The user of the Order.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TOrder":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> OrderDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Order: typing.Type[TOrder] = models.Order  # type: ignore


class OrderItemDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: str
    quantity: int
    created_at: str
    updated_at: str
    order: "OrderDict"
    item: "ItemDict"


class TOrderItem(typing.Protocol):
    """
    SQLAlchemy model protocol.

    注文明細

    Attrs:
        id: 注文明細ID
        quantity: 個数
        created_at: 作成日
        updated_at: 更新日
        order: The order of the OrderItem.
        item: The item of the OrderItem.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[str]'
    quantity: 'sqlalchemy.Column[int]'
    created_at: 'sqlalchemy.Column[datetime.datetime]'
    updated_at: 'sqlalchemy.Column[datetime.datetime]'
    order: 'sqlalchemy.Column["TOrder"]'
    item: 'sqlalchemy.Column["TItem"]'

    def __init__(self, id: str, quantity: int, created_at: datetime.datetime, updated_at: datetime.datetime, order: "TOrder", item: "TItem") -> None:
        """
        Construct.

        Args:
            id: 注文明細ID
            quantity: 個数
            created_at: 作成日
            updated_at: 更新日
            order: The order of the OrderItem.
            item: The item of the OrderItem.

        """
        ...

    @classmethod
    def from_dict(cls, id: str, quantity: int, created_at: datetime.datetime, updated_at: datetime.datetime, order: "OrderDict", item: "ItemDict") -> "TOrderItem":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: 注文明細ID
            quantity: 個数
            created_at: 作成日
            updated_at: 更新日
            order: The order of the OrderItem.
            item: The item of the OrderItem.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TOrderItem":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> OrderItemDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


OrderItem: typing.Type[TOrderItem] = models.OrderItem  # type: ignore


class PurchaseRightDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: str
    created_at: str
    updated_at: str
    affiliate_id: str
    item_id: str


class TPurchaseRight(typing.Protocol):
    """
    SQLAlchemy model protocol.

    購入権

    Attrs:
        id: 購入権ID
        created_at: 作成日
        updated_at: 更新日
        affiliate_id: The affiliate_id of the PurchaseRight.
        item_id: The item_id of the PurchaseRight.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[str]'
    created_at: 'sqlalchemy.Column[datetime.datetime]'
    updated_at: 'sqlalchemy.Column[datetime.datetime]'
    affiliate_id: 'sqlalchemy.Column[str]'
    item_id: 'sqlalchemy.Column[str]'

    def __init__(self, id: str, created_at: datetime.datetime, updated_at: datetime.datetime, affiliate_id: str, item_id: str) -> None:
        """
        Construct.

        Args:
            id: 購入権ID
            created_at: 作成日
            updated_at: 更新日
            affiliate_id: The affiliate_id of the PurchaseRight.
            item_id: The item_id of the PurchaseRight.

        """
        ...

    @classmethod
    def from_dict(cls, id: str, created_at: datetime.datetime, updated_at: datetime.datetime, affiliate_id: str, item_id: str) -> "TPurchaseRight":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: 購入権ID
            created_at: 作成日
            updated_at: 更新日
            affiliate_id: The affiliate_id of the PurchaseRight.
            item_id: The item_id of the PurchaseRight.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TPurchaseRight":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> PurchaseRightDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


PurchaseRight: typing.Type[TPurchaseRight] = models.PurchaseRight  # type: ignore
