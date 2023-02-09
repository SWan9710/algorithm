import sys
sys.stdin = open('input.txt', encoding='utf-8')

for N in range(10):
    tc = int(input())
    pattern_word = input()
    target_word = input()
    count = 0

    for i in range(len(target_word)-len(pattern_word)+1):
        for j in range(len(pattern_word)):
            if pattern_word[j] != target_word[i + j]:
                break
        else:
            count += 1
    print(f'#{tc}', count, target_word.count(pattern_word))
