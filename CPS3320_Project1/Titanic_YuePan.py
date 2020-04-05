import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time



train_data = pd.read_csv('/Users/nina/Desktop/CPS3320_Project1/train.csv')
#survival rate
survival = 0
died = 0
for n in train_data['Survived']:
    if n == 0:
        died = died +1
    elif n ==1:
        survival = survival + 1
labels = ['died','survival']
values = [died, survival]
plt.pie(values,labels = labels,autopct='%1.2f%%',colors=['salmon','paleturquoise'])
plt.axis('equal')
print('Survival rate is 40.62%')
plt.show()

# 1st part
train_data_age = train_data[train_data['Age'].notnull()]
plt.figure(figsize=(12,5))
plt.subplot(121)
train_data_age['Age'].hist(bins=70,color='lightskyblue')
plt.xlabel('Age')
plt.ylabel('Num')
plt.suptitle('Age Distribution')
 
plt.subplot(122)
train_data.boxplot(column='Age',showfliers=False)
print('Overall the age distribution: after removing the missing value,\
the sample had 714 , the mean age was about 30, the standard deviation was 14, \
the minimum age was 0.42, and the maximum age was 80.')
train_data_age['Age'].describe()
plt.show() 

# 2nd part
train_data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar()
survive_sex = train_data.groupby(['Sex','Survived'])['Survived'].count()
print(survive_sex)
# Women have higher survival rates

print('The survival rate for women is %.2f%%，The survival rate for men is %.2f%%' % 
     (survive_sex.loc['female',1]/survive_sex.loc['female'].sum()*100, survive_sex.loc['male',1]/survive_sex.loc['male'].sum()*100))
plt.show()

# 3rd part
train_data_age = train_data[train_data['Fare'].notnull()]

plt.figure(figsize=(12,5))
plt.subplot(121)
train_data_age['Fare'].hist(bins=70,color='lightsalmon')
plt.xlabel('Fare')
plt.ylabel('Num')
plt.suptitle('Fare Distribution')
plt.show()
#This graph is not representative and it's hard to see which fare group has higher survival rate
#I will draw the survival rate group by the ticket class, so it will be easy to find which ticket class has a higher survival rate
fig,ax = plt.subplots(1,2, figsize = (18,8))

sns.violinplot("Pclass","Age",hue="Survived",data=train_data_age,split=True,ax=ax[0])
ax[0].set_title('Pclass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
print('According to different cabin grades → \
the higher cabin grades are, the higher the survive rate is.\
the higher cabin grades are, the older the survivors are. \
Cabin grade 1 survival age is mainly between 20 and 40 years old, and more young passengers survive in 2/3 cabin grades')

sns.violinplot("Sex","Age",hue="Survived",data=train_data_age,split=True,ax=ax[1])
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0,110,10))
print('→ male and female survivors are mainly distributed in 20-40 years old, \
and there are more young passengers, among which female survivors are more')
plt.show()
print('In conclusion, buying 1st ticket class, older women passengers are more likely to survive.')
