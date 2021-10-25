#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Assignment-1" data-toc-modified-id="Assignment-1-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><center>Assignment 1</center></a></span><ul class="toc-item"><li><span><a href="#Q1.-Define-a-function-to-create-vocabulary-dictionary-for-an-input-document" data-toc-modified-id="Q1.-Define-a-function-to-create-vocabulary-dictionary-for-an-input-document-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Q1. Define a function to create vocabulary dictionary for an input document</a></span></li><li><span><a href="#Q2.-Define-a-class-to-analyze-a-document-##-(5-points)" data-toc-modified-id="Q2.-Define-a-class-to-analyze-a-document-##-(5-points)-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Q2. Define a class to analyze a document ## (5 points)</a></span></li><li><span><a href="#Q3.-(Bonus)-Create-Bigrams-from-a-document-##-(3-points)" data-toc-modified-id="Q3.-(Bonus)-Create-Bigrams-from-a-document-##-(3-points)-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Q3. (Bonus) Create Bigrams from a document ## (3 points)</a></span></li><li><span><a href="#Submission-Guideline##" data-toc-modified-id="Submission-Guideline##-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Submission Guideline##</a></span></li></ul></li></ul></div>

# # <center>Assignment 1</center>

# In this assignment, you are required to define a class to analyze an article. An sample article is provided. However, your class should be able to analyze any article.

# # Q1. Define a function to create vocabulary dictionary for an input document
#  - Define a function named `tokenize` which does the following:
#      * take a document (i.e. a string) as an input 
#      * split the document into a list of tokens by space (including tab, i.e. `\t`, newline, i.e. `\n`)
#      * remove leading or trailing spaces around each token. 
#      * remove leading or trailing punctuations around each token. However, punctuations are allowed to appear in the middle of a token (e.g. life-saving, didn't).
#      * remove empty tokens, i.e. a token has a least one character
#      * convert all tokens into lower case
#      * return the remaining tokens as a list

# In[3]:


# hint1: If needed, you can use the following to retrieve the list of punctions
import string
print(string.punctuation)

# hint 2: you can use the following to remove leading or trailing punctuations around a token
token = ' (9, 11). '
print(token.strip(string.punctuation+ ' '))
#string.punctuation 指所有标点


# In[18]:


import re;
import string;
from collections import Counter;

def tokenize(document):
    toks = re.split(r'\s', document);
    for i in range(0, len(toks)):
        toks[i] = toks[i].strip(string.punctuation + ' \t\n').lower();
    while '' in toks:
        toks.remove('');
    return toks;

class Doc_Analyzer:
    def __init__(self, document):
        self.tokens = tokenize(document);
        self.vocab = Counter(self.tokens);
    
    def get_doc_length(self):
        return len(self.tokens);

    def get_topN(self, N):
        return sorted(self.vocab.items(), key = lambda x : x[1], reverse = True)[0 : N];

    def get_ngram(self, n_gram, N):
        if n_gram < 1:
            raise ValueError('n_gram should not less than 1');
        elif n_gram == 1:
            return self.get_topN(N);
        ret = self.tokens[0 : len(self.tokens) - n_gram + 1];
        for i in range(1, n_gram):
            tmp = self.tokens[i : len(self.tokens) - n_gram + 1 + i];
            ret = [ret[j] + ' ' + tmp[j] for j in range(0, len(self.tokens) - n_gram + 1)];
        return sorted(Counter(ret).items(), key = lambda x : x[1], reverse = True)[0 : N];


# In[17]:


doc = '''Natural language processing employs computational techniques for the purpose of learning,
understanding, and producing human language content. Early computational approaches to
language research focused on automating the analysis of the linguistic structure of language
and developing basic technologies such as machine translation, speech recognition, and speech
synthesis. Today’s researchers refine and make use of such tools in real-world applications,
creating spoken dialogue systems and speech-to-speech translation engines, mining social
media for information about health or finance, and identifying sentiment and emotion toward
products and services. We describe successes and challenges in this rapidly advancing area. 
         '''

print(tokenize(doc))


# ## Q2. Define a class to analyze a document ## (5 points)
# 
# 
#  - Define a new class called `Doc_Analyzer` as follows: 
#     - it has two attributes:
#         - `tokens`: store the list of tokens as in the order they appear in the document
#         - `vocab`: a dictionary to store the count of each token  
#     - it has an `__init__` function which 
#        - takes a document (i.e. a string) as an input
#        - calls the `tokenize` function that you defined in Q1 to get the list of tokens
#        - store the returned tokens to attribute `tokens`
#        - count each token, and save the frequency of each token into attribute `vocab` such that
#            - each key is a token
#            - the value of each key is the count of the token         
#     - it has a function named `get_doc_length` which returns the total number of tokens in the document
#     - it has a function named `get_topN` which 
#         - takes a number `N` as an input
#         - finds the most frequent `N` words and their counts in the document
#         - returns the words and their counts as a list of tuples
#         
# - Question: What words are frequent? Are you able to get a good idea about the article based on the frequent words? Write your analysis as a pdf file and submit to Canvas

# In[3]:


import re;
import string;
from collections import Counter;

def tokenize(document):
    toks = re.split(r'\s', document);
    for i in range(0, len(toks)):
        toks[i] = toks[i].strip(string.punctuation + ' \t\n').lower();
    while '' in toks:
        toks.remove('');
    return toks;

class Doc_Analyzer:
    def __init__(self, document):
        self.tokens = tokenize(document);
        self.vocab = Counter(self.tokens);
    
    def get_doc_length(self):
        return len(self.tokens);

    def get_topN(self, N):
        return sorted(self.vocab.items(), key = lambda x : x[1], reverse = True)[0 : N];

    def get_ngram(self, n_gram, N):
        if n_gram < 1:
            raise ValueError('n_gram should not less than 1');
        elif n_gram == 1:
            return self.get_topN(N);
        ret = self.tokens[0 : len(self.tokens) - n_gram + 1];
        for i in range(1, n_gram):
            tmp = self.tokens[i : len(self.tokens) - n_gram + 1 + i];
            ret = [ret[j] + ' ' + tmp[j] for j in range(0, len(self.tokens) - n_gram + 1)];
        return sorted(Counter(ret).items(), key = lambda x : x[1], reverse = True)[0 : N];


# In[5]:



analyzer = Doc_Analyzer(doc)

print(analyzer.vocab)

print(analyzer.get_doc_length())

print(analyzer.get_topN(5))


# ## Q3. (Bonus) Create Bigrams from a document ## (3 points)
# 
# A n-gram is n consecutive tokens in a document. Phrases (e.g. data management) are usually frequent n-grams. In the class `Doc_Analyzer`, let's add a function to find phrases.
#  - Create a new function for the class called `get_ngram` as follows :
#      * take two parameters:
#          - `n_gram`: indicate if you want to retrieve phrases in the form of unigram (`n_gram = 1`), bigram (`n_gram = 2`), trigram (`n_gram = 3`) and so on
#          - `N`: top N phrases are returned
#      * slice the `tokens` to get any consecutive `n_gram` tokens if `n_gram > 1`;  if `n_gram == 1` , call `get_topN` as you define in Q2; if `n_gram <1`, `raise ValueError('n_gram should not less than 1')`
#      * count the frequency of each unique phrase
#      * return top N phrases and their counts as a list of tuples
# 
# Question: Are you able to find good phrases from the top N n-grams? Write down your analysis in a document. 

# In[4]:


import re;
import string;
from collections import Counter;

def tokenize(document):
    toks = re.split(r'\s', document);
    for i in range(0, len(toks)):
        toks[i] = toks[i].strip(string.punctuation + ' \t\n').lower();
    while '' in toks:
        toks.remove('');
    return toks;

class Doc_Analyzer:
    def __init__(self, document):
        self.tokens = tokenize(document);
        self.vocab = Counter(self.tokens);
    
    def get_doc_length(self):
        return len(self.tokens);

    def get_topN(self, N):
        return sorted(self.vocab.items(), key = lambda x : x[1], reverse = True)[0 : N];

    def get_ngram(self, n_gram, N):
        if n_gram < 1:
            raise ValueError('n_gram should not less than 1');
        elif n_gram == 1:
            return self.get_topN(N);
        ret = self.tokens[0 : len(self.tokens) - n_gram + 1];
        for i in range(1, n_gram):
            tmp = self.tokens[i : len(self.tokens) - n_gram + 1 + i];
            ret = [ret[j] + ' ' + tmp[j] for j in range(0, len(self.tokens) - n_gram + 1)];
        return sorted(Counter(ret).items(), key = lambda x : x[1], reverse = True)[0 : N];


# In[7]:


# Try the long document: Hirschberg, J. and Manning, C.D., 2015. Advances in natural language processing. Science, 349(6245), pp.261-266.
doc = open("hw1_test_doc.txt","r", encoding='utf-8').read()

analyzer = Doc_Analyzer(doc)
print(analyzer.get_ngram(1, 5))
print(analyzer.get_ngram(2, 5))
print(analyzer.get_ngram(3, 5))
# print(analyzer.get_ngram(0, 5))


# ## Submission Guideline##
# - Following the solution template provided below. Use __main__ block to test your functions and class？？
# - Save your code into a python file (e.g. assign1.py) that can be run in a python 3 environment. In Jupyter Notebook, you can export notebook as .py file in menu "File->Download as".
# - Make sure you have all import statements. To test your code, open a command window in your current python working folder, type "python assign1.py" to see if it can run successfully.？？
# - For more details, check assignment submission guideline on Canvas

# In[ ]:


# Structure of your solution to Assignment 1 

import string

# define your function and class here

# best practice to test your class
# if your script is exported as a module,
# the following part is ignored
# this is equivalent to main() in Java

if __name__ == "__main__":  
    
    # Test Question 1
    doc = '''Natural language processing employs computational techniques for the purpose of learning,
understanding, and producing human language content. Early computational approaches to
language research focused on automating the analysis of the linguistic structure of language
and developing basic technologies such as machine translation, speech recognition, and speech
synthesis. Today’s researchers refine and make use of such tools in real-world applications,
creating spoken dialogue systems and speech-to-speech translation engines, mining social
media for information about health or finance, and identifying sentiment and emotion toward
products and services. We describe successes and challenges in this rapidly advancing area. 
         '''

    print("Test Question 1")
    print(tokenize(doc))
    
    
    # Test Question 2
    print("\nTest Question 2")
    
    analyzer = Doc_Analyzer(doc)

    print("vocabulary: \n", analyzer.vocab)

    print("doc length: \n", analyzer.get_doc_length())

    print("top 5 words: \n", analyzer.get_topN(5))
    
    # Note that top words are not very meaningful. 
    # They are called stop words
    
    #3 Test Question 3
    print("\nTest Question 3")
    
    doc = open("hw1_test_doc.txt","r", encoding='utf-8').read()

    analyzer = Doc_Analyzer(doc)
    
    print("top 5 bigrams: \n", analyzer.get_ngram(2, 5))
    print("top 5 trigrams: \n", analyzer.get_ngram(3, 5))
    
    


# In[ ]:




