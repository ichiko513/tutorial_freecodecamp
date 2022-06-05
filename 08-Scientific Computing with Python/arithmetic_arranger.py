from enum import Flag
from msilib.schema import Error


def arithmetic_arranger(problemslist, display_result=False) -> None:
    if len(problemslist) > 5:
        # The limit of problems is five.
        print('Error: Too many problems.')
        return

    maxwidth = []
    for problem in problemslist:
        parts = problem.split()
        if parts[1] != '+' and parts[1] != '-':
            # Operator must be '+' or '-'
            print("Error: Operator must be '+' or '-'.")
            return
        if parts[0].isdecimal() == False or parts[2].isdecimal() == False:
            # must be digits.
            print('Error: Numbers must only contain digits.')
            return
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            # max of four digits in width
            print('Error: Numbers cannot be more than four digits.')
            return
        maxwidth.append( max(len(parts[0]),len(parts[2])) )
    
    digform = lambda x : '{:>'+str(x)+'}'

    for i in range(3):
        for pi, problem in enumerate(problemslist):
            parts = problem.split()
            if i == 0:
                print('  ', end='')
                f = digform(maxwidth[pi])
                print('{:>4}'.format(parts[0]), end='')
                if pi < len(problemslist)-1:
                    print('....', end='')
            if i == 1:
                print('{}{}{}'.format(parts[0],parts[1],parts[2]), end='')
        print('')

        # print(' = ', eval(problem))
    pass

if __name__ == '__main__':
    arithmetic_arranger(
        ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    pass