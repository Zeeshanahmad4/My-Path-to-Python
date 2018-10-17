#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#spliting data
import sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived',axis=1), 
                                                    train['Survived'], test_size=0.30, 
                                                    random_state=101)


# In[ ]:


#fitting model
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)


# In[ ]:


#Predicting
predictions = logmodel.predict(X_test)


# # Evaluation

# In[ ]:


#classifier report 
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))


# In[ ]:


#confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,pre)

