import datetime

ALLOWED_UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ALLOWED_NUM = set("0123456789")

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr

def FDollarTen2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:10.2f}".format(DollarValue)

    return DollarValueStr


def FDollarTen0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:10.0f}".format(DollarValue)

    return DollarValueStr


def FCommaTen2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:10.2f}".format(Value)

    return ValueStr


def FCommaTen0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:10.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr


def ValidateProv():

    ALLOWED_UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while True:
        Prov = input("Enter the province (AA): ").upper()
        if Prov == "":
            print("Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("Error - Province must be 2 letters.")
        elif not set(Prov[0:]).issubset(ALLOWED_UPPER):
            print("Error - Province must be 2 letters.")
        elif Prov not in ["AB", "BC", "MB", "SK", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU"]:
            print("Error - Province is invalid. Please re-enter")
        else:
            return Prov


'''
while True:
        Province = ValidateProv()
        break



def ValidateVehYear():
    while True:
        CurDate = datetime.date.today()
        CurYear = int(CurDate.year)
        VehYear = input("Enter the vehicle year: ")
        if VehYear == "":
            print("Error - Vehicle year cannot be blank.")
        elif len(VehYear) != 4:
            print("Error - Vehicle year must be 4 digits.")
        elif not set(VehYear[0:]).issubset(ALLOWED_NUM):
            print("Error - Vehicle year must be 4 digits.")
        elif int(VehYear) > CurYear:
            print("Vehicle year entered is higher than current year.")
        else:
            return VehYear
            break


while True:
        VehicleYear = ValidateVehYear()
        break
'''
def ValidatePhNum():

    while True:
        PhNum = input("Enter the phone number (9999999999): ")
        if PhNum == "":
            print("Error - Phone number cannot be blank.")
        elif len(PhNum) != 10:
            print("Error - Phone number must be 10 digits.")
        elif not set(PhNum[0:]).issubset(ALLOWED_NUM):
            print("Error - Phone number must be all digits.")
        else:
            return PhNum



def ValidatePCode():
    while True:
        PCode = input("Enter the postal code (A1A1A1): ").upper()
        if PCode == "":
            print("Error - Postal Code cannot be blank.")
        elif len(PCode) != 6:
            print("Error - Postal Code must contain 6 characters.")
        elif not set(PCode[0]).issubset(ALLOWED_UPPER):
            print("Error - Postal Code must have the format (A1A1A1).")
        elif not set(PCode[1]).issubset(ALLOWED_NUM):
            print("Error - Postal Code must have the format (A1A1A1).")
        elif not set(PCode[2]).issubset(ALLOWED_UPPER):
            print("Error - Postal Code must have the format (A1A1A1).")
        elif not set(PCode[3]).issubset(ALLOWED_NUM):
            print("Error - Postal Code must have the format (A1A1A1).")
        elif not set(PCode[4]).issubset(ALLOWED_UPPER):
            print("Error - Postal Code must have the format (A1A1A1).")
        elif not set(PCode[5]).issubset(ALLOWED_NUM):
            print("Error - Postal Code must have the format (A1A1A1).")
        else:
            return PCode

import sys
def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count),
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)