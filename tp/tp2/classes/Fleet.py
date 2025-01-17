import classes.Spaceship as Spaceship

class Fleet():
    def __init__(self, name, spaceship=None):
        self.__name = name
        self.__spaceship = spaceship if spaceship is not None else []

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _spaceship(self):
        return self.__spaceship
    
    def display_spaceship(self):
        print(f"\nLa flotte {self.__name} est composé de :")
        for Spaceship in self.__spaceship:
            print(f" - {Spaceship._name} :  {Spaceship._Type} - {Spaceship._state} - {len(Spaceship._crew)} membres")

    def append_spaceship(self, Spaceship):
        self.__spaceship.append(Spaceship)
        print(f"{Spaceship._name} a rejoint la flotte")

    def remove_spaceship(self, value):
        self.__spaceship.pop(value._name())
        print(f"{value._name} a quitté la flotte")

    def stat(self):
        nbt = 0
        nbt_O = 0
        nbt_p = 0
        nbt_t = 0
        nbt_M = 0
        nbt_xp = 0

        for Spaceship in self.__spaceship:
            for member in Spaceship._crew:
                match type(member).__name__:
                    case 'Operator':
                        nbt_xp += member._exp
                        match type(member._role).__name__:
                            case 'Pilote':
                                nbt_p += 1
                            case 'Technicien':
                                nbt_t += 1
                    case 'Mentalist':
                        nbt_M += 1

        nbt_O = nbt_p + nbt_t
        nbt = nbt_O + nbt_M
        print(f"\n Voici les Stats de la flotte {self.__name}:\n_____\nNombre de membres :\n    {nbt} \n    - {nbt_O} Operateurs\n     - {nbt_p} Pilotes\n     - {nbt_t} Techniciens\n - {nbt_M} Mentalistes\n_____\nExpérience:\n   - {nbt_xp} d'xp total\n - {nbt_xp / nbt if nbt > 0 else 0} d'xp moyenne\n")
