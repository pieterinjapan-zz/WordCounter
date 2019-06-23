"""
Pieter van Wyk
Created : 2018-12-30
Updated : 2019-06-23

Language : python

About : WordCounter
Simple program making use of class definitions. 
Counts the number of occurrences of a given word, 
and its synonyms chosen from a thesaurus, in a corpus 
of documents.

This was a homework project for the coursera course
"Computational Thinking for Problem Solving"
(https://www.coursera.org/learn/computational-thinking-problem-solving)
"""


# Defining Functions :
#---------------------

# Word Class :
class Word :
    def __init__(self,init_word) :
        self.word     = init_word
        self.synonyms = [init_word]

    def add_syn(self,new_synonym) :
        if new_synonym not in self.synonyms :
            self.synonyms.append(new_synonym)

# Thesaurus Entry Class :
class Entry :
  def __init__(self, input_word, input_synonyms) :
    self.word = input_word
    self.synonyms = input_synonyms

# Input :
# -------

# Thesaurus:
e1  = Entry('angry', ['mad', 'annoyed'])
e2  = Entry('mad', ['angry', 'annoyed'])
e3  = Entry('annoyed', ['angry', 'mad'])
e4  = Entry('sad', ['upset', 'depressed', 'unhappy'])
e5  = Entry('upset', ['sad', 'depressed', 'unhappy'])
e6  = Entry('depressed', ['sad', 'upset', 'unhappy'])
THE = [e1,e2,e3,e4,e5,e6]

# Corpus :
DOC_0 = ['you', 'bet', 'i', 'am', 'angry']
DOC_1 = ['i', 'am', 'angry', 'with', 'her']
DOC_2 = ['i', 'know', 'you', 'are', 'angry']
DOC_3 = ['i', 'was', 'angry', 'at', 'myself']
DOC_4 = ['i', 'get', 'angry', 'when', 'i', 'am', 'hungry']
DOC_5 = ['i', 'was', 'happy', 'when', 'i', 'was', 'able', 'to', 'complete', 'that', 'level', 'in', 'angry', 'birds']
DOC_6 = ['that', 'made', 'me', 'so', 'mad']
DOC_7 = ['i', 'am', 'sorry', 'i', 'got', 'mad']
DOC_8 = ['i', 'am', 'not', 'mad', 'anymore']
COR   = [DOC_0,DOC_1,DOC_2,DOC_3,DOC_4,DOC_5,DOC_6,DOC_7,DOC_8]

# Keyword :
syn_0 = 'angry'
print('the keyword is :', syn_0)
keyword = Word(syn_0)

# Step 1 : Creating Synonym List from Thesaurus
# ---------------------------------------------
SYN = []
for entry in THE:
    if entry.word == keyword.word:
        for syn_i in entry.synonyms:
            if (syn_i != keyword.word):
                #SYN.append(syn_i)
                keyword.add_syn(syn_i)
#print("list of synonyms is :", SYN)
SYN = keyword.synonyms
print("list of synonyms of keyword :", SYN)

# Step 2 : Counting Occurence of Each word in Corpus
# --------------------------------------------------
count_ls = []
for syn_i in SYN:
    count_syn = 0
    for DOC in COR:
        for word in DOC:
            if word == syn_i:
                count_syn = count_syn + 1
    #print(syn_i, count_syn)
    count_ls.append((syn_i, count_syn))

print("occurrence of each synonym :", count_ls)
print("")
