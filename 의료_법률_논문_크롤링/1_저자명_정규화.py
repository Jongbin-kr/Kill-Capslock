## 
## 본 프로그램은 논문 크롤링시, 여러 줄로 구성되기도 하고 다양한 특수문자/숫자가 섞여있는 
## 저자명을 `abc, def, ghi`처럼 정규화하기 위해 제작됨.
##
## 각각의 저자명을 복사-붙여넣기한 뒤, Enter + Ctrl + Z + Enter를 통해 input창을 종료하면,
## 정규화된 결과물이 출력창으로 출력됨. 

import re, sys

while True:

    print("input: ", end = '')
    raw = sys.stdin.readlines()

    
    print('raw: ', raw)

    prepro_list = []
    for x in raw:
        try: 
            print("try: ", x)
            prepro_xs = re.findall("[A-Za-z가-힣]+", x)
            print(prepro_xs)
            for prepo_x in prepro_xs:
                prepro_list.append(prepo_x)
        except: 
            print("except: ", x)
            print("!!!ERROR!!!")
            
    
    print("prepro_list: ", prepro_list)
    print("result:")
    for i in prepro_list[:-1]:
        print(i, end = ', ')
    print(prepro_list[-1])
    print('\n')


## 22.10.09. Add Except handlinh(input error, input only 1 line)
#### 22.10.09. Modify Logic. (Use re.findall instead of split)