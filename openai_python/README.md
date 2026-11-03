# OpenAI Python Chat

A small command-line chat application that sends your messages to the OpenAI API and prints the responses in the terminal.

## Requirements

- Python
- An OpenAI API key

## Setup

From the project directory, create and activate a virtual environment in PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in this directory and add your API key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

Keep your API key private. The `.env` file and virtual environment are excluded from Git.

## Run

With the virtual environment activated:

```powershell
python app.py
```

Or run the virtual environment's Python directly without activating it:

```powershell
.\env\Scripts\python.exe app.py
```

Enter a message at the `User:` prompt to chat. Type `bye` to exit.

## Configuration

The application loads `OPENAI_API_KEY` from `.env` and uses the model configured in `app.py`. Change the `model` value there if you want to use a different model available to your API account.
