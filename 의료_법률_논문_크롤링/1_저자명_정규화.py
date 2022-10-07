##
## 본 프로그램은 논문 크롤링시, 여러 줄로 구성되기도 하고 다양한 특수문자/숫자가 섞여있는 
## 저자명을 `abc, def, ghi`처럼 정규화하기 위해 제작됨.
##
## 각각의 저자명을 복사-붙여넣기한 뒤, Ctrl + Z + Enter 혹은 Ctrl + D를 통해 input창을 종료하면,
## 정규화된 결과물이 출력창으로 출력됨. 



import os, re, sys

while True:

    print("input: ", end = '')
    raw = sys.stdin.readlines()


    prepro_list = []
    for x in raw:
        prepro_x = re.search("[A-Za-z가-힣]+", x).group()
        prepro_list.append(prepro_x)
    
    
    print("result:")
    for x in prepro_list[:-1]:
        print(x, end = ', ')
    print(prepro_list[-1])
    print('\n')


