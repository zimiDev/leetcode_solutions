class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        uniq_code = set()

        for word in words:
            code = "".join(morse[ord(char) - ord("a")] for char in word)
            uniq_code.add(code)
        return len(uniq_code)