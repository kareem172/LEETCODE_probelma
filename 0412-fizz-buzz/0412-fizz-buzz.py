class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        val = ""
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 ==0:
                val = "FizzBuzz"
            elif i % 3 == 0:
                val = "Fizz"
            elif i % 5 == 0:
                val = "Buzz"
            else:
                val = f"{i}"
            res.append(val)
        return res