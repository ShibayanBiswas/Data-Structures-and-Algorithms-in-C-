"""
01. Convert Decimal to Binary:
   - Use a helper function `decimal_to_binary` to convert the given decimal number `num` into its binary representation as a string.

02. Flip the Bits to Find the Complement:
   - Iterate through the binary string and flip each bit:
     - Convert '0' to '1' and '1' to '0'.
   - Store the flipped bits in a new string `complement`.

03. Convert Binary to Decimal:
   - Use another helper function `binary_to_decimal` to convert the complement binary string back into its decimal form.

04. Return the Result:
   - The result is the decimal equivalent of the binary complement, which is returned as the output.

Time Complexity: O(log n) because the conversion from decimal to binary and back is logarithmic in the size of the number.
Space Complexity: O(log n) due to the storage of the binary string and the complement string.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        # 01. Convert decimal to binary
        def decimal_to_binary(n: int) -> str:
            if n == 0:
                return "0"
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary

        # 03. Convert binary to decimal
        def binary_to_decimal(binary_str: str) -> int:
            decimal = 0
            binary_str = binary_str[::-1]  # Reverse the string to process from right to left
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * (2 ** i)
            return decimal

        # 02. Flip the bits to find the complement
        binary = decimal_to_binary(num)
        complement = ''
        for char in binary:
            complement += '1' if char == '0' else '0'

        # 04. Return the result (complement in decimal)
        return binary_to_decimal(complement)