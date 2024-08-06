def Second_Best():
    """問題文
    長さ 
    N の整数列 
    A=(A 1,…,A N) が与えられます。ここで 
    A 1,A 2,…,A Nは相異なります。

    A の中で二番目に大きい要素は 
    A の何番目の要素でしょうか。
    """

    N = int(input())
    A = list(map(int,input().split()))
    X = A.sort()[-2]
    print(A.index(X)+1)
Second_Best()