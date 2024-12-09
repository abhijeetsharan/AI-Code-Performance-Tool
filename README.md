# AI-Powered Code Optimization Tool

An AI-powered tool to analyze code snippets for performance bottlenecks and provide optimization suggestions via a user-friendly interface.

---

## Features

- Detect performance bottlenecks in code.
- Suggest optimizations.
- Simple UI for uploading code and viewing results.

---

## Requirements

- **Python** (3.7 or later)
- **Flask**
- **Browser**

---

## Setup

### Clone the Repository
```bash
git clone <repository-url>
cd ai-performance-tool
```

### Backend Setup
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```
   The server runs at `http://127.0.0.1:5000`.

### Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd ../frontend
   ```
2. Open `index.html` in your browser:
   ```bash
   open index.html  # macOS/Linux
   start index.html # Windows
   ```

---

## Usage
1. Paste a code snippet in the frontend text area.
2. Click **Analyze**.
3. Review the detected issues and suggestions.

---

## Project Structure

```
ai-performance-tool/
|
|-- backend/
|   |-- app.py                # Flask backend code
|   |-- performance_analysis.py  # Code analysis logic
|   |-- requirements.txt      # Python dependencies
|
|-- frontend/
|   |-- index.html            # Main HTML file
|   |-- script.js             # Frontend logic
|   |-- style.css             # Styling
|
|-- README.md                 # Documentation
```

---

## Assumptions and Limitations

- Only supports Python snippets.
- Detects common performance issues (e.g., nested loops).
- Optimization is rule-based.
