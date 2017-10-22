#!/usr/bin/env python3
import sys

try:
    # income = int(sys.argv[1])
    income =int(input("your income2: "))

    if income>=0 and income<=3500:
        print(format(0,".2f"))
    
    elif income>3500 and income<5000:
        result = (income-3500)*0.03
        print(format(result,".2f"))
    
    elif income>=5000 and income<9000:
        result = (income-3500)*0.1-105
        print(format(result,".2f"))

    elif income>=9000 and income<12500:
        result = (income-3500)*0.2-555
        print(format(result,".2f"))

    elif income>=12500 and income<39500:
        result = (income-3500)*0.25-1005
        print(format(result,".2f"))

    elif income>=39500 and income<59500:
        result = (income-3500)*0.3-2755
        print(format(result,".2f"))

    elif income>=59500 and income<84500:
        result = (income-3500)*0.35-5505
        print(format(result,".2f"))

    elif income>=84500:
        result = (income-3500)*0.45-13505
        print(format(result,".2f"))
    else:
        print("无效数据")
except:
    print("Parameter Error!!!")






