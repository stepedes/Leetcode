class Solution:
    def findCombinations(self, combinations, digits, previous, index, mapping):
        if index == len(digits):
            combinations.append(previous)
            return
        letters = mapping[int(digits[index])]
        for i in range(0, len(letters)):
            self.findCombinations(combinations, digits, previous + letters[i], index+1, mapping)
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        combinations = []
        if digits is None or len(digits) == 0:
            return combinations
        self.findCombinations(combinations, digits, "", 0, mapping)
        return combinations