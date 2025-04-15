import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "x7MXxiQNmFLuCSK8iWa1wjHWUGm6hNu5"

def fetch_iqscore_data(url, api_key):
    api_url = "https://www.ipqualityscore.com/api/json/url"
    params = {"key": api_key, "url": url}
    try:
        response = requests.get(api_url, params=params)
        if response.status_code != 200:
            return {"error": f"API Error: {response.status_code}"}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def check_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    if not url.startswith("http"):
        url = "http://" + url

    result = fetch_iqscore_data(url, API_KEY)
    if "error" in result:
        messagebox.showerror("Error", result["error"])
        return

    risk_score = result.get("risk_score", "N/A")
    domain = result.get("domain", "N/A")
    final_url = result.get("final_url", url)

    indicators = {
        "Spamming": result.get("spamming", False),
        "Malware": result.get("malware", False),
        "Phishing": result.get("phishing", False),
        "Suspicious": result.get("suspicious", False),
        "Risky TLD": result.get("risky_tld", False),
        "Adult": result.get("adult", False),
        "Short Link Redirect": result.get("short_url", False),
        "Hosted Content": result.get("hosted_content", False),
        "Parked Domain": result.get("parking", False),
        "Redirected": result.get("redirected", False),
        "IP Address": result.get("ip_address", "N/A"),
        "SPF Enabled": result.get("spf", False),
        "DMARC Enabled": result.get("dmarc", False),
        "DNS Valid": result.get("dns_valid", False),
        "Domain Age": result.get("domain_age", "N/A"),
        "Category": result.get("category", "N/A")
    }

    info_label.config(text=f"{domain} - Risk Score: {risk_score}", fg="red" if risk_score > 50 else "lightgreen")
    for idx, (key, val) in enumerate(indicators.items()):
        label = indicators_labels[idx]
        label.config(text=f"{key}: {val}", fg="red" if val is True or (isinstance(val, str) and "True" in val) else "lightgreen")

# GUI SETUP
root = tk.Tk()
root.title("IQTotal Threat Check")
root.geometry("800x600")
root.configure(bg="white")  # Set background to white

# FONT STYLE
font_title = ("Poppins", 14, "bold")
font_normal = ("Poppins", 11)

# INPUT
tk.Label(root, text="Enter a URL to check:", font=font_title, bg="grey", fg="pink").pack(pady=10)
url_entry = tk.Entry(root, font=font_normal, width=50, bg="pink", fg="white")
url_entry.pack(pady=5)

check_btn = tk.Button(root, text="Lookup", font=font_title, bg="grey", fg="pink", command=check_url)
check_btn.pack(pady=10)

# RESULT SECTION
info_label = tk.Label(root, text="", font=("Poppins", 13, "bold"), bg="white", fg="pink")
info_label.pack(pady=10)

frame = tk.Frame(root, bg="grey")  # Create a frame with white background
frame.pack(padx=20, pady=20, fill="both", expand=True)

indicators_labels = []
for _ in range(16):  # total 16 indicators
    label = tk.Label(frame, text="", font=font_normal, bg="grey", fg="pink", anchor="w")
    label.pack(anchor="w", pady=2)
    indicators_labels.append(label)

root.mainloop()