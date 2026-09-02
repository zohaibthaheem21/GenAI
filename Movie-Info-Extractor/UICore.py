import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel
from typing import List, Optional

from langchain_mistralai import ChatMistralAI


# -------------------- Setup --------------------

load_dotenv()

@st.cache_resource
def get_model():
    return ChatMistralAI(
        model="mistral-small-2506",
        temperature=0.2
    )

model = get_model()

# -------------------- Schema --------------------

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# -------------------- Prompt --------------------

prompt = ChatPromptTemplate.from_messages([
    ("system",
        """
        Extract movie information from the paragraph.
        {format_instructions}
        """
    ),
    ("human",
    "{paragraph}"
    )
])

# -------------------- Page --------------------

st.set_page_config(
    page_title="Movie Info Extracter",
    page_icon="🎬",
    layout="centered"
)

# -------------------- Simple Styling --------------------

st.markdown("""
<style>

.stApp {
    background-color: #ffffff;
}

/* Main title */
h1 {
    color: #111111 !important;
}

/* Normal text */
p {
    color: #333333;
}

/* Subheading */
h2, h3 {
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
}

div[data-testid="stButton"] button {
    background-color: #000000 !important;
    border: 1px solid #000000 !important;
    color: #ffffff !important;
    opacity: 1 !important;
}

div[data-testid="stButton"] button p {
    color: #ffffff !important;
}

div[data-testid="stButton"] button span {
    color: #ffffff !important;
}

/* Result box */
.result-box {
    background-color: #f7f7f7;
    padding: 15px 20px;
    border-radius: 8px;
    margin-top: 15px;
    color: #222222;
}

/* Reduce space between fields */
.result-box b {
    color: #111111;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------

st.title("Movie Info Extracter")
st.write("Enter a movie description and extract its information.")

# -------------------- Input --------------------

paragraph = st.text_area(
    "Movie Description",
    height=180,
    placeholder="Enter a movie description here..."
)

# -------------------- Button --------------------

if st.button("Extract Information"):
    
    if not paragraph.strip():
        st.warning("Please enter a movie description first.")
    else:
        # Show analyzing message below button
        with st.spinner("Analyzing movie..."):
            try:

                # -------------------- Create Prompt --------------------

                final_prompt = prompt.invoke(
                    {
                        "paragraph": paragraph,
                        "format_instructions":parser.get_format_instructions()
                    }
                )

                # -------------------- Send to Mistral --------------------

                response = model.invoke(final_prompt)

                # -------------------- Parse Response --------------------

                movie_data = parser.parse(response.content)

                # -------------------- Result --------------------

                st.subheader("Movie Information")

                st.markdown(
                    f"""
                    <div class="result-box">
                    <b>Title:</b> {movie_data.title}<br>
                    <b>Release Year:</b> {movie_data.release_year}<br>
                    <b>Genre:</b> {", ".join(movie_data.genre)}<br>
                    <b>Director:</b> {movie_data.director}<br>
                    <b>Cast:</b> {", ".join(movie_data.cast)}<br>
                    <b>Rating:</b> {movie_data.rating}<br>
                    <b>Summary:</b> {movie_data.summary}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.subheader("Raw Model Output")
                st.code(response.content, language="json")

                st.subheader("Structured Output")
                st.json(movie_data.dict())

            except Exception as e:
                st.error("Could not extract movie information.")
                st.exception(e)