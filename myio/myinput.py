from myerrors.errors import InvalidRollNumberError, InvalidPercentageError, InvalidNameError


def get_rno():
    while True:
        try:
            rno = int(input("Enter The Roll Number : "))

            if rno < 1:
                raise InvalidRollNumberError("InvalidRollNumberError : Negative Roll Number Not Allowed")

        except InvalidRollNumberError as re:
            print(re)

        except ValueError as ve:
            print("Given Input Is Not A Number : ", ve)

        except:
            print("Unknown Error !!!")
        else:
            return rno

def get_name():
    while True:
        try:
            name = (input("Enter The Name : "))

            if not name.isalpha():
                raise InvalidNameError("InvalidNameError : Name Should have Alphabet Only !!")

        except InvalidNameError as ne:
            print(ne)
        except:
            print("Unknown Error !!!")
        else:
            return name

def get_per():
    while True:
        try:
            per = float(input("Enter The Percentage : "))

            if per < 0 or per > 100:
                raise InvalidPercentageError("InvalidPercentageError : Percentage Should be 0 and 100 !!")

        except InvalidPercentageError as pe:
            print(pe)

        except ValueError as ve:
            print("Given Input Is Not A Number : ", ve)

        except:
            print("Unknown Error !!!")
        else:
            return per