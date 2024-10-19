def count_words(sentence):
    res={}
    ls=[]
    string=""
    for letter in sentence:
        if letter.isalpha() or letter.isdigit():
            string+=letter
        else:
            ls.append(string)
            string=""
    if string!="":
        ls.append(string)
    for word in ls:
        if word not in res:
            res[word]=ls.count(word)   
    return res



print(count_words("skibidi"))