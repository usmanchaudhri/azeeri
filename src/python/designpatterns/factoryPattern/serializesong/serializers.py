"""
A factory design pattern is use to create a concrete implementation of a common interface.

It separates the process of creating an object from the code that depends on the interface
of the object

For example an application requires an object with a specific interface to perform its tasks.
The concrete implementation of the interfaces is identified by some parameter.

Instead of using a complex if/elif/else conditional structure to determine the concrete implementation,
the application delegates that decision to a separate component that creates the concrete object.
With this approach, the application code is simplified, making it more reusable and easier to maintain.
"""

"""
Imagine an application that needs to convert a Song object into its string representation using a specified format. 
Converting an object to a different representation is often called serializing. You’ll often see these requirements 
implemented in a single function or method that contains all the logic and implementation, like in the following code:
"""
import json
import xml.etree.ElementTree as et

class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)

class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')\

import yaml

class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)

class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

class SerializerFactory:
    """
    This class has the rules about what serialization implementation to invoke
    based on some input passed-in as method parameter
    """
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
factory.register_format('YAML', YamlSerializer)

from python.designpatterns.factoryPattern.serializesong.songs import Song

if __name__ == "__main__":
    song = Song('1','Teray darya ka', 'Khalil')
    serializer = ObjectSerializer()
    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))
