from abc import ABC, abstractmethod

"""
Create training by executing different set of queries each query generates a separate table.

This Processor abstract class has the common method for reading from file and than the processing 
for each query will be done by its respective child classes. That way the design is flexible to 
add more queries later.
"""
class Processor(ABC):
    def __init__(self, filepath):
        bp = open(filepath, "r")
        self.query = bp.read()
        bp.close()

    @abstractmethod
    def process(self):
        raise NotImplementedError

class FeatureXProcessor(Processor):
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def process(self):
        print('FeatureXProcessor...')
        print(self.query)

class FeatureYProcessor(Processor):
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def process(self):
        print('FeatureYProcessor...')
        print(self.query)

class FeatureZProcessor(Processor):
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def process(self):
        print('FeatureZProcessor...')
        print(self.query)


if __name__ == "__main__":
    FeatureXProcessor('featureX.sql').process()
    FeatureYProcessor('featureY.sql').process()
    FeatureZProcessor('featureZ.sql').process()