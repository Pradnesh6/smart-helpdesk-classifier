# Smart Helpdesk Ticket Classifier

An intelligent machine learning-based system for automatically classifying IT helpdesk support tickets into predefined categories using Natural Language Processing (NLP).

## 🎯 Overview

The Smart Helpdesk Ticket Classifier uses machine learning to automatically categorize incoming IT support tickets, helping streamline ticket routing and improve response times. It leverages TF-IDF vectorization and Naive Bayes classification to intelligently analyze ticket descriptions and assign them to appropriate categories.

## ✨ Features

- **Automatic Classification**: Intelligently classifies helpdesk tickets into predefined categories
- **Interactive Web Interface**: User-friendly Streamlit-based web application for real-time predictions
- **Machine Learning Pipeline**: Pre-trained model ready for immediate use
- **Easy to Train**: Simple training script to retrain the model with new data
- **Fast Predictions**: Efficient classification with minimal latency

## 📋 Requirements

- Python 3.7 or higher
- pandas
- scikit-learn
- streamlit
- joblib

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Pradnesh6/smart-helpdesk-classifier.git
cd smart-helpdesk-classifier
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pandas scikit-learn streamlit joblib
```

## 💻 Usage

### Running the Web Application

Start the Streamlit app to classify tickets interactively:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

**To use:**
1. Enter your IT support ticket description in the text area
2. Click the "Classify Ticket" button
3. View the predicted category

### Training the Model

To retrain the model with new ticket data:

```bash
python train.py
```

**Prerequisites:**
- Ensure `tickets.csv` exists in the project directory with columns: `text` (ticket description) and `category` (ticket category)
- CSV format example:

```
text,category
"Network is down in building A","Network"
"Cannot access email account","Account"
"Printer not working","Hardware"
```

## 📁 Project Structure

```
smart-helpdesk-classifier/
├── app.py              # Streamlit web application
├── train.py            # Model training script
├── model.pkl           # Pre-trained machine learning model
├── tickets.csv         # Training dataset (sample tickets with categories)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 How It Works

### Model Architecture

The classifier uses a scikit-learn pipeline with two main components:

1. **TF-IDF Vectorizer**: Converts text descriptions into numerical features
   - Extracts important keywords and phrases
   - Weights words by their importance

2. **Multinomial Naive Bayes**: Classification algorithm
   - Fast and efficient for text classification
   - Works well with sparse data from TF-IDF

### Workflow

```
Raw Ticket Text
    ↓
TF-IDF Vectorization
    ↓
Naive Bayes Classifier
    ↓
Predicted Category
```

## 📊 Dataset Format

The `tickets.csv` file should contain:

| Column | Description |
|--------|-------------|
| text | The ticket description/message |
| category | The category label (e.g., "Network", "Hardware", "Account") |

Example:

```csv
text,category
"My computer won't turn on",Hardware
"I need to reset my password",Account
"Internet is very slow",Network
```

## 🔄 Model Retraining

To improve classification accuracy:

1. Update `tickets.csv` with more examples
2. Run `python train.py`
3. The new model will be saved to `model.pkl`
4. Restart the app to use the updated model

## 📝 Example

```python
# Using the model programmatically
import joblib

model = joblib.load("model.pkl")
prediction = model.predict(["My email is not working"])[0]
print(f"Category: {prediction}")
```

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and CSV handling
- **Scikit-learn**: Machine learning library
- **Streamlit**: Web application framework
- **Joblib**: Model serialization

## 📈 Performance Tips

- Provide diverse training examples for better accuracy
- Include 50+ examples per category for optimal performance
- Update the model regularly with new ticket data
- Monitor prediction accuracy and retrain as needed

## 🤝 Contributing

Contributions are welcome! To improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m "Add improvement"`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Pradnesh**

- GitHub: [@Pradnesh6](https://github.com/Pradnesh6)
- Repository: [smart-helpdesk-classifier](https://github.com/Pradnesh6/smart-helpdesk-classifier)

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Run `train.py` to create the model |
| Streamlit not installed | Run `pip install streamlit` |
| CSV not found | Ensure `tickets.csv` exists in the project directory |
| Poor predictions | Add more training examples and retrain the model |

## 📚 Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TF-IDF Explanation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Naive Bayes Classification](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

---

**Happy Classifying! 🎉**
