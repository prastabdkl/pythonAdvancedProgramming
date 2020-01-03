def normal_division_with_exception():
    num1 = int(input('Enter a divisor'))
    num2 = int(input('Enter a dividend'))

    result = num1/num2

    print(result)

def normal_division_with_exception_control():
    """
    if num2 == 0:
        print('The number is not divisible by 0')
    else:
        result = num1/num2
        print(result)
     """
    try:
        num1 = int(input('Enter a divisor'))
        num2 = int(input('Enter a dividend'))
        result = num1/num2
        print(result)
        print('Hello Nepal')
        #infile =open('hell.txt','r')
    # except ZeroDivisionError as error:
    #     print('The divisor cannot be zero:',error)
    # except ValueError:
    #     print('Invalid value is entered')
    # except FileNotFoundError:
    #     print('File not found')
    except Exception as E:
        print(E)
    else:
        print('ELSE BLOCK')
    finally:
        print('FINALLY BLOCK')

def main():
    #normal_division_with_exception()
    normal_division_with_exception_control()

main()