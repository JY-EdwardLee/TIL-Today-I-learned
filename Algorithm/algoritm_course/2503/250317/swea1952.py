



T = int(input())

for tc in range(1, T+1):
    fees = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    costs = []
    # # 1일권만
    # costs.append(fees[0]*sum(plan))
    # # 한달권
    # costs.append((12 - plan.count(0))*fees[1])
    # # 3개월권
    # i, cost = 0, 0
    # while i < 12:
    #     if i:
    #         cost += fees[2]
    #         i += 2
    #     i += 1
    # costs.append(cost)
    # 연권
    costs.append(fees[3])
    # 1일권 + 한달권
    # cost = 0
    # for i in range(12):
    #     if plan[i]*fees[0] > fees[1]:
    #         cost += fees[1]
    #     else:
    #         cost += fees[0]*plan[i]
    # costs.append(cost)
    # 1일권 + 3개월권
    # plan.extend([0, 0])
    # i, cost = 0, 0
    # triple = [0] * 12
    # for a in range(10):
    #     triple[a] = (plan[a] + plan[a+1] + plan[a+2])
    # pass_list = []
    # x = 0
    # while x < 10:
    #     l = triple.index(max(triple))
    #     if triple[l] != -1 and triple[l+1] != -1 and triple[l+2] != -1 and plan[l] != 0:
    #         triple[l] = triple[l+1] = triple[l+2] = -1
    #         x += 3
    #         pass_list.append(l)
    #         pass_list.append(l+1)
    #         pass_list.append(l+2)
    #     else:
    #         triple[l] = 0
    #         x += 1
    # while i < 12:
    #     if i and i not in pass_list:
    #         cost += plan[i] * fees[0]
    #     elif i and i in pass_list:
    #         cost += fees[2]
    #         i += 2
    #     i += 1
    # costs.append(cost)
    # 일권 + 월권 + 3개월권
    i, cost = 0, 0
    costco = [0]*12
    while i < 12:
        costco[i] = costco[i-1] + plan[i]*fees[0]
        if plan[i]*fees[0] > fees[1]:
            costco[i] = costco[i] - plan[i]*fees[0] + fees[1]
        if costco[i] - costco[i-3] > fees[2] and i >= 2:
            costco[i] = costco[i-3] + fees[2]
        i += 1
    costs.append(max(costco))
    print(f'#{tc} {min(costs)}')