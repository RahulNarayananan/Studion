import nltk 
from nltk.corpus import stopwords 
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import word_tokenize, sent_tokenize 
from braille.main import open_text as ot
from tkinter import messagebox

def generate_summary(filename):
    
    # Input text - to summarize  
    with open(filename,'r') as f:
        text = f.read()
    
    # Tokenizing the text 
    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 
    
    # Creating a frequency table to keep the  
    # score of each word 
    
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1
    
    # Creating a dictionary to keep the score 
    # of each sentence 
    sentences = sent_tokenize(text) 
    sentenceValue = dict() 
    
    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq 
    
    
    
    sumValues = 0
    for sentence in sentenceValue: 
        sumValues += sentenceValue[sentence] 
    
    # Average value of a sentence from the original text 
    
    average = int(sumValues / len(sentenceValue)) 
    
    # Storing sentences into our summary. 
    summary = '' 
    newfile = 'sum_'+filename
    for sentence in sentences: 
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
            summary += " " + sentence 
    if summary != '' or len(summary) >= 17:
        pass
    else:
        summary = text

    with open(newfile, 'w+') as f:
        f.write(summary)
    print('\n\nText Summary Generated\n\n')

    ot(newfile)
    print('\n\nBraille Summary File Created\n\n')

    messagebox.showinfo('DONE','COMMAND EXECUTED SUCCESSFULY!!')

# let's begin
if __name__ == "__main__":
    generate_summary(input('Enter file name\n>> '))
