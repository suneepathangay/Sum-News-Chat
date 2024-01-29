from sentence_transformers import SentenceTransformer,util
from collections import defaultdict
import numpy as np
from heapq import heapify,heappop
import networkx as nx
from stopwords import get_stopwords
import re


##work on algorithm incorporating the LLM



def return_summary(text):

    #text="On the morning of February 24th, 2022, Russian forces launched a multi-pronged invasion by land, air, and sea on Ukraine. The deadly conflict continues unabated. Even as Ukrainian forces made significant ground gains, strikes by Russia against Ukraine on civilian targets exacerbated concern for humanitarian needs in winter.One year later, 17.7 million people need humanitarian assistance and nearly 8 million refugees from Ukraine have been recorded across Europe. In Ukraine, 6.3 million people are internally displaced, and 6.9 million people are sheltering in place. The UN Human Rights Monitoring Mission in Ukraine reports that from February 24 to December 26, 2022, 6,884 civilians in Ukraine had been killed and 10,974 injured. The real numbers are likely much higher.A year of war has caused widespread destruction, reducing some cities to rubble, damaging or destroying hundreds of thousands of homes along with critical infrastructure and leaving millions of people with limited or no access to electricity, water or heat. Many people are living either in collective centers or damaged buildings, without basic needs for daily life and vulnerable to a range of health threats. Internally displaced persons living in collective centers are most at risk with the majority being women, children, the elderly, and people with disabilities. Overall, an estimated 14.5 million people in Ukraine need health assistance."

    ##defining our model
    

    model = SentenceTransformer('sentence-transformers/sentence-t5-base')
    
        
    #removing stop words from text and splitting them up.


    ##This package stopwords stopped working weirdly enough
    list_stopwords=get_stopwords()

    sentence_list=re.split('(?<=[^A-Z].[.?]) +(?=[A-Z])',text)
    #sentence_list=sent_tokenize(text)
    

    nostop_senteces=[]

    for sentence in sentence_list:
        formatted_sent=""
        for words in sentence.lower().split(' '):
            if words not in list_stopwords:
                formatted_sent=formatted_sent+' '+words
        nostop_senteces.append(formatted_sent)
    
    
    
    sentence_embeddings=model.encode(nostop_senteces,convert_to_tensor=True)
    
    
    
    def cosine_simialrit(vector1,vector2):
        cosine_score=util.cos_sim(vector1,vector2)
        return cosine_score
    
    

    sim_matrix=np.zeros([len(sentence_embeddings),len(sentence_embeddings)])
    
    for i in range(len(sentence_embeddings)):
        for j in range(len(sentence_embeddings)):
            if i!=j:
                vec1=sentence_embeddings[i]
                vec2=sentence_embeddings[j]
                similairty=cosine_simialrit(vec1,vec2)
    #           
                sim_matrix[i][j]=similairty
    
    nx_graph = nx.from_numpy_array(sim_matrix)
    
    scores = nx.pagerank(nx_graph)
    
    list_scores=[]
    
    for score in scores:
        list_scores.append((-scores[score],score))
    
    heapify(list_scores)
    
    summary=""
    
    #print(list_scores) 
    
    for i in range(4):
        print(i)
        if list_scores:
            index=heappop(list_scores)
            index=index[1]
            summary=summary+sentence_list[index]
        else:
            return summary
    
    
    return summary
    
    