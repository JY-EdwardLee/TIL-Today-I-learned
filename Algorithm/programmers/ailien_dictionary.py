#url : https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    answer = 2
    for words in dic:
        spell_ = spell[:]
        for word in words:
            if word in spell_:
                spell_.remove(word)
            else:
                break
        else:
            if not spell_:
                answer = 1
                break
    return answer

spell = ["s", "o", "m", "d"]
dic = ["moos", "dzx", "smm", "sunmmo", "som"]
print(solution(spell, dic))