#!/usr/bin/python3

"""Definition of a class named Base. This class will be the “base” of all other
classes in this project."""
import json
import os.path
import csv
import turtle


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation

        Args:
        id (int): object id. Defaults to none.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of
        dictionaries

        Args: list (list of dictionaries)

        Return: JSON String (Str)
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string

        Returns: Json string representation
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the JSON string representation of
        an list_objs into a file"""

        filename = "{}.json".format(cls.__name__)

        list_dicts = []

        if list_objs is not None:
            for p in range(len(list_objs)):
                list_dicts.append(list_objs[p].to_dictionary())

            lists = cls.to_json_string(list_dicts)

        with open(filename, 'w') as f:
            f.write(lists)

    @classmethod
    def create(cls, **dictionary):
        """create a new object from dictionary"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        elif cls.__name__ == "Square":
            new = cls(10, 10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        object_created = []
        with open(filename, 'r') as f:
            file_string = f.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for el in data:
                object_created.append(cls.create(**el))

        return object_created

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.
        Args:
            cls (any): class.
        Returns:
            list: list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
            list_objs (list): objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using turtle

        Args:
        list_rectangles- a list of rectangle objects to draw
        list_squares - a list of square objects to draw
        """
        ttl = turtle.Turtle()
        ttl.screen.bgcolor("#F5DEB3")
        ttl.pensize("4")
        ttl.shape("turtle")

        ttl.color("000000")
        for i in list_rectangles:
            ttl.showturtle()
            ttl.up()
            ttl.goto(i.x, i.y)
            ttl.down()
            for i in range(2):
                ttl.forward(i.width)
                ttl.left(90)
                ttl.forward(i.height)
                ttl.left(90)
            ttl.hideturtle()

        ttl.color("8B008B")
        for j in list_squares:
            ttl.showturtle()
            ttl.up()
            ttl.goto(j.x, j.y)
            ttl.down()
            for j in range(2):
                ttl.forward(j.width)
                ttl.left(120)
                ttl.forward(j.height)
                ttl.left(120)
            ttl.hideturtle()

        turtle.exitonclick()
