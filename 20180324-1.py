# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-03-24 11:10:31
# @Last Modified by:   Marte
# @Last Modified time: 2018-03-24 13:21:06
# 日历小程序
#
import sys


# year = 2018
# month = 5

'''
    判断是不是一个闰年
'''

def is_leap_year(year):
    if year % 4 ==0 and year % 100 !=0 or year % 400== 0:
        return True
    else:
        return False
'''
    判断这个月有多少天
'''

def get_num_of_days_in_month(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28
'''
    从1800.1.1至今有多少天
'''

def get_total_num_of_days(year,month):
    #年份-1800 and 月份-1 and 日期-1
    days = 0
    for y in range(1800,year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365
    for m in range(1,month):
        days += get_num_of_days_in_month(year,m)

    return days

'''
1800.1.1 星期三
'''

def get_start_day(year,month):
    result = 0
    x = get_total_num_of_days(year,month)
    result = (3+x) % 7
    return result

def main():

    print is_leap_year(year)
    print get_num_of_days_in_month(year,month)
    print get_total_num_of_days(year,month)
    print get_start_day(year,month)

if __name__ == "__main__":
    main()
