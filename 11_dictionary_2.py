ai = {"name":"ChatGPT","developer":"OpenAI","type":"AI chatbot","release_year":2022,"language_model":"GPT","capabilities":"text generation","supports_languages":"multiple","platform":"web and mobile","use_cases":"education, coding, writing","interaction_style":"conversational","availability":"24/7","learning_type":"machine learning","model_family":"transformer","input_type":"text and image","output_type":"text","updates":"regular","access":"internet-based","purpose":"assist users","license":"proprietary","website":"[https://chat.openai.com"}
print(ai)
# copy_ai = ai #wrong way
copy_ai = ai.copy()
copy_ai.clear() #remove all key value pair from ai dictionary 
print(ai)
print(ai.keys()) #print all keys only
print(ai.values()) #print only values
print(ai.items()) #print key value pair as object
print(ai.get('name')) #display value of specific key
print(ai.get('author')) #display value of specific key
# print(ai['name'],ai['author']) #display value of specific key
ai.pop('license')
ai.popitem() 
print(ai)
ai.update({'author':'many','input_type':'any'})
print(ai)