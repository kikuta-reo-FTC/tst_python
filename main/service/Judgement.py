import variable

class Judgement:
    def checking(number):
        if isEvenNumber(number):
            return variable.EVEN
        elif number == 0:
            return variable.EXCEPTION_OF_ZERO
        else:
            return variable.ODD

class isEvenNumber:
    def checking_of_even(x):
        EVEN_NUMBER = x % 2
        if EVEN_NUMBER == 0:
            return true