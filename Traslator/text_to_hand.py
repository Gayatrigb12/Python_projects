import pywhatkit as pw 
txt ="""
NLP is a machine learning technology that gives machines the ability to interpret and manipulate 
human language. NLP does this by analyzing the data, intent, or sentiment in the message and responding to human communication. Typically, NLP implementation begins by gathering and preparing 
unstructured text or speech data from different sources and processing the data. It uses techniques 
such as tokenization, stemming, lemmatization, stop word removal, part-of-speech tagging, named entity recognition, speech recognition, sentiment analysis, and so on. However, modern LLMs don't require using these intermediate steps."""


pw.text_to_handwriting(txt,"demo1.png", [0,0,135]) # text , filename , color code 
print("-----END-------")