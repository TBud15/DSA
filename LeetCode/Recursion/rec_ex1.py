stack = []

def febonaci(num=1):
    # base case
    if stack and stack[-1] == 514229:
        return

    if not stack or not stack[-2]:
        stack.append(num)
        stack.append(num)

    if stack[-1] and stack[-2]:
        summary = stack[-1] + stack[-2]
        stack.append(summary)
        print(stack[-1])

    febonaci()

febonaci()