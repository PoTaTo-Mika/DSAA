from functools import cmp_to_key

def compare(x, y):
    # 比较两个数字拼接后的结果
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

num = int(input())
alist = list(map(str, input().split()))

# 使用自定义的排序规则对数字进行排序
sorted_alist = sorted(alist, key=cmp_to_key(compare))

# 拼接成一个最终的字符串
result = ''.join(sorted_alist)
result = int(result)  # 转换成整数，去掉前导零

# 输出最终结果
print(result)
