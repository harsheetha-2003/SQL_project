from tkinter import *           # For creating the GUI
from tkinter import scrolledtext # For scrollable text areas in the GUI
import spacy                    # For natural language processing (NLP)
from spacy.lang.en.stop_words import STOP_WORDS # For stop words in NLP
from string import punctuation  # For punctuation removal
from collections import Counter  # For counting word frequencies
from heapq import nlargest       # For extracting the most frequent elements
from transformers import pipeline # For abstractive summarization
import requests                   # For making HTTP requests to fetch web pages
from bs4 import BeautifulSoup    # For parsing HTML content
import webbrowser # For opening URLs in the default web browser

def fetch(topic):
    wiki=wikipediaapi.Wikipedia('en',user_agent='v.harshee.p@gmail.com')
    page=wiki.page(topic)
    if page.exists():
        return page.summary.split('\n')[0] #return the first paragraph
    else:
        return "No information available on this topic."
    
win = Tk()
win.title("EXTRACTIVE AND ABSTRACTIVE SUMMARIZATION")
win.geometry("1500x850")
win.configure(background="Lightyellow")

lbl1 = Label(win, text="TEXT SUMMARIZATION", bg="Green", fg="White",
             height=2, width=55, font=("time", 28, "bold"))
lbl1.place(x=0, y=0)

lbl2 = Label(win, text="ENTER THE TEXT BELOW", bg="purple", fg="White",
             height=1, width=25,font=("time", 18, "bold"))
lbl2.place(x=50, y=110)

lbl3 = Label(win, text="OUTPUT", bg="orange", fg="White",
             height=1, width=18, font=("times", 20, "bold"))
lbl3.place(x=700, y=110)

lbl4 = Label(win, text="ENTER TOPIC", bg="blue", fg="White",
             height=1, width=15, font=("time", 18, "bold"))
lbl4.place(x=20, y=600)


text_input = scrolledtext.ScrolledText(win, wrap=WORD, height=10,width=35, font=("time", 20))
text_input.place(x=20, y=150)

text_output = scrolledtext.ScrolledText(win, wrap=WORD, height=10, width=35, font=("time", 20))
text_output.place(x=600, y=150)


entry_topic = Entry(win,font=("time",20))
entry_topic.place(x=300,y=600)

def options(n):
    if n==1:
        extraction()
    if n==2:
        abstraction()


def extraction():
    text = text_input.get("1.0", END)
    print(text)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    token1 = []
    stopwords = list(STOP_WORDS)
    allowed_pos = ['ADJ', 'PROPN', 'VERB', 'NOUN']
    for token in doc:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in allowed_pos:
            token1.append(token.text)
    print(token1)
    word_freq = Counter(token1)
    print(word_freq)
    max_freq = max(word_freq.values())
    print(max_freq)
    
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq  # normalization
    print(word_freq)
    
    sent_token = [sent.text for sent in doc.sents]
    print(sent_token)
    
    sent_score = {}
    
    for sent in sent_token:
        for word in sent.split():
            if word.lower() in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] += word_freq[word]
            print(word)  # extracting word from sentences
    print(sent_score)
    num_sentences = 3
    n = nlargest(num_sentences, sent_score, key=sent_score.get)
    result = (" ".join(n))
    text_output.insert(END, result)

def abstraction():
    summarizer = pipeline("summarization", model='t5-base',
                          tokenizer='t5-base', framework='pt')
    text = text_input.get("1.0", END)
    print(text)
    summary = summarizer(text, max_length=100, min_length=10, do_sample=False)
    result = summary[0]['summary_text']
    print(result)
    text_output.insert(END, result)

def fetch_and_summarize():
    topic = entry_topic.get().strip()
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.text for para in paragraphs[:5]])
    # Getting the first 5 paragraphs
    text_input.delete("1.0", END)
    text_input.insert(END, text)
    option = int(entry_option.get().strip())
    options(option)

def open_in_browser():
    topic = entry_topic.get().strip()
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    webbrowser.open(url)
    

def options(n):
    if n==1:
        ectraction()
    elif n==2:
        abstraction()
 
btn = Button(win, text="EXTRACTION", bg="Green", fg="White", heigh=1, width=15,
             font=("time", 18, "bold"), command=lambda: extraction())
btn.place(x=20, y=500)

btn1 = Button(win, text="ABSTRACTION", bg="Green", fg="White", heigh=1, width=15,
              font=("time", 18, "bold"), command=lambda: abstraction())
btn1.place(x=280, y=500)

btn2 = Button(win, text="FETCH & SUMMARIZE", bg="Blue", fg="White", heigh=1, width=20,
              font=("time", 18, "bold"), command=lambda: fetch_and_summarize())
btn2.place(x=550, y=500)

btn3 = Button(win, text="OPEN IN BROWSER", bg="Yellow", fg="Black", heigh=1, width=20,
              font=("time", 18, "bold"), command=lambda: open_in_browser())
btn3.place(x=880, y=500)



win.mainloop()
