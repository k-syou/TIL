def postfix(s):
    # 중위표기식 => 후위표기식
    # 연산자 우선순위
    # '+' = '-' < '*' = '/'
    ops = {"+": 0, "*": 1}
    op_stack = []
    res = ""
    for c in s:
        if c in ops:  # 연산자인 경우
            # 현재 연산자 스택이 존재 하고,
            # 연산자 스택의 top(-1 인덱스)에 존재하는 연산자가
            # 현재 입력하는 연산자보다 우선순위가 높고, 여는 괄호가 아닌경우
            while op_stack and ops[op_stack[-1]] >= ops[c]:
                # 연산자를 빼서 결과에 출력
                res += op_stack.pop()
            # 해당 연산자 스택에 담기
            op_stack.append(c)
        else:
            # 숫자인 경우 출력
            res += c

    while op_stack:  # 연산자가 남아있는 경우
        # 나머지 연산자 출력
        res += op_stack.pop()
    return res


def calc(op, a, b):
    if op == "+":
        return a + b
    if op == "*":
        return a * b


def postfix_calc(postfix_str):
    # 후위 표기식 계산기
    num_stack = []
    ops = ["+", "*"]
    for c in postfix_str:
        if c in ops:  # 연산자인 경우
            # 숫자스택의 맨 끝 두 숫자를 가져옴
            b, a = num_stack.pop(), num_stack.pop()
            # 계산 후 계산된 결과를 숫자 스택에 추가
            num_stack.append(calc(c, a, b))
        else:
            # 숫자인 경우, 숫자 스택에 추가
            num_stack.append(int(c))
    # 마지막 남은 숫자 스택 출력
    return num_stack.pop()


for tc in range(1, 11):
    N = int(input())
    S = input()
    postfix_str = postfix(S)
    print(f"#{tc} {postfix_calc(postfix_str)}")
