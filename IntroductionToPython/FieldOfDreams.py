


def AddList(dicts):
    keys = []
    for key in dicts:
        keys.append(key)
    return keys

def GetQuestionByDictionary(dicts, keys, index):
    question = dicts[keys[index]]
    return question

def AddListField(keys):
    fields =[]
    result=""
    for i in range(len(keys)):
        count = len(keys[i])
        for j in range(count):
            result+='#'
        fields.append(result)
        result=''
    return fields

def PlayGame(keys, index):
    isTrue = False
    result=''
    print("1-слово целиком. 2- одна буква")
    print("Назовёте слово целиком или одну букву:", end='')
    wordsOrAlphabet = int(input())
    if wordsOrAlphabet ==1:
        while not isTrue:
            print("Назовите слово целиком:", end='')
            answer = input()
            if answer> keys[index] or answer < keys[index]:
                print("Это слова не подходит, повторите ещё раз")
                continue
            else:
                count = len(answer)
                result = keys[index]
                for i in range(count):
                    if answer[i] == result[i]:
                        isTrue = True
                        result=answer
                    else:
                        isTrue = False
                        break

            if isTrue:
                print("Поздравляю, вы угадали")
            else:
                print("Увы, вы не угадали, повторите ещё раз")
    elif wordsOrAlphabet == 2:
        while not isTrue:
            print("Назовите букву:", end='')
            symbol = input()
            if symbol in keys[index]:
                print("Есть такая буква")
                isTrue =True
                result = symbol
            else:
                print("Нет такой буквы, повторите ещё раз")
    return result

