def count_words(sentence):
    res={}
    ls=[]
    string=""
    counter=0
    for letter in sentence:
        if letter.isalpha() or letter.isdigit() or letter=="'" or letter.isnumeric():
            if  (sentence[sentence.index(letter)-1]).isalpha() or letter.isalpha() or letter=="'" or letter.isnumeric():

                try:
                    if letter=="'":
                        if sentence[counter-1].isalpha() and sentence[counter+1].isalpha():
                            string+=letter
                        else:
                            ls.append(string.lower())
                            string=""
                            counter+=1
                            continue
                    else:
                        string+=letter
                except IndexError:
                    continue
        else:
            ls.append(string.lower())
            string=""
        counter+=1

    if string!="":
        ls.append(string.lower())
    for word in ls:

        if word not in res and word!="" and word!="'":
            res[word]=ls.count(word)   
    return res



print(count_words("testing, 1, 2 testing"))
#passed all 17 tests