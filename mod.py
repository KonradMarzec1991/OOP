from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise AttributeError('Modulus must be an integer!')
        if not(isinstance(value, int) and value < 0):
            raise AttributeError('Value must be an positive integer!')

        self._modulus = modulus
        self._value = value % modulus

    @property
    def modulus(self):
        return self._modulus

    @property
    def value(self):
        return self._value

    def _retrieve_value(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        if isinstance(other, int):
            return other % self.modulus
        raise TypeError('Incompatible types')

    def __eq__(self, other):
        """
        If other is integer, compare residue to other
        If other is Mod instance, compare values
        """
        other_value = self._retrieve_value(other)
        return self.value == other_value

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __repr__(self):
        return f'Mod({self.value}, {self.modulus})'

    # Arithmetic operators

    def __add__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value + other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value + other, self.modulus)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value - other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value - other, self.modulus)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value * other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value * (other % self.modulus), self.modulus)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value ** other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value ** (other % self.modulus), self.modulus)
        return NotImplemented

    # In-place operators

    def __iadd__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (self.value + other.value) % self.modulus
            return self
        if isinstance(other, int):
            self._value = (self.value + other) % self.modulus
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (self.value - other.value) % self.modulus
            return self
        if isinstance(other, int):
            self._value = (self.value - other) % self.modulus
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (self.value * other.value) % self.modulus
            return self
        if isinstance(other, int):
            self._value = (self.value * other) % self.modulus
            return self
        return NotImplemented

    def __ipow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self._value = (self.value ** other.value) % self.modulus
            return self
        if isinstance(other, int):
            self._value = (self.value ** (other.value % self.modulus)) % self.modulus
            return self
        return NotImplemented