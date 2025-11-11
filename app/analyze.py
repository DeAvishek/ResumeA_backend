from fastapi import HTTPException
def analyzer(Job_desc,resume_text):
    try:
        import re
        import spacy
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        
        '''STEP 1 CLEANING JOB_DESC'''
        # Cleaning the jobdesc
        # cleaning --> to lower case convert regex matching
        Job_desc = Job_desc.lower()
        Job_desc = re.sub('[^a-zA-Z]',' ',Job_desc)
        
        #nlp -->lemmitization and stop word removing
        nlp = spacy.load("en_core_web_sm")
        doc_jobDesc = nlp(Job_desc)
        filtered_token = [token.lemma_ for token in doc_jobDesc if not token.is_stop]
        corpus_jdsc=" ".join(filtered_token)
        
        '''STEP 2 CLEANING RESUME'''
        resume_text = re.sub('[^a-zA-Z]',' ',resume_text)
        resume_text = resume_text.strip()
        resume_text = resume_text.lower()
        resume_text = re.sub(r"[0-9]","",resume_text)
        resume_text = re.sub(r"(linkedin|github)","",resume_text)
        resume_text = re.sub(r"link","",resume_text)
        resume_text = re.sub(r"(:|-)","",resume_text)
        resume_text = re.sub(r"\S+@\S+","",resume_text)
        resume_text = re.sub(r"(email|gmail|mail)","",resume_text)
        resume_text = re.sub(r"(contact|mobile|phone)","",resume_text)
        resume_text = re.sub(r"http?s://\S+","",resume_text)
        resume_text = re.sub(r"www\.\S+","",resume_text)
        resume_text = re.sub(r'[•*\-+]', '', resume_text)
        candidate_email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)
        
        # remove stop words and lemmatized
        doc_resume = nlp(resume_text)
        token_resume = [token.lemma_ for token in doc_resume if not token.is_stop]
        corpus_resume = ' '.join(token_resume)
        corpus_resume = re.sub(' +',' ',corpus_resume)
            
        '''STEP 3 SKILL MATCHING BY SPACY'''
        from spacy.matcher import Matcher
        import pandas as pd
        import numpy as np
        
        #--->loading the Skill_set csv file
        skill_csv = pd.read_csv("skill_list.csv") 
        skill_array = np.array(skill_csv['skill'])
        
        #--->matching skills from skill list and jobdesc
        nlp_match = spacy.load("en_core_web_sm")
        doc1 = nlp_match(corpus_jdsc)

        matcher = Matcher(nlp_match.vocab)

        #--->Add each skill as a separate pattern
        for skill in skill_array:
            skill = skill.lower()
            pattern = [{"LOWER": skill}]
            matcher.add(skill, [pattern])  # skill name as unique matcher ID

        # Run matcher
        matches = matcher(doc1)

        # Extract matched skills
        jobdesc_skill = set()
        for match_id,start, end in matches:
            skill_name = doc1[start:end].text
            jobdesc_skill.add(skill_name)
        
        #--->matching skill in jobedesc_Skill and resume
        doc2 = nlp_match(corpus_resume)
        matcher2 = Matcher(nlp_match.vocab)
        for skill in jobdesc_skill:
            skill = skill.lower()
            pattern = [{"LOWER":skill}]
            matcher2.add(skill,[pattern])
        matches2 = matcher2(doc2)
        # Extract matched skills
        resume_skill = set()
        for match_id,start,end in matches2:
            skill_name = doc2[start:end].text
            resume_skill.add(skill_name)
            
        '''Similarty score TF-IDF and sentimeant analysis'''
        #-->sentiment analysis
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(corpus_resume)
        sentiment_compund = vs['compound']
        
        #-->TF-IDF count
        tf_idf = TfidfVectorizer()
        vectors = tf_idf.fit_transform([corpus_resume,corpus_jdsc])
        similarity_score = cosine_similarity(vectors[0],vectors[1])
        
        totalScore = 0.8*similarity_score+sentiment_compund*.3
        return {"job_skill":jobdesc_skill,"resume_skill":resume_skill,"score":totalScore[0][0],"status":200}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
        
    