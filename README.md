# Page Pulse

Page Pulse is a simple web application built with Flask that analyzes a website URL and provides useful page and SEO information, including HTTP status, response time, page title, meta description, H1 count, images missing ALT text, and approximate word count.

Developed as part of the **Digital Heroes Software Development (SDE) Internship Qualification Task**.

---

## Tech Stack

- Python
- Flask
- Requests
- BeautifulSoup4
- HTML
- CSS
- JavaScript
- Pytest

---

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd page-pulse
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

Run the tests:

```bash
pytest -v
```

---

## API Contract

### Endpoint

```
POST /analyze
```

### Request

```json
{
  "url": "https://example.com"
}
```

### Success Response

```json
{
  "http_status": 200,
  "response_time": "120 ms",
  "title": "Example Domain",
  "meta_description": "...",
  "h1_count": 1,
  "missing_alt_images": 0,
  "word_count": 250
}
```

### Error Response

```json
{
  "error": "Please include http:// or https:// in the URL."
}
```

---

## Design Decisions

### 1. Modular Architecture
The website analysis logic is separated into `parser.py`, while `app.py` handles routing. This improves readability and maintainability.

### 2. Robust Error Handling
The application handles invalid URLs, connection failures, timeouts, HTTP errors, and non-HTML responses to provide clear feedback instead of crashing.

### 3. JSON-Based API
The backend returns structured JSON responses, making the application easier to integrate with different frontends or future services.

---

## Repository

**GitHub Repository:**  

https://github.com/Nithin3117/page-pulse

**Live Demo:**  

https://page-pulse-k8ja.onrender.com/

---

## Author

**Nithin Bollineni**  
B.Tech (3rd Year)  

---

Built for the **Digital Heroes Training Task**.
