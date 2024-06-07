# Foundational Papers in LLM

This project showcases key papers in the field of Large Language Models (LLMs) using a simple web app built with Streamlit. The web app allows users to search and filter papers by title, author, summary, and publication year.

[View demo](https://llmpapers.streamlit.app/)

## Files Included
- `papers.csv`: A CSV file containing the details of the foundational papers, including title, authors, summary, link, and year of publication.
- `papers.py`: The Streamlit application code to display and search through the papers.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amitabhadey/llm_papers.git
   cd foundational-papers-llm

2. **Install the required dependencies:**:
   Ensure you have Python installed. It's recommended to use a virtual environment.
   ```bash
   pip install streamlit pandas
   
3. **Run the Streamlit app:**:
   ```bash
   streamlit run papers.py

4. View the app:
   The app will open in your default web browser. You can search and filter the papers by title, author, summary, and year.

## Customizing for Your Own Domain Topics

You can use this code to create a similar web app for papers in your own domain topics by updating the papers.csv file.

1. Update the CSV file:
Replace the content of papers.csv with your own data. Ensure the CSV file includes the following columns: Paper, Authors, Summary, Link, and Year.

2. Run the app:
After updating the CSV file, run the Streamlit app again using the command:
   ```bash
   streamlit run papers.py
