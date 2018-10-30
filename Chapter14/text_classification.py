
from sklearn.datasets import fetch_20newsgroups 


categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med'] 

training_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42) 

print(len(training_data)) 

print(set(training_data.target)) 

sentence_1 = "as fit as a fiddle "
sentence_2 = "as you like it"

set((sentence_1 + sentence_2).split(" "))
    
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.naive_bayes import MultinomialNB 
count_vect = CountVectorizer() 
training_matrix = count_vect.fit_transform(training_data.data) 
    
matrix_transformer = TfidfTransformer() 
tfidf_data = matrix_transformer.fit_transform(training_matrix) 

print(tfidf_data)
print(tfidf_data[1:4].todense()) 
    
model = MultinomialNB().fit(tfidf_data, training_data.target) 
     
test_data = ["My God is good", "Arm chip set will rival intel"] 
test_counts = count_vect.transform(test_data) 
new_tfidf = matrix_transformer.transform(test_counts) 
    
prediction = model.predict(new_tfidf)  
        
for doc, category in zip(test_data, prediction): 
        print('%r => %s' % (doc, training_data.target_names[category])) 