"""
object to
"""
import pickle

class TransactionAttributeStore:
    def __init__(self):
        self.store = {'a': 1}

    def addAttribute(self, key, value):
        assert key is not None, ("key is None")
        self.store[key] = value


class Transaction:
    def __init__(self, attribute_store: TransactionAttributeStore):
        self.attributeStore = attribute_store


class DivisionTransaction:
    def __init__(self, attribute_store: TransactionAttributeStore):
        self.attributeStore = attribute_store


class ProductTransaction:
    def __init__(self, attribute_store: TransactionAttributeStore):
        self.attributeStore = attribute_store


if __name__ == "__main__":
    txnStore = TransactionAttributeStore()
    print(txnStore.store)
    txnStore.addAttribute('b', 2)
    print(txnStore.store)
    txnStore.addAttribute('c', 3)
