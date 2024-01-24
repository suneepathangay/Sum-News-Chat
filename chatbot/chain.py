from langchain_openai import ChatOpenAI
from dotenv import load_dotenv,find_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer,util
from pinecone import Pinecone
import os
import numpy as np


text="On the morning of February 24th, 2022, Russian forces launched a multi-pronged invasion by land, air, and sea on Ukraine. The deadly conflict continues unabated. Even as Ukrainian forces made significant ground gains, strikes by Russia against Ukraine on civilian targets exacerbated concern for humanitarian needs in winter.One year later, 17.7 million people need humanitarian assistance and nearly 8 million refugees from Ukraine have been recorded across Europe. In Ukraine, 6.3 million people are internally displaced, and 6.9 million people are sheltering in place. The UN Human Rights Monitoring Mission in Ukraine reports that from February 24 to December 26, 2022, 6,884 civilians in Ukraine had been killed and 10,974 injured. The real numbers are likely much higher.A year of war has caused widespread destruction, reducing some cities to rubble, damaging or destroying hundreds of thousands of homes along with critical infrastructure and leaving millions of people with limited or no access to electricity, water or heat. Many people are living either in collective centers or damaged buildings, without basic needs for daily life and vulnerable to a range of health threats. Internally displaced persons living in collective centers are most at risk with the majority being women, children, the elderly, and people with disabilities. Overall, an estimated 14.5 million people in Ukraine need health assistance."

text_split=RecursiveCharacterTextSplitter(
    chunk_size=700,chunk_overlap=0,length_function=len
)

chunks=text_split.split_text(text)
##we need to chunk this text more im gonna split it by periods also depending on a threshold

##algorithm to chunk the text even more

for c in chunks:
    c=c.strip()
    copy=c.replace(" ","")
    if len(copy)>500:
        c=c.split(".")




