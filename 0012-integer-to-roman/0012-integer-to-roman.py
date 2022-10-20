class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_list = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100],['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        output = ""
        for symbol, number in symbol_list:
            count = num//number
            if count:
                output += (symbol*count)
                num = num%number
        return output