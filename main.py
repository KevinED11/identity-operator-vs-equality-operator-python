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


class SillyString(str):
    # This method gets called when using == on the object
    def __eq__(self, other: str) -> bool:
        print(f"Comparing {self} to {other}")
        # Return True if self and other have the same length
        return len(self) == len(other)


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

        print("hello world" == "world hello")
        print("hello world" == SillyString("world hello"))
        print(SillyString("world hello").__eq__("hello world"))
        print("hello world".__eq__(SillyString("hello world")))




if __name__ == "__main__":
    Main.main()
