class Department:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def __str__(self):
        return f"Department(id={self.__id}, name={self.__name})"