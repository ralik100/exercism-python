def count_words(sentence):
    res={}
    ls=[]
    string=""
    for letter in sentence:
        if letter.isalpha() or letter.isdigit() or letter=="'":
            if  (sentence[sentence.index(letter)-1]).isalpha() or letter.isalpha() or letter=="'":
                string+=letter
        else:
            ls.append(string.lower())
            string=""
    if string!="":
        ls.append(string.lower())
    for word in ls:
        if word not in res and word!="" and word!="'":
            res[word]=ls.count(word)   
    return res



print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))