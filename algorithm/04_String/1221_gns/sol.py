import sys
sys.stdin = open('input.txt')

<<<<<<< HEAD
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
=======
# 딕셔너리로 풀어보기
# test_case = int(input())
# for tc in range(1,test_case+1):

    # num_dict = {'ZRO' : 0,'ONE' : 1,'TWO' : 2,'THR' : 3,'FOR' : 4,'FIV' : 5,'SIX' : 6,'SVN' : 7,'EGT' : 8,'NIN' : 9,}
    #
    # tc_num, num_length = input().split()
    # num_length = int(num_length)
    # num_list = list(input().split())
    #
    #
    # for i in range(num_length-1):                                               # 전체길이 - 1
    #     min_v = i                                                               # 최솟값을 첫번째 i값으로 지정
    #     for j in range(i+1, num_length):                                        # 1부터 전체길이를 돌거
    #         if num_dict[num_list[i]] > num_dict[num_list[j]]:                   # 배열의 첫번째 값이 배열의 두번째 값보다 크다면
    #             min_v = j                                                       # 최솟값은 배열의 두번째 값이므로 최솟값 변경
    #             num_list[i], num_list[min_v] = num_list[min_v], num_list[i]     # 첫번째 값과 최솟값의 위치 변경
    # print(tc_num)                                                               # 오름차순 정렬이 실행되는거
    # print(*num_list)

    # 리스트로 만들어서 풀어보기
test_case = int(input())
for tc in range(1, test_case + 1):

    tc_num, num_length = input().split()
    input_num_list = list(input().split())
    num_list = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    new_list = []


    for i in num_list:
        for j in input_num_list:
            if i == j:
                new_list.append(i)
            else:
                continue
    print(tc_num)
    print(*new_list)
>>>>>>> f4416a4feb89ca6720a098a41efb00c92baf3c80
