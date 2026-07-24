import sys
import os

# Add the project root directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import analyze_website


def test_valid_url():
    result = analyze_website("https://example.com")

    assert "http_status" in result
    assert result["http_status"] == 200


def test_invalid_url():
    result = analyze_website("abc")

    assert "error" in result


def test_http_404():
    result = analyze_website("https://example.com/thispagedoesnotexist")

    assert "error" in result


def test_connection_error():
    result = analyze_website(
        "https://this-domain-should-not-exist-123456789.com"
    )

    assert "error" in result