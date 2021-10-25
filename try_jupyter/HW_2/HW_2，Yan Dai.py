#!/usr/bin/env python
# coding: utf-8

# # <center>HW 2: Numpy Array and DataFrames</center>

# ## Q1. Define a function to analyze a numpy array 
# - **Q1.1**. Assume we have an array, named `dtm`, which contains word frequency of each document. In this array, each row represents a document, each column represents a word, and the value denotes the frequency of the word in the document. Define a function named `analyze_tf` which does the following: 
#     * Take two input parameters:
#         - `dtm`: the input `dtm` with a shape `(m, n)`
#         - `binarized`: a boolean argument. The default value is `False`
#     * If `binarized = True`, set an array value to 1 if it is positive and 0 otherwise. 
#     * Normalize each value, say $v_{i,j}$, as $v_{i,j}$ divided by the sum of row $i$. Save the result as `tf`. 
#     * Calculate the document frequency (`df`) of each word as the number of documents containing the word
#     * Calcuate the inverse document frequency (`idf`) as $\frac{m}{df}$, where $m$ is the total number of documents.
#     * Calculate `tf_idf` array as: $tf * (\log(idf) + 1) $. Specifically, the `tf_idf` value of a word in a document is its `tf` value multiplied by its logged `idf` value added by 1.  
#     * Return the `df` and `tf_idf` arrays.
#     
#  
# - **Q1.2**. Define a function `show_top_df_words` as follows:
#     - Take `df` and `word_dict`, a dictionary which maps an index to a word, as the inputs
#     - Print out the indexes of words with top 3 largest `df` values
#     - print out the words corresponding to these indexes.
#     
#     
# - **Q1.3**. Define a function `show_top_tf_idf_words` as follows:
#     - Take `tf_idf`, a row index `row_id`, and `word_dict`, a dictionary which maps an index to a word, as the inputs
#     - Print out the indexes of the words with top 5 largest `tf_idf` values for the `row_id` row.
#     - Print out the words corresponding to these indexes.
#           
#       
# - **Note**
#      - For all the steps, `do not use any loop`. Just use array functions and broadcasting for high performance computation.
#      - Test your function with `binarized = True or False`. Make sure it works in both scenarios
#      - For your testing, a `dtm` array and a dictionary which maps each column index to a word are provided. See below to load the test files.
# 

# In[13]:


import numpy as np
import pandas as pd
import pickle
from matplotlib import pyplot as plt
from itertools import combinations

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

np.set_printoptions(precision=4)
pd.set_option('precision', 4)


# In[17]:


def analyze_tf(arr, binarized=False):
    arr_bin = (arr > 0).astype(np.int_)

    if binarized:
        tf = arr_bin / np.sum(arr_bin, axis=1).reshape((-1,1))
    else:
        tf = arr / np.sum(arr, axis=1).reshape((-1,1))
    df = np.sum(arr_bin, axis=0)
    idf = arr.shape[0] / df
    
    tf_idf = tf * (np.log(idf) + 1)

    return df, tf_idf

def show_top_df_words(df, word_dict):
    num = 3
    ind = np.flip(np.argsort(df)[-num:])

    print(f'top 3 df indexes:  {ind}')
    print(f'''top 3 df words:  [{', '.join(map(lambda x: f"'{x}'", np.array(word_dict)[ind]))}]''')

def show_top_tf_idf_words(tf_idf, row_id, word_dict):
    row = tf_idf[row_id]
    num = 5
    ind = np.flip(np.argsort(row)[-num:])

    print(f'top 5 tf_idf indexes:  {ind}')
    print(f'''top 5 tf_idf words:  [{', '.join(map(lambda x: f"'{x}'", np.array(word_dict)[ind]))}]''')


# In[18]:


# array for testing
dtm = np.load("dtm.npy")
print(dtm.shape)

# a mapping from column index to words
word_dict = pickle.load(open("words.dict", 'rb'))

# pick any index and show the word at this index
idx = 50
print("words at index {0} is: {1} ".format(idx, word_dict[idx]))


# In[19]:


# Testing:

# binarize = False
print("\n testing binarize = False")
df, tf_idf = analyze_tf(dtm, binarized=False)
show_top_df_words(df, word_dict)

row_id = 1
show_top_tf_idf_words(tf_idf, row_id, word_dict)

print("\n testing binarize = True")
df, tf_idf = analyze_tf(dtm, binarized=True)
show_top_df_words(df, word_dict)

row_id = 1
show_top_tf_idf_words(tf_idf, row_id, word_dict)


# ## Q2. Define a function to analyze Pandas DataFrame 
# 
# Suppose you are classifying the sentiment of documents as positive or negative. Your machine learning model returns a probability of being positive for each document, denoted as `pred`. You also know the ground truth label of each document (0: negative and 1: positive), denoted as `truth`. Both `pred` and `truth` are numpy arrays.
# 
# - **Q2.1**. Write a function `analyze_performance` to do the following:
#     - Take `pred`, `truth`, and a threshod, say `thresh` as inputs
#     - Create a DataFrame with `pred` and `truth` as two columns
#     - Create a new column `binary_pred` which sets prediction to 1 if `pred > thresh`, and 0 otherwise
#     - Calculate a confusion table (pivot table or cross tabulation) as `[[TN, FP],[FN,TP]]`, where:
#         * True Positives (TP): the number of correct positive predictions
#         * False Positives (FP): the number of postive predictives which actually are negatives
#         * True Negatives (TN): the number of correct negative predictions
#         * False Negatives (FN): the number of negative predictives which actually are positives
#     - Calculate precision as $TP/(TP+FP)$ and recall as $TP/(TP+FN)$ for the positive class.
#     - return the confusion table, precision, and recall
#     
#     
# - **Q2.2**. Write a function `show_impact_of_threshold` as follows:
#     - Take `pred` and `truth` as inputs
#     - Call `analyze_performance` funtion by varying `thresh` from 0.05 to 0.95 with an increase of 0.05 each time. 
#     - Plot a line chart to see how precision and recall change by `thresh`.
#     - This function has no return. Just print out two lines in a plot.
#     
# - Hint: `don't use any loop`. Just use functions from numpy or Pandas packages

# In[22]:


def analyze_performance(pred, truth, thresh):
    df = pd.DataFrame({'pred': pred, 'truth': truth})
    df['binary_pred'] = (df['pred'] > thresh).astype(np.int_)

    confusion = pd.crosstab(df['truth'], df['binary_pred'])
    TP = confusion[1][1]
    FN = confusion[0][1]
    FP = confusion[1][0]
    prec = TP / (TP + FP)
    rec = TP / (TP + FN)
    
    return confusion, prec, rec

def show_impact_of_threshold(pred, truth):
    thresholds = np.linspace(0.05, 0.95, num=round((1-0.05)/0.05))
    prec_rec = map(lambda x: analyze_performance(pred, truth, x)[1:], thresholds)
    df = pd.DataFrame(prec_rec, columns=['prec', 'rec'])
    
    plt.plot(thresholds, df['prec'], label='precision')
    plt.plot(thresholds, df['rec'], label='recall')
    plt.xlabel('threshold')
    plt.legend(loc='lower left')
    plt.ylim([0,1.05])
    plt.show()


# In[23]:


# Testing arrays
pred = np.array([0.28997326, 0.10166073, 0.10759583, 0.0694934, 0.6767239,
                0.01446897, 0.15268748, 0.15570522, 0.12159665, 0.22593857,
                0.98162019, 0.47418329, 0.09376987, 0.80440782, 0.88361167,
                0.21579844, 0.72343069, 0.06605903, 0.15447797, 0.10967575,
                0.93020135, 0.06570391, 0.05283854, 0.09668829, 0.05974545,
                0.04874688, 0.07562255, 0.11103822, 0.71674525, 0.08507381,
                0.630128, 0.16447478, 0.16914903, 0.1715767, 0.08040751,
                0.7001173, 0.04428363, 0.19469664, 0.12247959, 0.14000294,
                0.02411263, 0.26276603, 0.11377073, 0.07055441, 0.2021157,
                0.11636899, 0.90348488, 0.10191679, 0.88744523, 0.18938904])

truth = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0,
                  0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 1, 0, 1, 0])


# In[24]:


conf, prec, rec = analyze_performance(pred, truth, 0.5)

conf

print("precision: {0: .4f}, recall: {1: .4f}".format(prec, rec))

show_impact_of_threshold(pred, truth)


# ## Q3 (Bonus). Find Coocurring Words
# 
# If two words frequently cooccur in a document (they don't have to be located next to each other), they may be semantically connected. For example, you may see words like "finance" and "stock" frequency cooccur in financial documents. 
# 
# Define a function `find_cooccur_words(dtm, word_dict, topN)` to:
# - find the `topN` pairs of cooccuring words in a given `dtm` (defined in Q1)
# - print out the word pairs using the `word_dict` dictionary. 
# 
# Hints:
# - You can select coocurring words using metrics measuring words dependencies, such as Jaccard index, Pointwise Mutual Information, etc. Do your research to find these metrics.
# - There is no unique solution to this question. You'll receive credits as long as your solution makes sense. You can write a few lines to explain your solution.
# - Again, `don't use any loop` to find the top N word pairs. But you can use loop when you print out the found word pairs.

# In[25]:


def find_cooccur_words(dtm, word_dict, topN=10):
    
    # add your code here
    p = np.sum(dtm, axis=0)
    p = p / sum(p)

    def pxy(x,y):
        return (len(list(filter(lambda s :  s[x] > 0 and s[y] > 0, dtm)))+1) / float(len(dtm))

    def pmi(t):
        x = t[0]
        y = t[1]
        return np.log(pxy(x,y)/(p[x]*p[y]))

    word_idx_list = list(range(len(word_dict)))
    comb = list(combinations(word_idx_list, 2))
    scores = list(map(pmi, comb))

    ind = np.flip(np.argsort(scores)[-topN:])
    print([(word_dict[comb[i][0]], word_dict[comb[i][1]]) for i in ind])  


# In[26]:


dtm = np.load("dtm.npy")
word_dict = pickle.load(open("words.dict", 'rb'))

# There is no unique solution. 
# So reference solution is not provided

find_cooccur_words(dtm, word_dict, topN=10)


# ## Submission Guideline ##
# - Following the solution template provided below. Use __main__ block to test your functions and class
# - Save your code into a python file (e.g. assign1.py) that can be run in a `python 3` environment. In Jupyter Notebook, you can export notebook as .py file in menu "File->Download as".
# - Make sure you have all import statements. To test your code, open a command window in your current python working folder, type "python assign1.py" to see if it can run successfully with the expected result printed.

# In[28]:




if __name__ == "__main__":  
    
    # Test Question 1
    
    print("==== Q1 ========")
    # array for testing
    dtm = np.load("dtm.npy")

    # a mapping from column index to words
    word_dict = pickle.load(open("words.dict", 'rb'))
    
    print("testing binarize = False")
    df, tf_idf = analyze_tf(dtm, binarized=False)
    show_top_df_words(df, word_dict)

    row_id = 1
    show_top_tf_idf_words(tf_idf, row_id, word_dict)

    print("\n")
    print("testing binarize = True")
    df, tf_idf = analyze_tf(dtm, binarized=True)
    show_top_df_words(df, word_dict)

    row_id = 1
    show_top_tf_idf_words(tf_idf, row_id, word_dict)
    
    print("\n")
    
    
    # Test Question 2
    print("==== Q2 ========")
    # Testing arrays
    pred = np.array([0.28997326, 0.10166073, 0.10759583, 0.0694934, 0.6767239,
                0.01446897, 0.15268748, 0.15570522, 0.12159665, 0.22593857,
                0.98162019, 0.47418329, 0.09376987, 0.80440782, 0.88361167,
                0.21579844, 0.72343069, 0.06605903, 0.15447797, 0.10967575,
                0.93020135, 0.06570391, 0.05283854, 0.09668829, 0.05974545,
                0.04874688, 0.07562255, 0.11103822, 0.71674525, 0.08507381,
                0.630128, 0.16447478, 0.16914903, 0.1715767, 0.08040751,
                0.7001173, 0.04428363, 0.19469664, 0.12247959, 0.14000294,
                0.02411263, 0.26276603, 0.11377073, 0.07055441, 0.2021157,
                0.11636899, 0.90348488, 0.10191679, 0.88744523, 0.18938904])

    truth = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0,
                  0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 1, 0, 1, 0])
    
    conf, prec, rec = analyze_performance(pred, truth, 0.5)

    print(conf)
    print("precision: {0: .4f}, recall: {1: .4f}".format(prec, rec))

    show_impact_of_threshold(pred, truth)
    
    
    #3 Test Question 3
    


# In[ ]:





# In[ ]:




