class Location:
    def __init__(self, street: str, number: int, postalCode: int, place: str, province: str):
        self.__street = street
        self.__number = number
        self.__postalCode = postalCode
        self.__place = place
        self.__province = province

    def get_street(self) -> str:
        return self.__street

    def set_street(self, street: str):
        self.__street = street

    def get_number(self) -> int:
        return self.__number

    def set_number(self, number: int):
        self.__number = number

    def get_postalCode(self) -> int:
        return self.__postalCode

    def set_postalCode(self, postalCode: int):
        self.__postalCode = postalCode

    def get_place(self) -> str:
        return self.__place

    def set_place(self, place: str):
        self.__place = place

    def get_province(self) -> str:
        return self.__province

    def set_province(self, province: str):
        self.__province = province

    def __str__(self):
        return f"Location(street={self.get_street()}, number={self.get_number()}, postalCode={self.get_postalCode()}, place={self.get_place()}, province={self.get_province()})"
