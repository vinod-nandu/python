# WhatsApp Bot – Playwright Automation

## 📌 Overview

A simple **Python-based WhatsApp Web automation bot** built using **Playwright**.

The application reads a contact and message template from an Excel file, opens the contact's WhatsApp chat, personalizes and sends the message, verifies the sent message, captures a screenshot, extracts recent messages, and generates **JSON and Excel reports**.

---

## 🚀 Features

* Read contact details from `contacts.xlsx`
* Search WhatsApp contact using phone number
* Open the matching WhatsApp chat
* Personalize messages using `{name}`
* Type and send messages automatically
* Add a random **2–5 second delay**
* Verify that the message was sent
* Capture a screenshot for verification
* Extract the last 3 incoming messages
* Store execution results
* Generate dated JSON reports
* Generate dated Excel reports
* Maintain WhatsApp login session using a persistent browser profile

---

## 🛠️ Technologies Used

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Main programming language       |
| Playwright | WhatsApp Web browser automation |
| Pandas     | Excel data processing           |
| OpenPyXL   | Excel file handling             |
| JSON       | Report generation               |
| Chromium   | Browser automation              |

---

## 📦 Installation

Install the required Python packages:

```bash
pip install playwright openpyxl pandas
```

Install the Playwright browser:

```bash
playwright install chromium
```

---

## 📁 Project Structure

```text
whatsapp_bot/
│
├── whatsapp_bot.py
├── contacts.xlsx
│
├── whatsapp_profile/
│   └── Browser session data
│
└── reports/
    ├── screenshots/
    │   └── Sent message screenshots
    │
    ├── whatsapp_report_YYYYMMDD_HHMMSS.json
    └── whatsapp_report_YYYYMMDD_HHMMSS.xlsx
```

---

## 📊 Input Excel File

Create a file named:

```text
contacts.xlsx
```

It should contain the following columns:

| name | phone        | message                               |
| ---- | ------------ | ------------------------------------- |
| John | 919876543210 | Hello {name}, this is a test message. |

### Column Description

* **name** – Contact's name
* **phone** – Contact's phone number with country code
* **message** – Message template
* **`{name}`** – Placeholder replaced with the actual contact name

### Example

Input:

```text
Hello {name}, your report is ready.
```

For John, the bot sends:

```text
Hello John, your report is ready.
```

---

## 🔄 Automation Workflow

```text
contacts.xlsx
      │
      ▼
Read Contact Details
      │
      ▼
Open WhatsApp Web
      │
      ▼
Search Contact
      │
      ▼
Open Chat
      │
      ▼
Personalize Message
      │
      ▼
Type Message
      │
      ▼
Random 2–5 Second Delay
      │
      ▼
Send Message
      │
      ▼
Verify Sent Message
      │
      ▼
Take Screenshot
      │
      ▼
Extract Last 3 Messages
      │
      ▼
Store Result
      │
      ▼
Generate JSON + Excel Reports
```

---

## ▶️ Running the Bot

Run:

```bash
python whatsapp_bot.py
```

On the first execution:

1. Chromium opens.
2. WhatsApp Web loads.
3. Scan the WhatsApp QR code.
4. The bot waits until WhatsApp Web is ready.
5. The automation starts.

The browser session is stored in:

```text
whatsapp_profile/
```

Therefore, subsequent executions can reuse the existing session.

---

## ⏱️ Human-Like Delay

Before sending the message, the bot generates a random delay:

```python
delay = random.uniform(2, 5)
```

This produces a delay between:

```text
2 seconds → 5 seconds
```

The delay is applied before pressing **Enter** to send the message.

---

## 📸 Screenshot

After successful message verification, the bot captures a screenshot.

Example:

```text
reports/screenshots/20260827_202530_John.png
```

The screenshot path is also stored in the report.

---

## 💬 Message Extraction

The bot attempts to extract the contact's last **3 incoming messages**.

Each extracted message contains:

```json
{
    "message": "Hello, how are you?",
    "timestamp": "[20:15, 27/08/2026]"
}
```

The results are stored in the JSON and Excel reports.

---

## 📄 JSON Report

Example:

```json
{
    "name": "John",
    "phone": "919876543210",
    "message": "Hello John, this is a test message.",
    "sent": true,
    "screenshot": "reports/screenshots/20260827_202530_John.png",
    "messages": [
        {
            "message": "Hello!",
            "timestamp": "[20:10, 27/08/2026]"
        }
    ],
    "error": ""
}
```

---

## 📊 Excel Report

The generated Excel report contains:

| Column             | Description               |
| ------------------ | ------------------------- |
| Name               | Contact name              |
| Phone              | Contact number            |
| Message            | Personalized message      |
| Sent               | Message sending status    |
| Screenshot         | Screenshot file path      |
| Extracted Messages | Last 3 messages           |
| Error              | Error information, if any |

---

## ⚠️ Error Handling

The automation uses exception handling to capture failures.

If an error occurs:

```text
Sent = False
Error = <error description>
```

The error is also included in the generated report.

---

## 🔐 WhatsApp Session

The script uses Playwright's persistent browser context:

```python
launch_persistent_context(
    "whatsapp_profile",
    headless=False
)
```

This stores browser session information locally.

**Do not share the `whatsapp_profile` directory**, because it may contain authentication/session data.

---

## ⚠️ Limitations

* WhatsApp Web's HTML structure and selectors can change.
* Contact search selectors may require maintenance.
* Message extraction depends on WhatsApp Web's current DOM.
* The script currently processes the **first contact** in the Excel file.
* It does not yet provide a sophisticated retry mechanism.
* Delivery/read confirmation is not fully implemented.
* It does not currently prevent duplicate messages.

---

## 🔮 Possible Enhancements

The bot can later be extended to support:

* [ ] Multiple contacts
* [ ] Contact-by-contact processing
* [ ] Retry mechanism
* [ ] Duplicate-message prevention
* [ ] Delivery-status verification
* [ ] Read-status verification
* [ ] Detailed logging
* [ ] Dry-run/test mode
* [ ] Scheduled execution
* [ ] Failed-contact retry queue
* [ ] Summary dashboard
* [ ] Email notification after execution
* [ ] CSV input support
* [ ] Configuration file
* [ ] Command-line arguments

---

## 🧪 Recommended Testing

Start with **one test contact** and a simple message:

```text
Hello {name}, this is a Playwright automation test.
```

Verify:

1. WhatsApp Web opens.
2. Contact is found.
3. Chat opens correctly.
4. `{name}` is replaced.
5. Message is sent.
6. Screenshot is created.
7. Messages are extracted.
8. JSON report is generated.
9. Excel report is generated.

---

## 📜 Disclaimer

This project is intended for **learning, testing, and authorized automation** of WhatsApp Web workflows. Use it responsibly and comply with WhatsApp's applicable terms, policies, and messaging requirements.
