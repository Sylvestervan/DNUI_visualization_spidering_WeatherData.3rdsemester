#TODO#列表练习

service = ['http', 'ssh', 'lftp']
service.append('nginx')
service.extend(['firewalld', 'mysql'])
service.insert(1, 'iptables')

print(service)

a1 = [0, 3, 2, 'a', 4, 'b', 5, 'm']

a2 = a1[::2]
print(a2)

a3 = a1[1:6:2]
print(a3)

a4 = a1[-1::]
print(a4)

a5 = a1[-3::-2]
print(a5)

a = [['k', ['qqq', 20, 33], 'xx', 'yy']]

a[0][1][0] = 'OOO'

a = [['l']+['m']+['n'] + a[0][1:] + a[0][:-2]]

a = [item[:-2] for item in a]

print(a)

#TODO#判断是否是回文数

n1 = 1234321
n2 = 1234567

n1_list = [int(digit) for digit in str(n1)]

n1_judgement1 = n1_list[:4]

n1_judgement2 = n1_list[:-3]

if n1_judgement1 == n1_judgement2:
    print("您输入的是回文数。")

#TODO#用户输入一个整数，求该数的阶乘。
def factorial(n):
    if n < 0:
        return "负数没有阶乘"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# 用户输入
num = int(input("请输入一个整数："))
print(f"{num}的阶乘是：{factorial(num)}")

#TODO#阶和

def summary(m):
    if m < 0:
        return "没有总和"
    elif m == 0:
        return "0 is 0"
    else:
        total = 0
        for j in range(1, m + 1):
            total += j
        return total

integer = int(input("请输入一个整数："))
print(f"{integer}的总和是：{summary(integer)}")

#TODO#求100内所有素数之和（加分项）

def is_prime(num_prime):
    if num_prime < 2:
        return False
    for k in range(2, int(num_prime**0.5) + 1):
        if num_prime % k == 0:
            return False
    return True

sum_of_primes = sum(num_prime for num_prime in range(2, 100) if is_prime(num_prime))
print(f"100以内所有素数之和为: {sum_of_primes}")

#TODO#求200内能被17整除的最大正整数

def judgement_divide(num_d):
    if num_d < 17:
        return "没有一个数能完全被17整除"
    elif num_d == 17:
        return "能被17整除的最小正整数是17"
    else:
        for s in range(num_d, 0, -1):
            if s % 17 == 0:
                return f"{num_d}以内能被17整除的最大正整数是: {s}"

# 测试函数
num_d = int(input("请输入一个整数："))
print(judgement_divide(num_d))