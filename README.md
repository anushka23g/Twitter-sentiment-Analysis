# SENTIMENT ANALYSIS IN TWITTER
<br>

 ## ABSTRACT<br>
In this project we have built a model which takes a dataset as an input andas an output gives the percentage of posive ,negative and neutral tweets in the given dataset. It is done using natural language processing library using scikit learn machine learning libraries such as textblob,etc.

<br>

## NATURAL LANGUAGE PROCESSING<br>

NLP is the method of interaction between humans and computers, so that computers can understand and process what the humans are trying to convey by their actions,thoughts,movements,expressions,etc. 
<br>
## SENTIMENT ANALYSIS<br>
sentiment analysis refers to a process which is used for determining if the given information is positive , negative or neutral using computational methods .
<br>
## STEPS TO BE FOLLOWED IN NLP<br>

 1: Segmentation of the Sentence <br>
The first step in the given text is to break the text apart into separate sentences.
We can assume that each sentence in English is a separate thought or idea. It will be a lot easier to write a program to understand a single sentence than to understand a whole paragraph.
Coding a Sentence Segmentation model can be as simple as splitting apart sentences whenever you see a punctuation mark. But modern NLP pipelines often use more complex techniques that work even when a document isn’t formatted cleanly.
<br>
Step 2: Tokenizing the words in the text
Now that we’ve split our document into sentences, we can process them one at a time. 
The next step in our pipeline is to break this sentence into separate words or tokens. This is called tokenization. 
Tokenization is easy to do in English. We’ll just split apart words whenever there’s a space between them. And we’ll also treat punctuation marks as separate tokens since punctuation also has meaning.
<br>
Step 3: Predicting Parts of Speech for Each Token
Here we check if the given token whether it is a noun, a verb, an adjective and so on. Knowing the role of each word in the sentence will help us start to figure out what the sentence is talking about.
<br>

<br>

 ## LEXICON BASED APPROACH
<br>
In this project we have used the lexicon based approach for analysing the given tweets.
The lexicon based approach uses sentiment dictionary with opinion words and match them with the data for determining polarity. There are three techniques to construct a sentiment
lexicon: manual construction, corpus-based methods and dictionary-based methods. The manual construction is a difficult and time-consuming task. Corpus-based methods can
produce opinion words with relatively high accuracy. Finally, in the dictionary based techniques, the idea is to first collect a small set of opinion words manually with known orientations, and then to grow this set by searching in the WordNet dictionary for their synonyms and antonyms. 
<br>
