
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# You survey households in your area to find the average rent they are paying. Find the standard deviation from the following data: $1550, $1700, $900, $850, $1000, $950.


# In[3]:


x = [1550,1550,1700,1700,900,900,850,850,1000,1000,950]
Avg_rent_paid = np.mean(x)
std_dev = np.std(x)

print('Average rent paid by the households for the sample information collected : {:0.2f}'.format(Avg_rent_paid))
print('The limits of data perating to rent paid by the households is +/- : {:0.2f}'.format(std_dev))


# In[4]:


# Find the variance for the following set of data representing trees in California (heights in feet): 3, 21, 98, 203, 17, 9


# In[5]:


#x : height of trees in feet

x = [3,21,98,203,17,9]
variance = np.var(x)

print("The spread of data representing trees in california(heights in feet): {:0.2f}".format(variance))


# In[6]:


# In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects and 3 failed in three subjects. Find the probability distribution of the variable for number of subjects a student from the given class has failed in.


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
n_students = 100
passed_all = 80
failed_one = 10
failed_two = 7
failed_three = 3

num_students_not_passed_all = n_students - passed_all
prob_failed_none = passed_all / n_students
prob_failed_in_one = failed_one / n_students
prob_failed_in_two = failed_two / n_students
prob_failed_in_three = failed_three / n_students

print("Probability failed in no subjects : ", prob_failed_none)
print("Probability failed in one subjects : ", prob_failed_in_one)
print("Probability failed in two subjects :  ", prob_failed_in_two)
print("Probability failed in three subjects : ", prob_failed_in_three)

