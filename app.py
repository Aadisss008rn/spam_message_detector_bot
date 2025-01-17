# import streamlit as st
# from models.spam_detector import SMSSpamDetector

# def load_model():
#     detector = SMSSpamDetector()
#     detector.train_model()
#     return detector

# def main():
#     st.title("SMS Spam Detection System")
    
#     # Initialize model
#     if 'detector' not in st.session_state:
#         st.session_state.detector = load_model()
    
#     # Create input area
#     message = st.text_area("Enter your message:", height=100)
    
#     if st.button("Analyze Message"):
#         if message:
#             # Get prediction and analysis
#             result = st.session_state.detector.predict_message(message)
            
#             # Display result
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 if result['is_spam']:
#                     st.error("📧 This message appears to be SPAM!")
#                 else:
#                     st.success("✉️ This message appears to be legitimate (HAM)")
                
#                 st.info(f"Confidence: {result['confidence']:.2%}")
            
#             # Show keyword analysis
#             st.subheader("Keyword Analysis")
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.write("🚨 Spam Keywords Found:")
#                 if result['spam_keywords']:
#                     for word, count in result['spam_keywords'].items():
#                         st.write(f"- '{word}' (appears {count} times in spam training data)")
#                 else:
#                     st.write("No spam keywords found")
            
#             with col2:
#                 st.write("✅ Legitimate Keywords Found:")
#                 if result['ham_keywords']:
#                     for word, count in result['ham_keywords'].items():
#                         st.write(f"- '{word}' (appears {count} times in ham training data)")
#                 else:
#                     st.write("No ham keywords found")
            
#             # Show all extracted keywords
#             with st.expander("See all extracted keywords"):
#                 st.write(", ".join(result['all_keywords']))
        
#         else:
#             st.warning("Please enter a message to analyze")

# if __name__ == "__main__":
#     main()






import streamlit as st
from models.spam_detector import SMSSpamDetector

def load_model():
    detector = SMSSpamDetector()
    detector.train_model()
    return detector

def main():
    st.title("SMS Spam Detection System")
    
    # Initialize model
    if 'detector' not in st.session_state:
        st.session_state.detector = load_model()
    
    # Create input area
    message = st.text_area("Enter your message:", height=100)
    
    if st.button("Check for Spam"):
        if message:
            # Get prediction
            result = st.session_state.detector.predict_message(message)
            
            # Display result
            if result['is_spam']:
                st.error("🚨 This message appears to be SPAM!")
            else:
                st.success("✉️ This message appears to be legitimate")
            
            st.info(f"Confidence: {result['confidence']:.2%}")
        else:
            st.warning("Please enter a message to analyze")

if __name__ == "__main__":
    main()