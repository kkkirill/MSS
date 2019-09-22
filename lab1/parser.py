import sys
import os.path
if(len(sys.argv) == 4):
    if(os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2])):
        text = open(sys.argv[1], "r").read()
        operators = open(sys.argv[2], "r").readlines()

        with open(sys.argv[3], "w") as output:
            print("\n-----OPERATORS:-----\n", file=output)

            for index in range(0, len(operators)):
                operators[index] = operators[index].replace("\n", "")
                print(str(operators[index]) + " - " + str(text.count(operators[index])), file=output)
                text = ' '.join(text.replace(operators[index], " ").split())

            print("\n-----OPERANDS:-----\n", file=output)
            operands = sorted(list(set(text.split())))
            text = " " + text + " "

            for operand in range(len(operands)):
                operands[operand] = " " + operands[operand] + " "
                print(operands[operand] + " - " + str(text.count(operands[operand])), file=output)

                while (text.count(operands[operand]) != 0) :
                    text = text.replace(operands[operand], ' ')
        output.close()
    else:
        print("\nPass on correct file paths")
else:
    print("\nYou need pass on 3 arguments:\n 1 - file with code\n 2 - file with operators\n 3 - output file")