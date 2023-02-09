import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):

    num_dict = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }

    tc_num, num_length = input().split()
    word_num = input().split()

    num_list = []
    for i in range(int(num_length)):
        dict_key = ''.join(word_num[i])
        num_list.append(num_dict[dict_key])

    # 버블소트
    for i in range(len(num_list)-1,0,-1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    print(num_list)
    for i in num_list:
        print(num_dict.values(num_list[i]))
    # 리스트로 만들어서 풀어보기
    # 딕셔너리로 풀어보기
