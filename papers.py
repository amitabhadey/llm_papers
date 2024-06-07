import streamlit as st
import pandas as pd

# Load the CSV file
file_path = 'papers.csv'
papers_df = pd.read_csv(file_path)

# Convert the dataframe to a list of dictionaries
papers = papers_df.to_dict(orient='records')

st.title("Foundational Papers in LLM")
st.write("A showcase of key papers in the field of Large Language Models (LLMs)")

# Add a banner image
st.image("https://media.wired.com/photos/63a11855a12918bc073554af/master/pass/02_Mind-your-language.jpg", use_column_width=True)
# Centered caption
st.markdown('<p style="text-align: center;">Illustration: Scott Balmer, Wired</p>', unsafe_allow_html=True)


# Search bars
search_title = st.text_input("Search papers by title")
search_author = st.text_input("Search papers by author")
search_summary = st.text_input("Search papers by keywords")
search_year = st.selectbox("Filter papers by year", options=[None] + sorted(papers_df['Year'].unique().tolist()))

# Filtering based on search terms
filtered_papers = papers
if search_title:
    filtered_papers = [paper for paper in filtered_papers if search_title.lower() in paper["Paper"].lower()]
if search_author:
    filtered_papers = [paper for paper in filtered_papers if search_author.lower() in paper["Authors"].lower()]
if search_summary:
    filtered_papers = [paper for paper in filtered_papers if search_summary.lower() in paper["Summary"].lower()]
if search_year:
    filtered_papers = [paper for paper in filtered_papers if paper["Year"] == search_year]

# Display filtered papers
for paper in filtered_papers:
    st.header(paper["Paper"])
    st.subheader(paper["Authors"])
    st.markdown(f'<p style="font-size:18px;">{paper["Summary"]}</p>', unsafe_allow_html=True)
    st.markdown(f"[Read more]({paper['Link']})")

# Add a footer
footer = """
    <style>
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #333;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <footer>
        <p>Made with ♥︎ by Amitabha Dey</p>
    </footer>
"""

st.markdown(footer, unsafe_allow_html=True)