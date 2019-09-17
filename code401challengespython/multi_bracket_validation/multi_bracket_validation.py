def multi_bracket_validation(input):
    open = ("(", "[", "{")
    close = (")", "]", "}")
    pairs = {open[0]:close[0],
               open[1]:close[1],
               open[2]:close[2]}

    closing= []
    for i in input:
        if i in open:
            closing.append(pairs[i])
        elif i in close:
            if not closing:
                return False

            elif closing[-1] == i:
                closing.pop()
            else:
                return False

    return True

