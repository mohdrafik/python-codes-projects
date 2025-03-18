class BinaryNumber:
    """Overloading &, |, and ^ in a Custom Class"""
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        """Overloads & operator"""
        return BinaryNumber(self.value & other.value)

    def __or__(self, other):
        """Overloads | operator"""
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other):
        """Overloads ^ operator"""
        return BinaryNumber(self.value ^ other.value)

    def __str__(self):
        """Returns the binary representation of the number"""
        return f"{self.value} (Binary: {bin(self.value)})"

#  Creating two BinaryNumber objects
num1 = BinaryNumber(5)  # 0b0101
num2 = BinaryNumber(3)  # 0b0011

#  Performing bitwise operations
and_result = num1 & num2  # Calls __and__()
or_result = num1 | num2   # Calls __or__()
xor_result = num1 ^ num2  # Calls __xor__()

#  Printing results
print("Bitwise AND:", and_result)
print("Bitwise OR:", or_result)
print("Bitwise XOR:", xor_result)
