def solution(s):
    count=0
    for i in s:
        if i == '(':
            count+=1
        elif i == ')' and count>0:
            count-=1
        else: return False

    if count==0:
        return True
    else: return False


# print(solution("()()"))
