import operator
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
        """Retrieves residue of other object"""
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        if isinstance(other, int):
            return other % self.modulus
        raise TypeError('Incompatible types')

    def _perform_operation(self, other, op, *, in_place=False):
        other_value = self._retrieve_value(other)
        modified_value = op(self.value, other_value)
        if in_place:
            self._value = modified_value % self.modulus
            return self
        else:
            return Mod(modified_value, self.modulus)

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
        return self._perform_operation(other, operator.add)

    def __sub__(self, other):
        return self._perform_operation(other, operator.sub)

    def __mul__(self, other):
        return self._perform_operation(other, operator.mul)

    def __pow__(self, other):
        return self._perform_operation(other, operator.pow)

    # In-place operators

    def __iadd__(self, other):
        return self._perform_operation(other, operator.add, in_place=True)

    def __isub__(self, other):
        return self._perform_operation(other, operator.sub, in_place=True)

    def __imul__(self, other):
        return self._perform_operation(other, operator.mul, in_place=True)

    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)
