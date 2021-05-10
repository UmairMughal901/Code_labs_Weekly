#!/usr/bin/env python
# coding: utf-8

# # <font style=color:Red>Complete Guide for Python Basic</font>

# # STRING OPERATIONS

# ### What is sting?

# In[2]:


#String is collection of words as givern below.
"Umair Asghar"


# We can use single quotation marks too.

# In[3]:


'Umair Asghar'


# String can be space or digits

# In[4]:


'Umair 1 2 3 4 5 6 9'


# String can be special characters.

# '@#$%^&*()_'

# How to print the string?

# In[8]:


print ('How to print the string')


# We can bind or assign a string to another variable:

# In[26]:


name = 'Uamir Asgahr'
print(name)
#or simpel use name to print the statement.
name


# # Indexing

# It is helpful to think of a string as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers:  

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsIndex.png" width="600" align="center" />
# 

# In[10]:


# Print the first element in the string

print(name[0])


# In[11]:


# we can print index 6

print(name[6])


# In[14]:


print(name[11])


# ## Negative Indexing
# We can also use negative indexing with strings:

# In[15]:


print(name[-1])


# In[17]:


print(name[-11])


# ## Find the length of the string.

# In[18]:


len("Umair Asgahr")


# # Slicing
# We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th to the 12th element:

# In[19]:


name [0:5]


# In[20]:


name [6:12]


# # Stride
# We can also input a stride value as follows, with the '2' indicating that we are selecting every second variable:

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsStride.png" width="600" align="center" />
# 

# In[23]:


name[::3]


# In[24]:


name[0:5:2]


# # Concatenate Strings
# We can concatenate or combine strings by using the addition symbols, and the result is a new string that is a combination of both:

# In[25]:


# Concatenate two strings

statement = name + "is the best"
statement


# To replicate values of a string we simply multiply the string by the number of times we would like to replicate it. In this case, the number is three. The result is a new string, and this new string consists of three copies of the original string:

# In[29]:


6*name


# You can create a new string by setting it to the original variable. Concatenated with a new string, the result is a new string that changes from Michael Jackson to “Michael Jackson is the best".

# In[31]:


changestring = name + ' is the great man.'
changestring


# # Escape Sequences
# Back slashes represent the beginning of escape sequences. Escape sequences represent strings that may be difficult to input. For example, back slash "n" represents a new line. The output is given by a new line after the back slash "n" is encountered:

# In[32]:


#line escape
print ('Umair Asghar is a \n Py developer')


# In[34]:


# tab escape
print ('Umair Asgahr is not a \t king py developer')


# In[35]:


#include backslash
print ('Umair Asgahr is including \\ in the statement.')


# In[37]:


#how to show string as it is. Its raw string use r in start of string.
print (r'Umair Asghar is nothing but a  \ py developer')


# # String Operations
# There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the data.
# 
# Let's try with the method upper; this method converts lower case characters to upper case characters:

# In[ ]:





# In[38]:


# Convert all the characters in string to upper case

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)


# ## Replace function

# In[39]:


a = 'Umair Asghar is a great py developer'
b = a.replace('great','greatest')
b


# In[41]:


#find
name.find('UA')


# In[43]:


# Find the substring in the string.

name.find('Umair')


# In[44]:


# If cannot find the substring in the string

name.find('Jasdfasdasdf')


# # Lists in Python

# ## Objectives
# After completing this lab you will be able to:
# 
# Perform list operations in Python, including indexing, list manipulation and copy/clone list.

# ### About the Dataset
# Imagine you received album recommendations from your friends and compiled all of the recommandations into a table, with specific information about each album.
# 
# The table has one row for each movie and several columns:
# 
# * artist - Name of the artist
# * album - Name of the album
# * released_year - Year the album was released
# * length_min_sec - Length of the album (hours,minutes,seconds)
# * genre - Genre of the album
# * music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
# * claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
# * date_released - Date on which the album was released
# * soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
# * rating_of_friends - Indicates the rating from your friends from 1 to 10

# Imagine you received album recommendations from your friends and compiled all of the recommandations into a table, with specific information about each album.
# 
# The table has one row for each movie and several columns:
# 
# -   **artist** - Name of the artist
# -   **album** - Name of the album
# -   **released_year** - Year the album was released
# -   **length_min_sec** - Length of the album (hours,minutes,seconds)
# -   **genre** - Genre of the album
# -   **music_recording_sales_millions** - Music recording sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/?utm_email=Email&utm_source=Nurture&utm_content=000026UJ&utm_term=10006555&utm_campaign=PLACEHOLDER&utm_id=SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395)
# -   **claimed_sales_millions** - Album's claimed sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/?utm_email=Email&utm_source=Nurture&utm_content=000026UJ&utm_term=10006555&utm_campaign=PLACEHOLDER&utm_id=SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395)
# -   **date_released** - Date on which the album was released
# -   **soundtrack** - Indicates if the album is the movie soundtrack (Y) or (N)
# -   **rating_of_friends** - Indicates the rating from your friends from 1 to 10
#     <br>
#     <br>
# 
# The dataset can be seen below:
# 
# <font size="1">
# <table font-size:xx-small>
#   <tr>
#     <th>Artist</th>
#     <th>Album</th> 
#     <th>Released</th>
#     <th>Length</th>
#     <th>Genre</th> 
#     <th>Music recording sales (millions)</th>
#     <th>Claimed sales (millions)</th>
#     <th>Released</th>
#     <th>Soundtrack</th>
#     <th>Rating (friends)</th>
#   </tr>
#   <tr>
#     <td>Michael Jackson</td>
#     <td>Thriller</td> 
#     <td>1982</td>
#     <td>00:42:19</td>
#     <td>Pop, rock, R&B</td>
#     <td>46</td>
#     <td>65</td>
#     <td>30-Nov-82</td>
#     <td></td>
#     <td>10.0</td>
#   </tr>
#   <tr>
#     <td>AC/DC</td>
#     <td>Back in Black</td> 
#     <td>1980</td>
#     <td>00:42:11</td>
#     <td>Hard rock</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td></td>
#     <td>8.5</td>
#   </tr>
#     <tr>
#     <td>Pink Floyd</td>
#     <td>The Dark Side of the Moon</td> 
#     <td>1973</td>
#     <td>00:42:49</td>
#     <td>Progressive rock</td>
#     <td>24.2</td>
#     <td>45</td>
#     <td>01-Mar-73</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Whitney Houston</td>
#     <td>The Bodyguard</td> 
#     <td>1992</td>
#     <td>00:57:44</td>
#     <td>Soundtrack/R&B, soul, pop</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td>Y</td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Meat Loaf</td>
#     <td>Bat Out of Hell</td> 
#     <td>1977</td>
#     <td>00:46:33</td>
#     <td>Hard rock, progressive rock</td>
#     <td>20.6</td>
#     <td>43</td>
#     <td>21-Oct-77</td>
#     <td></td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Eagles</td>
#     <td>Their Greatest Hits (1971-1975)</td> 
#     <td>1976</td>
#     <td>00:43:08</td>
#     <td>Rock, soft rock, folk rock</td>
#     <td>32.2</td>
#     <td>42</td>
#     <td>17-Feb-76</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Bee Gees</td>
#     <td>Saturday Night Fever</td> 
#     <td>1977</td>
#     <td>1:15:54</td>
#     <td>Disco</td>
#     <td>20.6</td>
#     <td>40</td>
#     <td>15-Nov-77</td>
#     <td>Y</td>
#     <td>9.0</td>
#   </tr>
#     <tr>
#     <td>Fleetwood Mac</td>
#     <td>Rumours</td> 
#     <td>1977</td>
#     <td>00:40:01</td>
#     <td>Soft rock</td>
#     <td>27.9</td>
#     <td>40</td>
#     <td>04-Feb-77</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
# </table></font>
# 

# # Lists
# ## Indexing
# We are going to take a look at lists in Python. A list is a sequenced collection of different objects such as integers, strings, and other lists as well. The address of each element within a list is called an index. An index is used to access and refer to items within a list.

# In[8]:


#create list
mylist = ['umair asghar','23','56.8']
mylist


# In[14]:


# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',mylist[0],
'\n Negative:' , mylist[-3]  )
print('the same element using negative and positive indexing:\n Postive:',mylist[1],
'\n Negative:' , mylist[-2]  )
print('the same element using negative and positive indexing:\n Postive:',mylist[2],
'\n Negative:' , mylist[-1]  )


# #### List Content
# Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. The same indexing conventions apply for nesting:

# In[21]:


# Sample List

newL = ["Umair Asghar", 26.1, 1985, [1, 2], ("N", 1)]
newL


# # List Operations
# We can also perform slicing in lists. For example, if we want the last two elements, we use the following command:

# In[24]:


newL[3:5]


# ## method extend

# In[33]:


# Use extend to add elements to list

List = ["Sting is here",45,2532.2]
List.extend(['newstring',235146])
List


# ### Another similar method is append. If we apply append instead of extend, we add one element to the list:

# In[34]:


List = ["Sting is here",45,2532.2]
List.append(['newstring',235146])
List


# #### Each time we apply a method, the list changes. If we apply extend we add two new elements to the list. The list List is then modified by adding two new elements

# In[36]:


# Use extend to add elements to list

List = ["Sting is here",45,2532.2]
List.extend(['newstring',235146])
List


# ## If we append the list ['a','b'] we have one new element consisting of a nested list:

# In[37]:


# Use append to add elements to list

List.append(['a','b'])
List


# ### As lists are mutable, we can change them. For example, we can change the first element as follows:

# In[38]:


# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


# ### <code style=color:Blue>del</code> command

# In[39]:


# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)


# #### <code>split</code>

# In[40]:


# Split the string, default is by space

'hard rock'.split()


# ##### We can use the split function to separate strings on a specific character. We pass the character we would like to split on into the argument, which in this case is a comma. The result is a list, and each element corresponds to a set of characters that have been separated by a comma:

# In[42]:


# Split the string by comma

'A,B,C,D'.split(',')


# #### Copy and Clone List

# In[43]:


# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


# In[44]:


<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsVal.gif" width="1000" />


# In[45]:


print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])


# <font style=color:blue><h1> Difference Between Tuple and List </h1></font>

# the tuples cannot be changed unlike lists, and tuples use parentheses, whereas lists use square brackets.
# 
# what is the result of the

# In[ ]:





# In[ ]:




