#  Mini Project: Customer Feedback NLP Pipeline

class CleanerMixin:
    def clean(self,text):
        text=text.lower()
        text=text.replace(".","").replace(",","").replace("!","").replace("?","")
        return text
    
class TokenizerMixin:
    def tokenize(self,text):
        return text.split()

class StopwordMixin:
    stop_words=["the", "is", "a", "an", "and", "was", "this"]

    def remove_stopwords(self,tokens):
        clean_words=[]

        for token in tokens:
            if token not in self.stop_words:
                clean_words.append(token)

        return clean_words

class FrequencyMixin:
    def frequency(self,tokens):
        freq={}

        for token in tokens:
            freq[token]=freq.get(token,0)+1

        return freq
    
class SentimentMixin:
    positive_words=["love", "great", "fast", "quality", "excellent"]
    negative_words=["bad", "slow", "poor", "hate", "terrible"]

    def predict(self,tokens):
        
        for token in tokens:
            if token in self.positive_words:
                return "Positive"
            
        for token in tokens:
            if token in self.negative_words:
                return "Negative"
            
        return "Neutral"
            
class FeedbackPipeline(
    CleanerMixin,
    TokenizerMixin,
    StopwordMixin,
    FrequencyMixin,
    SentimentMixin
):
    def process(self,text):
        cleaned=self.clean(text)
        tokens=self.tokenize(cleaned)
        tokens=self.remove_stopwords(tokens)
        freq=self.frequency(tokens)
        prediction=self.predict(tokens)

        return{
            "tokens": tokens,
            "frequency": freq,
            "prediction": prediction
        }
    
pipeline=FeedbackPipeline()
result=pipeline.process("I love this product! The delivery was fast, and the quality is great.")

print(result)