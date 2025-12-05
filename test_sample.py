from playwright.sync_api import GooglePage


def test_google_title(page, base_url):
    google = GooglePage(page)

    # Navigate to Google
    google.navigate(base_url)

    # Handle cookie consent popup (if present)
    google.handle_consent()

    # Validate the title
    title = google.get_title()
    assert "Google" in title

    