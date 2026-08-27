class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res


        # output = []
        # for i in range(len(temperatures)):
        #     stack = []
        #     r = i + 1
        #     while temperatures[i] < temperatures[r] and r < len(temperatures):
        #             stack.append(temperatures[r])
        #             r += 1
        #     output.append(len(stack))
        # return output