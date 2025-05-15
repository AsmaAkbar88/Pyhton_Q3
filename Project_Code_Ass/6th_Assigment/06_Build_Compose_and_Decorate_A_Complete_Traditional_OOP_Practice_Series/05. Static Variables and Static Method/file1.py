class MathUtils:
    sum = 0  

    @classmethod
    def sum_add_fun(cls, add_num1, add_num2):
        cls.sum += add_num1 + add_num2  # Add to total sum


MathUtils.sum_add_fun(5, 6)


print("Total Sum is:", MathUtils.sum)

# OUTOUT:  Total Sum is: 11
# ______________________________________________________________________________
