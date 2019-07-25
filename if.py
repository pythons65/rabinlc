def search(string,word):
    for i in range(0,len(string),1):
        char = string[i]
        if char == word[0]:
            stro = string[i:]

            word1 = stro[0:len(word)]
            if word1 == word:
                num = i
                print(i,string[num])


search("hello world","orld")
