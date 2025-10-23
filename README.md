
# 🩺 Doc Q — Doctor Appointment Booking System

**Doc Q** is a web-based platform designed to simplify doctor appointment scheduling.  
Built using **Flask**, it allows patients to book, verify, and cancel appointments securely through **Gmail OTP verification**, while storing data in **Google Sheets** for real-time record management.

---

## 🧾 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Folder Structure](#folder-structure)  
5. [Installation & Setup](#installation--setup)  
6. [Environment Variables](#environment-variables)  
7. [Screenshots](#screenshots)  
8. [Future Enhancements](#future-enhancements)  
9. [Contributing](#contributing)  
10. [License](#license)

---

## 🩹 Overview

Doc Q helps clinics and patients manage appointments seamlessly using secure email verification.  
Its modular design supports easy scaling, enabling future integration of payment gateways, AI-based doctor recommendations, and patient management modules.

---

## 🚀 Features

- 🔐 **Gmail OTP Verification** – Ensures secure user identity confirmation.  
- 📅 **Appointment Booking** – Patients can easily book and view slots.  
- ❌ **Appointment Cancellation** – Remove existing bookings using name/date.  
- 📊 **Google Sheets Integration** – Stores all bookings in real time.  
- 🧩 **Modular Design** – Separate modules for OTP, email, and sheet management.  
- 🖥️ **Responsive UI** – Works smoothly across desktop and mobile browsers.  

---

## 🧰 Tech Stack

### 🧠 **Core Languages & Frameworks**
| Layer | Technology |
|-------|-------------|
| Backend | 🐍 Python 3 |
| Web Framework | 🌐 Flask |
| Frontend | 🧱 HTML5 • 🎨 CSS3 • ⚡ JavaScript (Vanilla JS) |

### ⚙️ **APIs & Integrations**
| Function | Integration |
|-----------|--------------|
| Appointment Storage | 📊 Google Sheets API |
| Email Verification | ✉️ Gmail SMTP |
| Authentication | 🔑 OAuth 2.0 (Service Account) |

### 🧩 **Python Libraries**
`flask`, `gspread`, `oauth2client`, `smtplib`, `email.mime`, `random`, `time`, `datetime`, `os`, `json`

### 🧑‍💻 **Development Tools**
| Tool | Use |
|------|-----|
| **VS Code** | Development & Debugging |
| **venv** | Virtual Environment |
| **Git & GitHub** | Version Control & Hosting |
| **Browser (Chrome/Edge)** | Testing Routes & UI |

---

## 📂 Folder Structure

```
DocQ/
│
├── app.py                   # Main Flask application
├── config.py                # Central configuration
├── requirements.txt         # Project dependencies
│
├── credentials/
│   └── service_account.json # Google API credentials
│
├── templates/               # HTML pages
│   ├── index.html
│   ├── verify.html
│   ├── book.html
│   └── success.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
└── utils/                   # Utility modules
    ├── email_sender.py
    ├── google_sheets.py
    └── otp_handler.py
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<vivekojha02>/DocQ.git
   cd DocQ
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate       # Windows
   # or
   source venv/bin/activate    # macOS / Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables** (see below)

5. **Run the Flask App**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 🔐 Environment Variables

**Remember to change config.py,service_account.json file before use:**

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
SHEET_ID=your_google_sheet_id
```

> ⚠️ Make sure to enable Gmail “App Passwords” and Google Sheets API access for your service account.

---

## 🖼️ Screenshots


- Homepage / Booking Form  
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0b040be2-3816-4b36-baf0-20126a3ded97" />
- OTP Verification Page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/19e8a1c0-5ea3-4110-8189-252be14309b6" />

- Form
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/eb69f4f3-c990-4299-a422-ef5531fed80b" />

- Success / Cancellation Message  
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f55c99c8-985c-4eee-9778-a40236c2a6b1" />

---

## 🧠 Future Enhancements

- 💳 Online Payment Gateway (Razorpay / Stripe)  
- 🤖 Doctor Recommendation  
- 🩹 Prescription Upload & Download  
- 📅 Integration with hospital website 
- 📧 SMS Notification Service  

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, open an issue first to discuss your ideas.  
Make sure to update tests as needed.

---

## 🪪 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

### 💬 Developed By
**Vivek Ojha**  

