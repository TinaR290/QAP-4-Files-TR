#QAP4 Project 1
#Program to enter and calculate new insurance policy information
#for the One Stop Insurance Company
# Author:  Tina Rowe
# Date Written July 18-23 2023

#import libraries
import FormatValues as FV
import datetime
import time
from tqdm import tqdm

CurrDate = datetime.date.today()
PayDateDay = 1
PayDateMonth = CurrDate.month + 1
PayDateYear = CurrDate.year
PmtDate = datetime.date(PayDateYear, PayDateMonth, PayDateDay)

# Constants
ALLOWED_UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ALLOWED_NUM = set("0123456789")
PROV_LIST = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
PMT_FREQ = ["F","M"]
OPTIONS = ["Y", "N"]

# Open the defaults file and read the values into variables
f = open('OSICDef.dat', 'r')
NEXT_POL_NUM = int(f.readline())
BAS_PREM = float(f.readline())
ADD_CAR_DIS = float(f.readline())
EX_LIAB = float(f.readline())
OP_GLASS = float(f.readline())
OP_LOANER = float(f.readline())
HST_RATE = float(f.readline())
MTH_PROC_FEE = float(f.readline())
f.close()

# Main program
while True:
    CustFirstName = input("Enter customer first name: ").title()
    if CustFirstName.upper() == "END":
        break
    CustLastName = input("Enter customer last name: ")
    StAdd = input("Enter customer street address: ")
    City = input("Enter customer city: ").title()
    Prov = FV.ValidateProv()
    PCode = FV.ValidatePCode()
    PhNum = str(FV.ValidatePhNum())

    while True:
        NumCars = input("Enter number of cars to be insured: ")
        if NumCars == "":
            print("Error - Answer cannot be blank - Please reenter.")
        elif not set(NumCars[0:]).issubset(ALLOWED_NUM):
            print("Error - Answer must be a number - Please reenter.")
        else:
            NumCars = int(NumCars)
            break

    while True:
        OpExLiab = input("Does customer wish to purchase additional liability coverage? (Y/N): ").upper()
        if OpExLiab == "":
            print("Error - Answer cannot be blank - Please reenter.")
        elif OpExLiab not in OPTIONS:
            print("Error - Answer must be  Y  or  N - Please reenter.")
        else:
            if OpExLiab == OPTIONS[0]:
                PremExLiab =  EX_LIAB * NumCars
                OpExLiabDsp = "Yes"
                break
            elif OpExLiab == OPTIONS[1]:
                PremExLiab = 0
                OpExLiabDsp = "No "
                break

    while True:
        OpGlass = input("Does customer wish to purchase glass coverage? (Y/N): ").upper()
        if OpGlass == "":
            print("Error - Answer must be  Y  or  N - Please reenter.")
        elif OpGlass not in OPTIONS:
            print("Error - Answer must be  Y  or  N - Please reenter.")
        else:
            if OpGlass == OPTIONS[0]:
                PremGlass = OP_GLASS * NumCars
                OpGlassDsp = "Yes"
                break
            elif OpGlass == OPTIONS[1]:
                PremGlass = 0
                OpGlassDsp = "No "
                break

    while True:
        OpLoaner = input("Does customer wish to purchase loaner vehicle coverage? (Y/N): ").upper()
        if OpLoaner == "":
            print("Error - Answer must be  Y  or  N - Please reenter.")
        elif OpLoaner not in OPTIONS:
            print("Error - Answer must be  Y  or  N - Please reenter.")
        else:
            if OpLoaner== OPTIONS[0]:
                PremLoaner = OP_LOANER * NumCars
                OpLoanerDsp = "Yes"
                break
            elif OpLoaner == OPTIONS[1]:
                PremLoaner = 0
                OpLoanerDsp = "No "
                break

    while True:
        PmtTerms = input("Does the customer wish to pay in full or monthly? (F/M): ").upper()
        if PmtTerms == "":
            print("Error - Answer must be  F  or  M - Please reenter.")
        elif PmtTerms not in PMT_FREQ:
            print("Error - Answer must be  F  or  M - Please reenter.")
        else:
            if PmtTerms == PMT_FREQ[1]:
                MthPmtFee = MTH_PROC_FEE
                PmtFreq = "Monthly"
                break
            elif PmtTerms == PMT_FREQ[0]:
                MthPmtFee = 0
                PmtFreq = "Annually"
                break

# Calculations
    LiabPrem = float((BAS_PREM * NumCars) - (BAS_PREM * ADD_CAR_DIS * (NumCars - 1)))

    TotExCost = PremExLiab + PremGlass + PremLoaner

    TotPrem = LiabPrem + TotExCost

    HSTCost = TotPrem * HST_RATE

    TotCost = TotPrem + HSTCost

    if PmtTerms == PMT_FREQ[1]:
        Payment = (TotCost + MthPmtFee) / 8
    elif PmtTerms == PMT_FREQ[0]:
        Payment = TotCost
    else:
        break

# Print outputs
    print()
    print()
    print("=========================================================")
    print("                One Stop Insurance Company")
    print()
    print("                     *** RECEIPT ***")
    print("=========================================================")
    print("Date:           ",CurrDate)
    print("Policy Number:  ",NEXT_POL_NUM)
    print("Policy Holder:  ",CustFirstName + " " + CustLastName)
    print("Address:        ",StAdd)
    print("                ",City + " " + Prov + "  " + PCode)
    PhNumDsp = (PhNum[0:3]) + "-" + (PhNum[3:6]) + "-" + (PhNum[6:])
    print("Phone Number:   ",PhNumDsp)
    print("=========================================================")
    print("Number of vehicles insured:           ",NumCars)
    BasPremDsp = FV.FDollar2(LiabPrem)
    print(f"Basic premium:                                 {BasPremDsp:>10s}")
    ExLiabDsp = FV.FDollar2(PremExLiab)
    print(f"Additional liability coverage: {OpExLiabDsp} {ExLiabDsp:>10s}")
    PremGlassDsp = FV.FComma2(PremGlass)
    print(f"Optional glass coverage:       {OpGlassDsp} {PremGlassDsp:>10s}")
    PremLoanerDsp = FV.FComma2(PremLoaner)
    print(f"Optional rental vehicle:       {OpLoanerDsp} {PremLoanerDsp:>10s}")
    print("                                   __________")
    TotExCostDsp = FV.FComma2(TotExCost)
    print(f"Total extra costs:                             {TotExCostDsp:>10s}")
    print("                                               __________")
    TotPremDsp = FV.FDollar2(TotPrem)
    print(f"Total premium:                                 {TotPremDsp:>10s}")
    HSTCostDsp = FV.FComma2(HSTCost)
    print(f"HST:                                           {HSTCostDsp:>10s}")
    print("                                               __________")
    TotCostDsp = FV.FDollar2(TotCost)
    print(f"Total cost:                                    {TotCostDsp:>10s}")
    print("                                               ==========")
    print()
    print("Payment frequency:               ",PmtFreq)
    CurrDate = datetime.date.today()
    print("Payment due date:                ",PmtDate)
    print(f"Payment amount:                  ",FV.FDollar2(Payment))
    print("=========================================================")
    print()

# Write the values to Policies.dat file for future reference.
    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POL_NUM}, ")
    f.write(f"{CustFirstName}, ")
    f.write(f"{CustLastName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PCode}, ")
    f.write(f"{PhNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{OpExLiab}, ")
    f.write(f"{OpGlass}, ")
    f.write(f"{OpLoaner}, ")
    f.write(f"{PmtTerms}, ")
    f.write(f"{TotPrem}\n")
    f.close()

    print()
    print("Saving data - please wait")

#Add a progress bar
    for i in tqdm(range(int(9e6))):
        pass

    print("Policy #" + " " + str(NEXT_POL_NUM) + " " + "information processed and saved ...")
    time.sleep(1)
    print()

# Update any default values based on the processing requirements
    NEXT_POL_NUM += 1

# Write the current values back to the OSICDef.dat defaults file.
f = open('OSICDef.dat', 'w')
f.write(f"{NEXT_POL_NUM}\n")
f.write(f"{BAS_PREM}\n")
f.write(f"{ADD_CAR_DIS}\n")
f.write(f"{EX_LIAB}\n")
f.write(f"{OP_GLASS}\n")
f.write(f"{OP_LOANER}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{MTH_PROC_FEE}\n")
f.close()