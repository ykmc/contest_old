# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    print(X*N)
else:
    print(X*K + Y*(N-K))