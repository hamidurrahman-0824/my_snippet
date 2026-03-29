class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients   # list

    def evaluate(self, x):
        result = 0
        for power, coef in enumerate(self.coefficients):
            result += coef * (x ** power)
        return result

    def __str__(self):
        terms = []
        for power, coef in enumerate(self.coefficients):
            if coef != 0:
                terms.append(f"{coef}x^{power}")
        return " + ".join(terms)
p = Polynomial([1,2,3])   # 1 + 2x + 3x²

print(p)
print("Value at x=2:", p.evaluate(2))
class Polynomial:

    def __init__(self,*coef):
        self.coef = coef

    def evaluate(self,x):
        return sum(c*(x**i) for i,c in enumerate(self.coef))
p = Polynomial(1,2,3)

print(p.evaluate(2))