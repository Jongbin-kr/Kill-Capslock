## 
## 본 프로그램은 논문 크롤링시, 여러 줄로 구성되기도 하고 다양한 특수문자/숫자가 섞여있는 
## 저자명을 `abc, def, ghi`처럼 정규화하기 위해 제작됨.
##
## ----사용방법----
## 각각의 저자명을 복사-붙여넣기한 뒤, Enter + Ctrl + Z + Enter를 통해 input창을 종료하면,
## 정규화된 결과물이 출력창으로 출력됨. 
##
## ----정규화 규칙----
## 1) 저자명에는 한글, 영문 대소문자만 올 수 있으며, 그 외 숫자나 특수문자 등은 모두 제거한다.
## 2) 저자가 여려 명인 경우, 저자명간의 구분은 쉼표로 통일한다.
## 3) 저자명이 두 글자인 경우, 중간의 공백은 제거한다.

import re, sys

while True:

    print("input: ", end = '')
    raw = sys.stdin.readlines()
    # print('raw: ', raw)


    prepro_list = []
    for x in raw:
        try: 
            # print("try: ", x)
            prepro_xs = re.findall("[A-Za-z가-힣]+[ ]?[A-Za-z가-힣]*", x)
            # print(prepro_xs)
            for prepo_x in prepro_xs:
                if " " in prepo_x:
                    prepo_x = prepo_x.replace(" ", "")
                prepro_list.append(prepo_x)
        except: 
            print("except: ", x)
            print("!!!ERROR!!!")
    # print("prepro_list: ", prepro_list)
    
    
    
    print("result:")
    for i in prepro_list[:-1]:
        print(i, end = ', ')
    print(prepro_list[-1])
    print('\n')


## 22.10.09. Add Except handlinh(input error, input only 1 line)
#### 22.10.09. Modify Logic. (Use re.findall instead of split)
## 22.10.12. Now can deal name with two chars and space. Also clean up the output screen. Add Regularization Rule Guide.

## TODO: python 터미널에서 실행할 때, priint(input: )보다 sys.stdin.realindes가 먼저 실행....