
def arithmetic_arranger(problemslist, display_result=False) -> None:
    if len(problemslist) > 5:
        # The limit of problems is five.
        print('Error: Too many problems.')
        return

    maxwidth = []
    result = []
    for problem in problemslist:
        item = problem.split()
        if item[1] != '+' and item[1] != '-':
            # Operator must be '+' or '-'
            print("Error: Operator must be '+' or '-'.")
            return
        if item[0].isdecimal() == False or item[2].isdecimal() == False:
            # must be digits.
            print('Error: Numbers must only contain digits.')
            return
        if len(item[0]) > 4 or len(item[2]) > 4:
            # max of four digits in width
            print('Error: Numbers cannot be more than four digits.')
            return
        maxwidth.append( max(len(item[0]),len(item[2])) )
        result.append( str(eval(problem)) )
       
    digform = lambda ope,digw,endspace : ope + '{:>'+str(digw)+'}'+ ('    ' if endspace else '')

    loopcnt = 4 if display_result == True else 3
    for i in range(loopcnt):
        for pi, problem in enumerate(problemslist):
            item = problem.split()
            endspace = pi < len(problemslist) - 1
            if i == 0:
                print( digform('  ', maxwidth[pi], endspace).format(item[0]), end='' )
            if i == 1:
                print( digform(item[1] + ' ', maxwidth[pi], endspace).format(item[2]), end='' )
            if i == 2:
                bar = ''.join( '-' for i in range(maxwidth[pi]) )
                print( digform('--', maxwidth[pi], endspace).format(bar), end='' )
            if i == 3:
                print( digform('', maxwidth[pi]+2, endspace).format(result[pi]), end='' )
        print('')

    pass

if __name__ == '__main__':

    arithmetic_arranger(
        # ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
        #  ["9999 + 9999", "0 - 9999", "0 + 0", "0 - 1"])
        ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

