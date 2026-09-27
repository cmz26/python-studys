# 学了变量, 但是我们不知道怎么判断!

# 判断是 if 语句, 例如:
# if a == b:
# Python 是有缩进的, 实战演示:

age = input("How old are you > ")
# 接下来怎么做?
# if age >= 18:
#     print("成年")
# 吗?
# Python, java, C++ 以及所有的语言都有类型一说, 比如 C++ 就是靠 int a,b 申请 a 和 b 的变量
# 要强制类型转换,就要用 int() 了:

age = int(age)

# 让后就继续
if age >= 18:
    print("成年")
# 接着, 就是否则
else:
    print(未成年)
# 当然, 还有 elif
# 结构
"""
if - elif(可以多个) - else

"""
