import time
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

def fetch_page(url):
    start_time = time.time()
    response = requests.get(
        url,
        timeout=10,
        headers=HEADERS
    )
    response_time = round((time.time() - start_time) * 1000)

    # Check HTTP status
    if response.status_code != 200:
        return None, None, response_time, {
            "error": f"Website returned HTTP {response.status_code}."
        }

    # Check HTML content
    content_type = response.headers.get("Content-Type", "").lower()
    if "text/html" not in content_type:
        return None, None, response_time, {
            "error": "The URL does not point to an HTML page."
        }
    soup = BeautifulSoup(response.text, "html.parser")
    return response, soup, response_time, None

def extract_title(soup):
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "Not Found"

def extract_meta_description(soup):
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        return meta["content"].strip()
    return "Not Found"

def count_h1(soup):
    return len(soup.find_all("h1"))

def count_missing_alt_images(soup):
    images = soup.find_all("img")
    return sum(1 for img in images if not img.get("alt"))

def count_words(soup):
    text = soup.get_text(separator=" ", strip=True)
    words = text.split()
    return len(words)

def analyze_website(url):
    try:
        response, soup, response_time, error = fetch_page(url)
        if error:
            return error
        return {
            "http_status": response.status_code,
            "response_time": f"{response_time} ms",
            "title": extract_title(soup),
            "meta_description": extract_meta_description(soup),
            "h1_count": count_h1(soup),
            "missing_alt_images": count_missing_alt_images(soup),
            "word_count": count_words(soup)
        }

    except requests.exceptions.MissingSchema:
        return {
            "error": "Please include http:// or https:// in the URL."
        }

    except requests.exceptions.InvalidURL:
        return {
            "error": "Invalid URL."
        }

    except requests.exceptions.Timeout:
        return {
            "error": "The website took too long to respond."
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Unable to connect to the website."
        }

    except Exception:
        return {
            "error": "Unexpected error while analyzing the website."
        }
