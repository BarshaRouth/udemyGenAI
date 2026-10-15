# Udemy Gen AI Projects

A repository containing hands-on Generative AI projects built using Python, Google Gemini SDKs, and Streamlit.

## 🚀 Quick Setup & Installation

Follow these steps to set up the project environment from scratch.

### 1. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you need to update `pip`, run:

```bash
python -m pip install --upgrade pip
```

## 🔑 Managing Environment Variables

### 1. Create a `.env` File

Create a file named `.env` in the root directory of the project and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your actual API key.

**Important:** Never share your API key or upload your `.env` file to GitHub.

## ▶️ Running the Projects

Make sure your virtual environment is activated before running any script.

### 1. Run a Standard Python Script

```bash
python test_gemini_speed.py
```

### 2. Run Streamlit Web Applications

**Vision Application:**
```bash
streamlit run vision.py
```

**Invoice Extractor Application:**
```bash
streamlit run invoice_extractor.py
```

Streamlit will provide a local URL in your terminal. Open that URL in your browser to access the application.

## 📦 Managing Dependencies

Whenever you install new Python packages, update `requirements.txt` to keep track of your project's dependencies.

To save the installed packages:

```bash
pip freeze > requirements.txt
```

To reinstall dependencies later:

```bash
pip install -r requirements.txt
```

## 🛡️ Git Configuration (`.gitignore`)

Create a `.gitignore` file in the root directory of your repository and add the following entries to prevent unnecessary files and sensitive information from being uploaded to GitHub:

```gitignore
# Environment variables and secrets
.env
.streamlit/secrets.toml

# Virtual environment
venv/
.venv/

# Python cache files
__pycache__/
*.py[cod]

# IDE settings
.vscode/

# Operating system files
.DS_Store
Thumbs.db
```

## 🔄 Recreating the Virtual Environment

If your virtual environment becomes corrupted or you want to reinstall your dependencies, delete the existing `venv` folder and recreate it by following the setup instructions above.

Once the environment is activated, reinstall all dependencies using:

```bash
pip install -r requirements.txt
```

This makes it easy to restore your development environment without manually installing each package.

## 📁 Project Structure

Your repository may follow a structure similar to this:

```text
Udemy-Gen-AI-Projects/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── test_gemini_speed.py
├── vision.py
├── invoice_extractor.py
└── venv/
```

**Note:** The `.env` and `venv/` entries are shown for illustration. They should not be uploaded to GitHub.

## 🎯 Project Goals

- Explore Generative AI concepts through practical projects.
- Integrate Google Gemini models using Python.
- Build interactive AI applications with Streamlit.
- Practice API integration, environment management, and dependency handling.
- Develop hands-on skills for building and deploying Generative AI applications.

---

**Happy Coding! 🚀**