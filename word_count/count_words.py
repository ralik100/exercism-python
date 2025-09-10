def count_words(sentence):
    res={}
    ls=[]
    string=""
    counter=0
    for letter in sentence:
        if letter.isalpha() or letter.isdigit() or letter=="'":
            if  (sentence[sentence.index(letter)-1]).isalpha() or letter.isalpha() or letter=="'":

                try:
                    if letter=="'" and string[-1].islower() and sentence[counter+1].islower():
                        print(letter)
                        print(sentence[counter+1])
                        string+=letter
                        continue
                except IndexError:
                    continue
                string+=letter
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



print(count_words("Joe can't tell between 'large' and large."))