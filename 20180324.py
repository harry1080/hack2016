# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-03-24 10:25:35
# @Last Modified by:   Marte
# @Last Modified time: 2018-03-24 10:43:24
# 判断回文数和素数小程序
import sys


# 在num处定义需要判断的数字
num = 131

num_p = 0
num_t = num

is_palin = False
is_prime = False

while num_t !=0:
    num_p = num_p * 10 + num_t % 10
    num_t =num_t / 10

if num == num_p:
    is_palin = True

for i in range(2,num):
    if num % i ==0:
        break
    else:
        is_prime = True
def main():
    if is_palin and is_prime:
        print 'OK'
    else:
        print 'NO'

if __name__ == "__main__":
    main()
