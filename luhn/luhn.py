class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        self.length = len(self.card_num)
        self.part = self.length % 2
        self.result = 0

    def valid(self):
        if not self.card_num.isdigit() or self.length <= 1:
            return False
        else:
            for i in range(0, self.length):
                number = int(self.card_num[i])
                if i % 2 == self.part:
                    number *= 2
                    if number > 9:
                        number -= 9
                self.result += number
            return self.result % 10 == 0
