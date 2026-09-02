# Movie Info Extractor

A Generative AI application that extracts structured movie information from an unstructured movie description.

## Features

* Extracts movie title
* Extracts release year
* Identifies movie genres
* Extracts director information
* Extracts cast members
* Extracts movie rating
* Generates a movie summary
* Returns structured JSON output
* Simple and interactive Streamlit interface

## Technologies Used

* Python
* Streamlit
* LangChain
* Mistral AI
* Pydantic

## How It Works

The application takes a movie description as input and sends it to a Mistral AI model through LangChain.

A Pydantic schema defines the required movie fields, and `PydanticOutputParser` converts the model's response into structured data.

### Workflow

```text
Movie Description
       ↓
ChatPromptTemplate
       ↓
Mistral AI
       ↓
PydanticOutputParser
       ↓
Structured Movie Information
       ↓
Streamlit UI
```

## Extracted Information

The application extracts:

```text
Title
Release Year
Genre
Director
Cast
Rating
Summary
```

##  Installation

Clone the repository:

```bash
git clone https://github.com/zohaibthaheem21/GenAI.git
cd GenAI/Movie-Info-Extractor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```text
MISTRAL_API_KEY=your_api_key_here
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Purpose

This project was built to practice Generative AI concepts, including:

* LLM integration
* Prompt templates
* Structured output
* Pydantic data validation
* LangChain
* Streamlit application development

## Author

**Zohaib Ali Thaheem**

GitHub: `https://github.com/zohaibthaheem21`
