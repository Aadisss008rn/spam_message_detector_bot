import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class SMSSpamDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()
    
    def get_sample_data(self):
        """Create an expanded dataset with more examples"""
        data = {
            'message': [
                # Spam Messages (30)
                "WINNER!! Claim your 90,000 prize reward now!",
                "FREE RINGBONE text WIN to 87131 to get your reward",
                "Congratulations! You've won a free iPhone. Click here",
                "URGENT: Your bank account has been suspended",
                "You're a WINNER! Claim your $1000 prize now",
                "FREE entry into our prize draw! Text YES",
                "50% OFF! Limited time offer on all products",
                "Your PayPal account needs verification",
                "Congratulations! You won the lottery",
                "EXCLUSIVE OFFER: Buy one get two free!",
                "Win a dream holiday! Click here to enter",
                "Your credit card has been charged $500",
                "Amazing discount! 70% off designer brands",
                "You're pre-approved for a $10,000 loan!",
                "Free gift card! Complete survey now",
                "URGENT: Your Netflix account is suspended",
                "You have won a $500 Amazon gift card",
                "Double your income working from home!",
                "Hot stock tip! Invest now for huge returns",
                "Your iCloud account has been compromised",
                "Claim your free Caribbean cruise now",
                "URGENT: Invoice paid twice. Click for refund",
                "You've been selected for a special offer",
                "Guaranteed weight loss in 7 days",
                "Make money fast! Work from home",
                "Your attention required: Account suspended",
                "FREE: Latest iPhone model for survey",
                "Unclaimed prize waiting for collection",
                "Important: Your package delivery failed",
                "Win big! Casino bonus offer inside",

                # Ham Messages (30)
                "Hey, can we meet at 3pm for coffee?",
                "Your package will arrive tomorrow between 2-4pm",
                "Meeting rescheduled to 10am tomorrow",
                "Thanks for the birthday wishes!",
                "Don't forget to bring the documents tomorrow",
                "I'm running late. Be there in 15 minutes",
                "Your dentist appointment is confirmed",
                "Great seeing you yesterday at lunch",
                "Can you pick up milk on your way home?",
                "The report is ready for review",
                "Are you free this weekend for dinner?",
                "Your order has been shipped",
                "Please call me when you get a chance",
                "The kids loved the party yesterday",
                "Remember to send the invoice today",
                "What time should we meet for lunch?",
                "Project meeting starts in 10 minutes",
                "Thanks for helping with the move",
                "Your flight is confirmed for tomorrow",
                "Happy birthday! Have a great day",
                "Should we order pizza for dinner?",
                "The car is ready for pickup",
                "See you at the gym at 6pm",
                "How was your vacation?",
                "Did you get the files I sent?",
                "Weather looks good for the picnic",
                "Your reservation is confirmed",
                "Can you send me the presentation?",
                "Don't forget mom's birthday tomorrow",
                "The tickets are in my drawer"
            ],
            'label': ['spam'] * 30 + ['ham'] * 30
        }
        return pd.DataFrame(data)
    
    def train_model(self):
        """Train the spam detection model"""
        df = self.get_sample_data()
        
        # Transform the messages into vectors
        X = self.vectorizer.fit_transform(df['message'])
        y = (df['label'] == 'spam').astype(int)
        
        # Train the model
        self.model.fit(X, y)
        return self
    
    def predict_message(self, message):
        """Predict whether a message is spam or not"""
        # Vectorize the message
        vectorized_message = self.vectorizer.transform([message])
        
        # Make prediction
        prediction = self.model.predict(vectorized_message)[0]
        probability = self.model.predict_proba(vectorized_message)[0]
        
        return {
            'is_spam': bool(prediction),
            'confidence': probability[1] if prediction else probability[0]
        }

if __name__ == "__main__":
    detector = SMSSpamDetector()
    detector.train_model()
    
    test_message = "WINNER!! Claim your prize reward now!"
    result = detector.predict_message(test_message)
    print(f"Message: {test_message}")
    print(f"Is Spam: {result['is_spam']}")
    print(f"Confidence: {result['confidence']:.2f}")