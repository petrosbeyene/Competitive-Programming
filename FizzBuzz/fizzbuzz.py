class Solution:
    def fizzBuzz(self, n: int):
        answerList = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                answerList.append("FizzBuzz")
            elif i%3 == 0:
                answerList.append("Fizz")
            elif i%5 == 0:
                answerList.append("Buzz")
            else:
                answerList.append(str(i))
        return(answerList)