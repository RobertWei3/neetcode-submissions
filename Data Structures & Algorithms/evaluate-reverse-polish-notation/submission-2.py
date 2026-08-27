class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)

                elif token == "-":
                    stack.append(left - right)
                
                elif token == "*":
                    stack.append(left * right)

                elif token == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(token))
            
        return stack[0]





        # curr_val = int(tokens[0])
        # num_stack = []
        # for i in range(1, len(tokens)):
        #     if nottokens[i].isdigit():
        #         if tokens[i] == "+":
        #             curr_val += num_stack.pop()
        #         elif tokens[i] == "-":
        #             curr_val -= num_stack.pop()
        #         elif tokens[i] == "*":
        #             curr_val *= num_stack.pop()
        #         else:
        #             curr_val /= num_stack.pop()
        #     num_stack.append(int(tokens[i]))
        # return curr_val
