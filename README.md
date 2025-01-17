# SMS Spam Detection Chatbot

A machine learning-powered chatbot built with Streamlit that detects whether SMS messages are spam or legitimate (ham). The system uses TF-IDF vectorization and Naive Bayes classification to provide real-time spam detection with confidence scores.

## 🌟 Features

- Real-time SMS spam detection
- User-friendly web interface built with Streamlit
- High accuracy using TF-IDF and Naive Bayes algorithms
- Confidence score for each prediction
- Pre-trained on a diverse dataset of spam and legitimate messages

## 🛠️ Installation

1. Clone the repository
2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and go to localhost

3. Enter any SMS message in the text area

4. Click "Check for Spam" to analyze the message

5. View the results showing whether the message is spam or legitimate, along with the confidence score

## 📁 Project Structure

```
sms-spam-detection/
├── app.py                 # Main Streamlit application
├── models/
│   └── spam_detector.py   # Spam detection model implementation
├── requirements.txt       # Project dependencies
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
```

## 📚 Dependencies

- pandas==1.5.3
- numpy==1.24.2
- scikit-learn==1.2.2
- nltk==3.8.1
- streamlit==1.22.0

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Mail id - aadirajput6951@gmail.com

## 🙏 Acknowledgments

- Dataset inspired by the SMS Spam Collection Dataset
- Built with Streamlit and scikit-learn
- Special thanks to all contributors
