# URL Threat Analysis 

A lightweight and intuitive Python GUI tool to analyze and detect potentially harmful URLs using the [IPQualityScore](https://www.ipqualityscore.com/) API. This tool helps identify threats like phishing, malware, spam, short links, and more.

## Features
- Real-time URL threat analysis
- Highlights indicators like:
  - Phishing
  - Malware
  - Suspicious domains
  - Domain age, SPF/DMARC status
- Easy-to-use GUI built with Tkinter
- Color-coded results (green = safe, red = risky)

# Screenshots
> _Add screenshots to `/screenshots` and link them here._

![GUI Screenshot](screenshots/gui.png)

## Getting Started

# Prerequisites
- Python 3.10+
- `requests` module
- IPQualityScore API key

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/URL-Threat-Scanner.git
   cd URL-Threat-Scanner
   ```

2. Install required packages:
   ```bash
   pip install requests
   ```

3. Run the tool:
   ```bash
   python main.py
   ```

# API Key
Sign up at [IPQualityScore](https://www.ipqualityscore.com/) to get a free API key and replace the placeholder in `main.py`:
```python
API_KEY = "your_api_key_here"
```

# Project Structure
├── main.py
├── README.md
├── screenshots/

# Authors
- Ishita Jain 

# Project Info
This mini project was built as part of the B.Tech Cybersecurity curriculum under the guidance of Dr. Harinee S, Jain (Deemed-to-be) University.

# License
This project is for educational use. Attribution appreciated.
