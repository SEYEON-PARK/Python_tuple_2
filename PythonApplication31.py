def A(a, b):
    return(a+b, a-b)

first=int(input("첫 번째 정수를 입력하시오. : "))
second=int(input("두 번째 정수를 입력하시오. : "))

(first, second)=A(first, second)

print("두 수의 합은 %d이고, 두 수의 차는 %d이다." %(first, second))