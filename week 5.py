class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        x = self.numerator * other.denominator + self.denominator * other.numerator
        y = self.denominator * other.denominator
        return self.__str__() + ' + ' + other.__str__() + ' = ' + Fraction(x, y).__str__()

    def __sub__(self, other):
        x = self.numerator * other.denominator - self.denominator * other.numerator
        y = self.denominator * other.denominator
        return self.__str__() + ' - ' + other.__str__() + ' = ' + Fraction(x, y).__str__()

    def inverse(self):
        return 'reverse of ' + self.__str__() + ' is ' + Fraction(self.denominator, self.numerator).__str__()


print(Fraction(3,4))
print(Fraction(1,2) + Fraction(1,4))
print(Fraction(1,2) - Fraction(1,4))
print(Fraction(4,5).inverse())