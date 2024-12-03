---

# **Fake News Detection Application**

This is a web-based application for detecting fake news using **Natural Language Processing (NLP)** and **web scraping**. Users can input news text, and the app fetches related articles from trusted websites, analyzes their similarity, and classifies the input as either "Real" or "Fake."

---

## **Features**
- **User Input**: Accepts news text input from users through a web interface.
- **Web Scraping**: Scrapes related articles from trusted websites (e.g., Reuters, BBC, etc.).
- **NLP Analysis**: Uses **Sentence Transformers** to compute similarity scores between user input and scraped articles.
- **Fake News Detection**: Classifies the news as **Real** or **Fake** based on similarity thresholds.
- **Local Storage**: Saves the results locally for reference.

---

## **Technologies Used**
### **Backend:**
- **Python**
- **Flask** for web application
- **BeautifulSoup4** for web scraping
- **Requests** for HTTP requests
- **Sentence Transformers** for NLP embeddings and similarity analysis
- **Torch** for deep learning computations

### **Frontend:**
- HTML and CSS (basic styling included)

---

## **Project Structure**
```
project/
├── app.py                  # Main Flask application
├── scrapper.py             # Web scraping logic
├── nlp_analysis.py         # NLP similarity and classification logic
├── storage.py              # Handles local storage of results
├── templates/
│   └── index.html          # Frontend HTML template
└── README.md               # Project documentation
```

---

## **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/Anmolkundap2004/Fake-News-Detection-NLP-and-Web-Scrapping.git
   cd fake-news-detection
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open the browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Usage**
1. Enter the news text in the input box on the webpage.
2. Click the "Check" button.
3. View the result (Real/Fake) along with links to scraped articles for reference.

---

## **Example**
- **Input**:  
  "COVID-19 vaccines are harmful and unsafe."
  
- **Output**:  
  - **Result**: Fake  
  - **Scraped Articles**:
    - [https://www.reuters.com/...](https://www.reuters.com/)
    - [https://www.bbc.com/...](https://www.bbc.com/)

---

## **Libraries Used**
1. Flask  
2. Requests  
3. BeautifulSoup4  
4. Sentence Transformers  
5. Torch  
6. os  
7. json  
8. math  

---

## **License**
This project is open-source and available under the [MIT License](LICENSE).

--- 
