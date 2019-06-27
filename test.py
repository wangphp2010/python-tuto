'''
import numpy as np  
import seaborn as sns  
import matplotlib.pyplot as plt  
 
sns.set( palette="muted", color_codes=True)  
 
rs = np.random.RandomState(10)  
d = rs.normal(size=100)  
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)  
 
plt.title('seaborn) : statistical data visualization')
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])  
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])  
sns.distplot(d, hist=False, color="g", kde_kws={"shade") : True}, ax=axes[1, 0])  
sns.distplot(d, color="m", ax=axes[1, 1])  
plt.show()  
'''
import re

def getCatId(title)   :
	if re.search( r"face" ,  title , re.IGNORECASE )   :  
		catId = 29
	elif(re.search( "cute", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "S-CUTE", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "女子校生", title , re.IGNORECASE ) ) : 
		catId = 33  
	elif(re.search( "Niece", title , re.IGNORECASE ) ) : 
		catId = 36  
	elif(re.search( "Mouths", title , re.IGNORECASE ) ) : 
		catId = 29  
	elif(re.search( "Housemaid", title , re.IGNORECASE   ) ) : 
		catId = 40  
	elif(re.search( "Humiliation", title , re.IGNORECASE ) ) : 
		catId = 28 
	elif(re.search( "wife", title , re.IGNORECASE ) ) : catId = 32 
	elif(re.search( "Married Woman", title , re.IGNORECASE ) ) : 
		catId = 32 
	elif(re.search( "Schoolgirl", title , re.IGNORECASE ) ) : 
		catId = 33 
	elif(re.search( "Mother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "father", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "brother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "sister", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "teacher", title , re.IGNORECASE ) ) : 
		catId = 37 
	elif(re.search( "rape", title , re.IGNORECASE ) ) : 
		catId = 39 
	elif(re.search( "cute", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "Mature", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Pregnant", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Bibian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( "Lesbian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( " Maid ", title , re.IGNORECASE ) ) : 
		catId = 34 
	elif(re.search( "Big Tits", title , re.IGNORECASE   ) ) : 
		catId = 16 
	elif(re.search( "Creampie", title , re.IGNORECASE ) ) : 
		catId = 22 
	elif(re.search( "Molester",  title , re.IGNORECASE   ) ) : 
		catId = 31  
	elif(re.search( "Molested",  title , re.IGNORECASE   ) ) : 
		catId = 31  
	elif(re.search( "Humiliation", title , re.IGNORECASE ) ) : 
		catId = 28 
	elif(re.search( "wife", title , re.IGNORECASE ) ) : 
		catId = 32 
	elif(re.search( "Married Woman", title , re.IGNORECASE ) ) : 
		catId = 32 
	elif(re.search( "Schoolgirl", title , re.IGNORECASE ) ) : 
		catId = 33 
	elif(re.search( "Mother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "father", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "brother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "sister", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "teacher", title , re.IGNORECASE ) ) : 
		catId = 37 
	elif(re.search( "rape", title , re.IGNORECASE ) ) : 
		catId = 39 
	elif(re.search( "cute", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "Mature", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Pregnant", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Bibian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( "Lesbian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( " Maid ", title , re.IGNORECASE ) ) : 
		catId = 34 
	elif(re.search( "Big Tits", title , re.IGNORECASE ) ) : 
		catId = 16 
	elif(re.search( "Creampie", title , re.IGNORECASE ) ) : 
		catId = 22 
	elif(re.search( "Molester", title , re.IGNORECASE ) ) : 
		catId = 31  
	elif(re.search( "Molester", title , re.IGNORECASE ) ) : 
		catId = 31  
	elif(re.search( "Pervert", title , re.IGNORECASE ) ) : 
		catId = 31  
	elif(re.search( "Uniform", title , re.IGNORECASE ) ) : 
		catId = 19  
	elif(re.search( "Adolescent", title , re.IGNORECASE ) ) : 
		catId = 33  
	elif(re.search( "Middle\-aged", title , re.IGNORECASE ) ) : 
		catId = 24  
	elif(re.search( "Clinic", title , re.IGNORECASE ) ) : 
		catId = 35 
	elif(re.search( "Housewife", title , re.IGNORECASE ) ) : 
		catId = 40 
	elif(re.search( "\bass\b", title , re.IGNORECASE ) ) : 
		catId = 17  
	else  :
		catId = 21 
				
	return str(catId)	

print(getCatId('face') ) 