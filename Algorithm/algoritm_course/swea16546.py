'''
100
666236
234121
111650
678623
123715
777099
000705
666323
333310
678576
123646
678176
888021
456793
456339
111034
567164
678470
456593
888844
111316
111821
567372
555654
555157
345592
789598
678847
234297
345134
678952
000194
345708
000524
567430
234648
456316
456115
345539
123618
222897
789088
012156
444344
111042
234022
456036
666247
789568
333823
012798
555817
999503
456221
444681
234912
444945
999227
000698
000016
444998
567004
234502
567236
567149
333179
222177
000139
000882
345273
567985
111065
999058
888527
012359
345900
222034
888024
888014
678454
456220
567617
999930
000315
345355
456941
777250
666006
000132
555082
000075
111524
777995
000299
111479
999707
333139
456199
678705
222223

'''
'''
10
123456
139673
644544
123123
667767
054060
101123
000000
111111
532235

'''
'''
1)tri 2개
333333
2)tri 2개
333334
333344
333444
3) 3개
333345
333445
334455
4)
333456
334456
5)
334567
6)
345678
'''
T = int(input())
# all_six_digit_numbers = [f"{i:06d}" for i in range(1000000)]


def baby_gin(N):
    set_N = set(N)
    list_N = list(map(int,N))
    if len(set_N) == 1: # len(set)이 1이면 항상 baby_gin
        return f'true'
    elif len(set_N) == 2: # len(set)이 2인 경우에 run+run가능
        list_N.sort()
        for i in list_N:
            if list_N.count(i)==3:
                return f'true'
        return f'false'
    elif len(set_N) == 3: # len(set)이 3인 경우에 run + triplet(숫자 하나가 겹치는 것 아닌것 2가지), triplet + triplet
        list_N.sort()
        for i in list_N:
            if list_N.count(i)==4: # run+triplet(숫자하나가 겹치는 것)
                for _ in range(3):
                    list_N.remove(i)
                if list_N[0]+2 == list_N[1]+1 == list_N[2]:
                    return f'true'
                else:
                    return f'false'

        for i in list_N:
            if list_N.count(i)==3: # run+triplet(숫자 안겹치는 것)
                for _ in range(3):
                    list_N.remove(i)
                if list_N[0]+2 == list_N[1]+1 == list_N[2]:
                    return f'true'
                else:
                    return f'false'

        for i in list_N:
            if list_N.count(i)==2:
                if list_N[0]+2 == list_N[2]+1 == list_N[4]:
                    return f'true'
                else:
                    return f'false'
    elif len(set_N) == 4: # run+triplet 한가지 경우
        list_N.sort()
        for i in list_N:
            if list_N.count(i)==3:
                for _ in range(3):
                    list_N.remove(i)
                if list_N[0]+2 == list_N[1]+1 == list_N[2]:
                    return f'true'
                else:
                    return f'false'
        for i in list_N:
            if list_N.count(i)==2:
                return f'false'
    elif len(set_N) == 5:
        list_N.sort()
        if (list_N[0]+2 == list_N[1]+1 == list_N[2]) and (list_N[3]+2 == list_N[4]+1 == list_N[5]):
            return f'true'
        else:
            return f'false'
    elif len(set_N) == 6:
        list_N.sort()
        if (list_N[0]+2 == list_N[1]+1 == list_N[2]) and (list_N[3]+2 == list_N[4]+1 == list_N[5]):
            return f'true'
        else:
            return f'false'

for tc in range(1, T+1):
# for i in all_six_digit_numbers:
#     N = i
    N = str(input().strip())
    print(f'#{tc} {baby_gin(N)}')