# Romanian License Plate Availability Checker

A Python tool to automatically check the availability of custom Romanian license plate numbers using the official DGPCI (formerly DRPCIV) online form. The script handles Cloudflare protection and solves reCAPTCHA v2 challenges automatically via Anti-Captcha.

---

## Features

- **Batch Processing:** Reads multiple plate numbers from a text file (`numere.txt`).
- **Cloudflare Bypass:** Uses `cloudscraper` to bypass basic bot-detection systems.
- **Automated CAPTCHA Solving:** Integrated with the Anti-Captcha API (`anticaptchaofficial`) to solve reCAPTCHA v2 automatically.
- **Visual Output:** Displays results in colored terminal output using `colorama`:
  - **Green:** Plate is available.
  - **Red:** Plate is taken / unavailable.
  - **Yellow / Retry:** CAPTCHA or request error (automatically retries the plate).

---

## Prerequisites

- Python 3.7+
- An active [Anti-Captcha](https://anti-captcha.com/) account with available funds and an API key.

---

## Installation

1. **Clone or download this repository** to your local machine.

2. **Install required dependencies:**

```bash
pip install cloudscraper requests colorama anticaptchaofficial
```

---

## Configuration

1. **Input File:** Create a file named `numere.txt` in the same directory as the script. Add the license plates you want to check, one per line:

   ```text
   B123ABC
   CJ99XYZ
   TM01ONE
   ```

2. **API Key Setup:**
   Open `plate.py` and replace the placeholder Anti-Captcha API key with your own key:

   ```python
   solver.set_key("YOUR_ANTICAPTCHA_API_KEY")
   ```

---

## Usage

Run the script using Python:

```bash
python plate.py
```

### Output Example

- **Green text:** The license plate is available for registration.
- **Red text:** The license plate is already assigned or unavailable.
- **Yellow text / Warning:** CAPTCHA verification failed or request timed out; the script will re-queue the current plate and try again.

---

## Disclaimer

This script is intended strictly for personal utility and educational purposes. Ensure your usage adheres to the terms of service of the target website and respect rate limits to avoid unnecessary server load.
