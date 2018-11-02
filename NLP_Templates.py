#!/usr/bin/env python
# coding: utf-8

# In[ ]:


messages = [line.rstrip() for line in open('path to data set')] #reading a list wth strings
print(len(messages))


# In[ ]:


for message_no, message in enumerate(messages[:10]): #checking the head of data
    print(message_no, message)
    print('\n')


# In[ ]:


messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t', #making panda data fram of the data
                           names=["label", "message"])
messages.head()


# ## Text Pre-processing

# In[ ]:


def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


# In[ ]:


# Check to make sure its working
messages['message'].apply(text_process)


# # Vectorization

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer


# In[ ]:


# Might take awhile...
bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message']) #passing un to the countvectorized we define fun earlier

# Print total number of vocab words
print(len(bow_transformer.vocabulary_))#freequency


# In[ ]:


messages_bow = bow_transformer.transform(messages['message'])#vectorization
print('Shape of Sparse Matrix: ', messages_bow.shape)#shape of vactorization
print('Amount of Non-Zero occurences: ', messages_bow.nnz) # non zero occurance


# In[ ]:


sparsity = (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))
print('sparsity: {}'.format(sparsity))#checking non zero occurance by percent


# # TF-IDF
# So what is TF-IDF?¶
# TF-IDF stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus. Variations of the tf-idf weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance given a user query.
# 
# One of the simplest ranking functions is computed by summing the tf-idf for each query term; many more sophisticated ranking functions are variants of this simple model.
# 
# Typically, the tf-idf weight is composed by two terms: the first computes the normalized Term Frequency (TF), aka. the number of times a word appears in a document, divided by the total number of words in that document; the second term is the Inverse Document Frequency (IDF), computed as the logarithm of the number of the documents in the corpus divided by the number of documents where the specific term appears.
# 
# TF: Term Frequency, which measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided by the document length (aka. the total number of terms in the document) as a way of normalization:
# 
# TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).
# 
# IDF: Inverse Document Frequency, which measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following:
# 
# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
# 
# See below for a simple example.

# In[ ]:


from sklearn.feature_extraction.text import TfidfTransformer
messages_tfidf = tfidf_transformer.transform(messages_bow)#input vactorize form of data
print(messages_tfidf.shape)


# ## Manuall method without pipelines

# ## spliting data,Training a model,classification report

# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB#you can use any model you want 

msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.2)

print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))


spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])


# In[ ]:


from sklearn.metrics import classification_report
print (classification_report(messages['label'], all_predictions))


# 
# 
# ## Creating a Data Pipeline
# 
# Let's run our model again and then predict off the test set. We will use SciKit Learn's [pipeline](http://scikit-learn.org/stable/modules/pipeline.html) capabilities to store a pipeline of workflow. This will allow us to set up all the transformations that we will do to the data for future use. Let's see an example of how it works:

# In[ ]:


from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])


# Now we can directly pass message text data and the pipeline will do our pre-processing for us! We can treat it as a model/estimator API:

# In[ ]:


pipeline.fit(msg_train,label_train)


# In[ ]:


predictions = pipeline.predict(msg_test)


# ## More Resources
# 
# Check out the links below for more info on Natural Language Processing:
# 
# [NLTK Book Online](http://www.nltk.org/book/)
# 
# [Kaggle Walkthrough](https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words)
# 
# [SciKit Learn's Tutorial](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

# In[ ]:




