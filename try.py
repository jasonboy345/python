# 查看异常效果
try:
	income = int("aaaa")
	print(income)
	print(123)
except ValueError:
	print("值错误")


