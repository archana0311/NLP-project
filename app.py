import streamlit as st 
from time import sleep
from stqdm import stqdm
import pandas as pd
from transformers import pipeline
import json
import spacy
import spacy_streamlit


def draw_all(
    key,
    plot=False,
):
    st.write(
        """
        # NLP App
        
        This app empower you to explore the endless possibilities hidden within the world of text
        
        This App is built using pretrained transformers.
        
        ```python
        # Key Features of this App.
        1. Text Summarizer    
        2. Sentiment Analysis
        3. Question Answering
        4. Text Completion
       
        ```
        """
    )

    

with st.sidebar:
    draw_all("sidebar")



def main():
    st.title("NLP App")
    menu = ["--Select--","Summarizer","Sentiment Analysis","Question Answering","Text Completion"]
    choice = st.sidebar.selectbox("SELECT", menu)
    
    if choice=="--Select--":
        
        st.write("""
                 
                 This is a Natural Language Processing Based Web App that can do anything u can imagine with the Text.
        """)
        
        st.write("""
                 
                 Natural Language Processing (NLP) is a computational technique to understand the human language in the way they spoke and write.
        """)
        
        st.write("""
                 
                 NLP is a sub field of Artificial Intelligence (AI) to understand the context of text just like humans.
        """)
        
        
        st.image('dhanvi.jpeg')
    
    
    
    elif choice=="Summarizer":
        st.subheader("Text Summarization")
        st.write(" Enter the Text you want to summarize !")
        raw_text = st.text_area("Your Text","Enter Your Text Here")
        num_words = st.number_input("Enter Number of Words in Summary")
        
        if raw_text!="" and num_words is not None:
            num_words = int(num_words)
            summarizer = pipeline('summarization')
            summary = summarizer(raw_text, min_length=num_words,max_length=50)
            s1 = json.dumps(summary[0])
            d2 = json.loads(s1)
            result_summary = d2['summary_text']
            result_summary = '. '.join(list(map(lambda x: x.strip().capitalize(), result_summary.split('.'))))
            st.write(f"Here's your Summary : {result_summary}")
        
        
      
    elif choice=="Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        sentiment_analysis = pipeline("sentiment-analysis")
        st.write(" Enter the Text below To find out its Sentiment !")

        raw_text = st.text_area("Your Text","Enter Text Here")
        if raw_text !="Enter Text Here":
            result = sentiment_analysis(raw_text)[0]
            sentiment = result['label']
            for _ in stqdm(range(50), desc="Please wait a bit. The model is fetching the results !!"):
                sleep(0.1)
            if sentiment =="POSITIVE":
                st.write("""# This text has a Positive Sentiment.  🤗""")
            elif sentiment =="NEGATIVE":
                st.write("""# This text has a Negative Sentiment. 😤""")
            elif sentiment =="NEUTRAL":
                st.write("""# This text seems Neutral ... 😐""")
    
    elif choice=="Question Answering":
        st.subheader("Question Answering")
        st.write(" Enter the Context and ask the Question to find out the Answer !")
        question_answering = pipeline("question-answering")
        

        context = st.text_area("Context","Enter the Context Here")
        
        question = st.text_area("Your Question","Enter your Question Here")
        
        if context !="Enter Text Here" and question!="Enter your Question Here":
            result = question_answering(question=question, context=context)
            s1 = json.dumps(result)
            d2 = json.loads(s1)
            generated_text = d2['answer']
            generated_text = '. '.join(list(map(lambda x: x.strip().capitalize(), generated_text.split('.'))))
            st.write(f" Here's your Answer :\n {generated_text}")
    
    elif choice=="Text Completion":
        st.subheader("Text Completion")
        st.write(" Enter the uncomplete Text to complete it automatically using AI !")
        text_generation = pipeline("text-generation")
        message = st.text_area("Your Text","Enter the Text to complete")
        
        
        if message !="Enter the Text to complete":
            generator = text_generation(message)
            s1 = json.dumps(generator[0])
            d2 = json.loads(s1)
            generated_text = d2['generated_text']
            generated_text = '. '.join(list(map(lambda x: x.strip().capitalize(), generated_text.split('.'))))
            st.write(f" Here's your Generate Text :\n   {generated_text}")
            
  

if __name__ == '__main__':
	main()