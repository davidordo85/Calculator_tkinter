class RomanNumber():
    __symbols = {'M': 1000,
          'CM': 900,
          'D': 500,
          'CD': 400,
          'C': 100,
          'XC': 400,
          'L': 50,
          'XL': 40,
          'X': 10,
          'IX': 9,
          'V': 5,
          'IV': 4,
          'I': 1,
    }

    def __init__(self, value):
        if isinstance(value, str) and value.isdigit() == False:
            self.valor = self.roman_number_to_integer(value)
            if self.valor == 'Format error':
                self.rValor = self.valor
            else:
                self.rValor = str(self.valor)
        else:
            self.valor = int(value)
            self.rValor = self.integer_to_roman_number()
            if self.rValor == 'Overflow':
                self.valor = self.rValor


    def roman_number_to_integer(self, roman_number):
        if roman_number == '':
            return 'Format error'

        integer = 0
        repeated_number = 1
        previous_letter = ''
        was_subtraction = False
        for letter in roman_number:

            if letter in self.__symbols:
                if previous_letter == '' or self.__symbols[previous_letter] >= self.__symbols[letter]:
                    integer += self.__symbols[letter]
                    was_subtraction = False
                else:
                    if previous_letter + letter in self.__symbols.keys() and repeated_number < 2 and not was_subtraction:
                        integer = integer - self.__symbols[previous_letter] * 2 + self.__symbols[letter]
                        was_subtraction = True
                    else:
                        return 'Format error'
            else:
                return 'Format error'

            if letter == previous_letter and repeated_number == 3:
                return 'Format error'
            elif letter == previous_letter:
                repeated_number += 1
            else:
                repeated_number = 1
            
            previous_letter = letter

        return integer

    def integer_to_roman_number(self):
        if self.valor > 3999 or self.valor < 1:
            return 'Overflow'
        components = self.__discompose(self.valor)
        res = ''        
        for value in components:
            while value > 0:
                k, v = self.__find_less_than_or_equal_value(value)
                value -= v
                res += k
        return res

    def __find_less_than_or_equal_value(self, v):
        for key, value in self.__symbols.items():
            if value <= v:
                return key, value

    def __discompose(self, number):
        res = []
        for order in range(3, 0, -1):
            rest = number % 10 ** order
            res.append(number - rest)
            number = rest
        res.append(number)
        return res

    def __str__(self):
        return self.rValor

    def __repr__(self):
        return self.rValor


    def __add__(self, other):
        #       I,    III
        if isinstance(other, int):
            addiction = self.valor + other
        else:
            addiction = self.valor + other.valor
        result = RomanNumber(addiction)
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            subtraction = self.valor + other
        else:
            subtraction = self.valor + other.valor
        result = RomanNumber(subtraction)
        return result

    def __rsub__(self, other):
        return self.sub(other)

    def __eq__(self, other):
        return self.valor == other.valor
     
