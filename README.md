# 📱 Phone Number Region & Carrier Lookup

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📖 Overview

**Phone Number Region & Carrier Lookup** is a lightweight Python application that retrieves the **general geographic region** and **original network carrier** associated with a phone number based on publicly available numbering information.

The project also supports generating an interactive map of the number's approximate region using the **OpenCage Geocoding API** and **Folium**.

> **Note:** This application is intended for educational purposes and demonstrates the use of third-party Python libraries, API integration, geocoding, and data visualization.

---

## ✨ Features

- 📱 Phone number validation
- 🌍 Region and country lookup
- 📡 Original carrier detection
- 🗺️ Interactive map generation
- 🔑 OpenCage API integration
- 📄 HTML map export
- ⚡ Simple command-line interface
- 🐍 Built entirely with Python

---

## 🛠️ Technologies Used

- Python 3
- phonenumbers
- Folium
- OpenCage Geocoding API

---

## 📂 Project Structure

```
Tracking-phone-Numbers/
│── phone_lookup.py
│── requirements.txt
│── Location.html
│── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- OpenCage API Key (only required for map generation)

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Reigns-B/Tracking-phone-Numbers.git
```

### Navigate into the project

```bash
cd Tracking-phone-Numbers
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

```text
phonenumbers
folium
opencage
```

Or install them manually:

```bash
pip install phonenumbers folium opencage
```

---

## 🔑 API Configuration

Create a free OpenCage account and obtain an API key.

Set the API key as an environment variable.

### Windows

```powershell
setx OPENCAGE_API_KEY "YOUR_API_KEY"
```

### macOS/Linux

```bash
export OPENCAGE_API_KEY="YOUR_API_KEY"
```

---

## ▶️ Usage

Run the application:

```bash
python phone_lookup.py
```

Example input:

```text
Enter the phone number with country code:
+254712345678
```

Example output:

```text
Country: Kenya

Region:
Nairobi

Carrier:
Safaricom

Map saved as:
Location.html
```

Open **Location.html** in your browser to view the generated interactive map.

---

## 📚 What You'll Learn

This project demonstrates:

- Phone number parsing
- Number validation
- Carrier lookup
- Geocoding
- API integration
- Interactive map generation
- Environment variables
- Python package management
- File generation

---

## 🛣️ Roadmap

Future improvements include:

- ✅ Batch phone lookup
- ✅ CSV import/export
- ✅ JSON output
- ✅ Command-line arguments (argparse)
- ✅ Flask web interface
- ✅ FastAPI REST API
- ✅ Database integration
- ✅ Result caching
- ✅ Unit testing
- ✅ Alternative geocoding providers

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

---

## ⚠️ Important Disclaimer

This tool **does not**:

- ❌ Track phones in real time
- ❌ Access GPS locations
- ❌ Reveal a user's live location
- ❌ Hack or monitor mobile devices

It only displays publicly inferable metadata such as the country, region, and the original carrier assigned to a phone number.

Phone numbers may be **ported** between carriers, meaning the reported carrier may not always represent the user's current mobile operator.

Please use this project responsibly and respect local privacy laws and regulations.

---

## 👨‍💻 Author

**Bradley Ochieng**

Digital Transformation Enthusiast • Software Engineer •   Digital Marketing Expert

---

## 🌐 Connect

- Website: https://bradleydigitals.com
- Instagram:https://www.instagram.com/mrbradley__/
- Bradley Digitals: https://instagram.com/bradleydigitals

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Report issues
- 💡 Suggest improvements

---

## 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it while retaining the original license notice.

---
