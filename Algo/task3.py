def checkBrackets(expression):
    opening = "{[("
    ending = "}])"

    brackets_only = [x for x in expression if x in opening or x in ending]
    stack = []
    no = 0

    for x in brackets_only:
        if x in opening:
            if not(stack) or (stack and (opening.index(x)-opening.index(stack[-1]) == 1):
                stack.append(x)
            else:
                no = 1
                break
        elif x in ending and stack and stack[-1] == opening[ending.index(x)]:
            stack.pop()
        else:
            no = 1
            break

    if no == 1:
        print("NO")
    else:
        print("YES")

checkBrackets("[123(145)38(37)812]")
checkBrackets("{125[2][(1)][3]125}")
checkBrackets("[125()125()125()125]")
checkBrackets("{125()125}")
checkBrackets("{125[12]{125}[12]125}")
checkBrackets("{125[12(123]125}")
