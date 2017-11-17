### Pie Chart
### Bar Graph

~~~python
f,ax=plt.subplots(1,2,figsize=(18,8))
data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
sns.countplot('Survived',data=data,ax=ax[1])
ax[1].set_title('Survived')
plt.show()
~~~

![Pie and Bar](matplotlib_images/pie_bar.png)

### Seaborn Countplot

~~~python
f,ax=plt.subplots(1,2,figsize=(18,8))
data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax=ax[0])
ax[0].set_title('Survived vs Sex')
sns.countplot('Sex',hue='Survived',data=data,ax=ax[1])
ax[1].set_title('Sex:Survived vs Dead')
plt.show()
~~~

![Countplot](matplotlib_images/countplot.png)

### Crosstab

~~~python
pd.crosstab(data.Pclass, data.Survived, margins=True).style.background_gradient(cmap='summer_r')
~~~

![Crosstab](matplotlib_images/crosstab.png)

### Factor Plot

~~~python
sns.factorplot('Pclass', 'Survived', hue='Sex', data = data)
~~~
![factor Plot](matplotlib_images/factorplot.png)
