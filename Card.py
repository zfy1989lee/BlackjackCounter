class Card:
    def __init__(self, value):
        self._value = value
        self._count = 2
        if self._value in ['10', 'J', 'Q', 'K', 'A']:
            self._count = -1
        elif self._value in ['7', '8', '9']:
            self._count = 0
        elif self._value in ['2', '3', '4', '5', '6']:
            self._count = 1
            
    def get_value(self):
        return self._value

    def get_count(self):
        return self._count