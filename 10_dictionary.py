#dictionary with tuples and list and scaler values 
book = {} #empty dictionary
print(book)

#adding scaler(single) value
book['name'] = 'AI/ML/DS'
book['price'] = 1000
book['author'] = "Ankit Patel"

print(book)
#add tuple into dictionary
book['chapters'] = (1,2,3,4) 

#add list into dictionary
book['topics'] = ['Python','Machine Learning','Data Science','Interview prep']
print(book)

#update value using key
book['name'] = 'Introduction to AI/ML/DS'
print(book)