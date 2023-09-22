"""
1. identity operator compares two objects and determines if they are the same based in their memory address
2. equality operator compares two objects and determines if they are the same based on their values
"""
from typing import TypeVar


T = TypeVar("T")


def compare_objects_with_identity_operator(obj1: T, obj2: T) -> bool:
    """
    Compare two objects and determine if they are the
    same based on their memory address.
    """
    return obj1 is obj2


def compare_objects_with_equality_operator(obj1: T, obj2: T) -> bool:
    """
    Compare two objects and determine if they are the
    same based on their values.
    """
    return obj1 == obj2


class Main:
    @staticmethod
    def main() -> None:
        print("Hello World!")

        result = compare_objects_with_identity_operator({"a": 1, "b": 2}, {"a": 1, "b": 2})
        print(result)

        obj = {"a": 1, "b": 2}
        obj2 = obj
        result2 = compare_objects_with_identity_operator(obj, obj2)
        print(result2)

        obj3 = {"a": 1, "b": 2}
        obj4 = {"a": 1, "b": 2}
        result3 = compare_objects_with_equality_operator(obj3, obj4)
        print(result3)

        obj5 = obj3
        print(obj5 is obj3)

        a = [1, 2, 3]
        b = a
        print(a is b)

        a.append(4)
        print(a, id(a))
        print(b, id(b))

        c = a.copy()
        print(c, id(c))


if __name__ == "__main__":
    Main.main()
