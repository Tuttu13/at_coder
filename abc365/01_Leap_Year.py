

def Leap_yearear():
    """問題文
    1583 以上 2023 以下の整数 
    year が与えられます。

    西暦 
    year 年の日数を求めてください。

    なお、制約の範囲内では西暦year年の日数は以下の通りです。

    year が4の倍数でない年は 365 日

    year が4の倍数で、かつ100 の倍数でない年は366 日

    year が 100 の倍数で、かつ 400 の倍数でない年は 365 日

    year が 400 の倍数である年は 366 日
    """

    year = int(input())

    if year % 400 == 0:
        print(366)
    elif year % 100 == 0 and year % 400 != 0:
        print(365)
    elif year % 100 != 0 and year % 4 == 0:
        print(366)
    else:
        print(365)

Leap_yearear()