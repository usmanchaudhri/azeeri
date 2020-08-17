"""
"""
class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_name: str) -> dict:
        pass

class PdfParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        pass

class EmailParser(InformalParserInterface):
    """ Email text from an email """
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text_from_email(self, full_file_name: str) -> dict:
        pass

# pdfParser = PdfParser()
# emailParser = EmailParser()
#
# print(isinstance(pdfParser, InformalParserInterface))
# print(isinstance(emailParser, InformalParserInterface))
#
# print(issubclass(PdfParser, InformalParserInterface))
# print(issubclass(EmailParser, InformalParserInterface))


""" 
Ideally, you would want issubclass(EmlParser, InformalParserInterface to return False when the implementing class 
doesn’t define all of the interface’s abstract methods. To do this, you’ll create a metaclass called ParserMeta. 
You’ll be overriding two dunder methods:
"""
class ParserMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__instancecheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """
    This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass

class PdfParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass

class EmailParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass
    def extract_text_from_email(self, full_file_path) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass

# print(issubclass(PdfParserNew, UpdatedInformalParserInterface))
# print(issubclass(EmailParserNew, UpdatedInformalParserInterface))
# print(PdfParserNew.__mro__)

""" Formal interfaces """
import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__ (cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

# print(issubclass(PdfParserNew, FormalParserInterface))
# print(issubclass(EmailParserNew, FormalParserInterface))

""" Using Abstract Method Declaration """
class FormalParserInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplementedError)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError

class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass
    def extract_text_from_email(self, full_file_path: str):
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

pdf_parser = PdfParserNew()
eml_parser = EmlParserNew()













