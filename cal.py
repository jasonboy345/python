#!/usr/bin/env python3
#coding:utf-8

# 计算个税计算器，输入工资，打印应缴纳的个税

import sys

# 获取到工资
try:
   salary = int(sys.argv[1])
   if salary <= 0:
      print('工资必须大于0')
      raise ValueError()
   elif salary <=3500:
      print('0')
   elif salary:

      # 应纳税所得额
      tax = (salary - 3500)

      if tax <= 1500:
          taxRate = 0.03
          other = 0
      elif tax <= 4500:
          taxRate = 0.10
          other = 105
      elif tax <= 9000:
          taxRate = 0.20
          other = 555
      elif tax <= 35000:
          taxRate = 0.25
          other = 1005
      elif tax <= 55000:
          taxRate = 0.3
          other = 2755
      elif tax <= 80000:
          taxRate = 0.35
          other = 5505
      else:
          taxRate = 0.45
          other = 13505
      
      result = format(tax*taxRate - other, ".2f") 
      print(result)

except:
   print("Parameter Error")

