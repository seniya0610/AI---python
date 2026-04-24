class calculator:
    def multiply(self, a = 1, b = 1, *arg):
        result = a * b
        for i in arg:
            result *= i
        return result
    
calc1 = calculator()
calc1.multiply(2,2,3,8)
