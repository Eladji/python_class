import Pilote, Technicien
class Ship:
    def __init__(self, name, Type, crew = [], state = "operational"):
        self.__name = name
        self.__Type = Type
        self.__crew.list = crew
        self.__state = state

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _Type(self):
        return self.__Type

    @_Type.setter
    def _Type(self, value):
        self.__Type = value

    @property
    def _crew(self):
        return self.__crew

    @property
    def _state(self):
        return self.__state

    @_state.setter
    def _state(self, value):
        self.__state = value

    def append_member(self, Member):
        if self.__crew.size <= 10:
            self.__crew.append(Member)
            print(f"{Member._first_name()} {Member._last_name()} a rejoint l'équipage")
        else:
            print("impossible d'ajouter de nouveau membre a l'équipage")

    def remove_member(self, Member):
        if Member:
            self.__crew.pop(Member._first_name())
        else:
            print("le membre que vous essayer d'enlever est invalide")
    def check_preparation(self):
        check = []
        for i in self.__crew:
            if i._role() == Pilote:
                check[0] = True
            if i._role() == Technicien:
                check[1] = True
        return check[0] and check[1] == True
    def display_crew(self):
        for i in self.__crew:
            print(f"{i._first_name()} {i._last_name()} {i._role()}\n")