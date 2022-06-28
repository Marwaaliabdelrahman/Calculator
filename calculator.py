class Calculator:
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2=num2  

    def set_num1(self, num1):
        self.num1= num1

    def get_num1(self):
        return self.num1

    def set_num2(self, num2):
        self.num2= num2

    def get_num2(self):
        return self.num2

    def calc_sum(self):
        calc_sum = self.num1 + self.num2
        return calc_sum

    def calc_div(self):
        calc_div = self.num1 / self.num2
        return calc_div
    
    def calc_multi(self):
        calc_multi = self.num1 * self.num2
        return calc_multi
    def calc_sub(self):
        calc_sub = self.num1 - self.num2
        return calc_sub

calc = Calculator(10, 5)


print(calc.calc_sum())
print(calc.calc_multi())
print(calc.calc_div())
print(calc.calc_sub())