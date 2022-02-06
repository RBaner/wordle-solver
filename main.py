from words import english_words_set

def score(word):
    vowels = 'aeiou'
    score = 0
    for vowel in vowels:
        if vowel in word.lower():
            score += 1
    return(score)

def best_possi(possi):
    scores = {}
    for word in possi:
        if score(word) not in scores:
            scores[score(word)] = [word]
        else:
            scores[score(word)].append(word)
    return(scores[max(scores)])

def check_word(exclude,include,placed,word):
    """exclude is a dict of chars not in the final word separated by place
    include is a list of chars for which we know where they aren't
    placed are chars which we know the place of"""
    for index in range(len(word)):
        if index in exclude:
            if word[index] in exclude[index]:
                return(False)
        if index in placed:
            if word[index] != placed[index]:
                return(False)
    for char in include:
        if char not in word:
            return(False)
    return(True)

        
def restrict_possibilities(exclude,include,placed,possi):
    return([i for i in possi if check_word(exclude,include,placed,i)])

def output(words):
    print("Try any of the following:")
    for word in words:
        print(word)

def main():
    exclude = {0:[],1:[],2:[],3:[],4:[]}
    placed = {}
    include = []
    possi = [i.lower() for i in english_words_set if len(i) == 5]

    output(['adieu','audio'])
    while True:
        word_tried = input("Which word did you try? ")
        results = input("What were the results (b=black,y=yellow,g=green; e.g. bybbg)? ")
        if results == 'ggggg':
            break
        for index in range(len(results)):
            if results[index] == 'b':
                for i in exclude:
                    exclude[i].append(word_tried[index])
            elif results[index] == 'y':
                if index not in exclude:
                    exclude[index] = [word_tried[index]]
                else:
                    exclude[index].append(word_tried[index])
                include.append(word_tried[index])
            else:
                placed[index] = word_tried[index]
        #print(placed)
        possi = restrict_possibilities(exclude, include, placed, possi)
        output(sorted(best_possi(possi)))
    return(0)


if __name__=="__main__":
    main()
