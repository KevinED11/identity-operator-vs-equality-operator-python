def compare_objects(obj1: dict, obj2: dict) -> bool:
    return obj1 is obj2


class Main(object):
    @staticmethod
    def main() -> None:
        print("Hello World!")

        result = compare_objects({"a": 1, "b": 2}, {"a": 1, "b": 2})
        print(result)


if __name__ == "__main__":
    Main.main()
