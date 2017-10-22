#!/usr/bin/env python3
# encoding: utf-8
import sys

def calculator(arg):
    for a in arg:
        li = a.split(":")
        id = li[0]
        income = li[1]
        print(id,income)
        try:
            # income = int(sys.argv[1])
            # income =int(input("your income2: "))
            income = int(income)


            if income>=0 and income<=3500:
                print(id+":"+format(0.835*income,".2f"))
            
            elif income>3500 and income<=5000:
                result = 0.835*income-((0.835*income-3500)*0.03-0)
                print(id+":"+format(result,".2f"))
            
            elif income>5000 and income<=9000:
                result = 0.835*income-((0.835*income-3500)*0.1-105)
                print(id+":"+format(result,".2f"))

            elif income>9000 and income<=12500:
                result = 0.835*income-((0.835*income-3500)*0.2-555)
                print(id+":"+format(result,".2f"))

            elif income>12500 and income<=39500:
                result = 0.835*income-((0.835*income-3500)*0.25-1005)

                print(id+":"+format(result,".2f"))

            elif income>39500 and income<=59500:
                result = 0.835*income-((0.835*income-3500)*0.3-2755)
                print(id+":"+format(result,".2f"))

            elif income>59500 and income<=84500:
                result = 0.835*income-((0.835*income-3500)*0.35-5505)
                print(id+":"+format(result,".2f"))

            elif income>84500:
                result = 0.835*income-((0.835*income-3500)*0.45-13505)
                print(id+":"+format(result,".2f"))
            else:
                print("无效数据")
        except:
            print("Parameter Error!!!")




# calculator("1:3500","2:5000","3:haha")
# calculator(['1:3000', '2:5000'])

sys.argv.pop(0)
# print(sys.argv)
calculator(sys.argv)

