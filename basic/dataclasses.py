from dataclasses import dataclass, field, InitVar
import typing
import uuid

@dataclass
class Customer(object):
    database: InitVar[typing.Any]
    id: int
    name: str
    address: str

    def __post_init__(self, databse):
        self.address = self.address.capitalize()
        self._connection = databse.connect()

@dataclass(frozen=True, order=True)
class Customer(object):
    processing_time: typing.ClassVar[int]   # this will be a class level attribute will never be set as a field

    # id: uuid.UUID = field(default=False)
    id: uuid.UUID = field(compare=False, default_factory=uuid.uuid4, init=False)
    value: float = field(compare=True)
    product: str = field(compare=False)

    # NOTE - this would raise an error because of the class is declared frozen (immutable)
    def __post_init__(self):
        self.product = self.product.capitalize()

# applying the Hash Flag to Mutable Types
@dataclass(hash=True)
class CustomrOne(object):
    id: int
    name: str
    address: str

@dataclass(frozen=True)
class CustomerOrder(object):
    id: int
    value: float
    product: str