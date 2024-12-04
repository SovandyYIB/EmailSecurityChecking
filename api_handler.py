
import requests

IPQS_API_KEY = "o7Zvhw6NMtRlLZvYcdIqAKe8CZgoIVbl"  # Replace with your IPQS API key


def check_ipqs(query):
    """
    Queries the IPQS API with the given input.
    This can be a URL or an email.
    """
    response = requests.get(f"https://ipqualityscore.com/api/json/url/{IPQS_API_KEY}/{query}")

    # Check for a successful response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"IPQualityScore API error: {response.status_code}, {response.text}"}
