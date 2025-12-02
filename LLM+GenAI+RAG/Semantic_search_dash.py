import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai


# -------------------------
# CONFIG
# -------------------------
genai.configure(api_key="YOUR_API_KEY")
EMBED_MODEL = "text-embedding-004"


# -------------------------
# FUNCTION: Get Embedding
# -------------------------
def get_embedding(text):
    return genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )["embedding"]


# -------------------------
# STREAMLIT UI
# -------------------------
st.title("🔍 Semantic Search: Customer Feedback Analysis")
st.write("Find similar feedback using **Gemini Embeddings**.")


# ---- Upload CSV ----
uploaded_file = st.file_uploader("Upload CSV with a column named 'feedback'", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "feedback" not in df.columns:
        st.error("CSV must contain a 'feedback' column!")
    else:
        st.success("CSV uploaded successfully!")

        # Generate embeddings if not present
        if "embedding" not in df.columns:
            st.info("Generating embeddings... (only once)")
            df["embedding"] = df["feedback"].apply(get_embedding)
            st.success("Embeddings generated!")

        st.write("### 📝 Input your search query")
        query = st.text_input("Enter text (Example: 'delivery issues')")

        if query:
            q_emb = get_embedding(query)

            # Similarity scores
            df["similarity"] = df["embedding"].apply(
                lambda x: cosine_similarity([x], [q_emb])[0][0]
            )

            # Sort by similarity
            results = df.sort_values("similarity", ascending=False)

            st.write("### 📊 Top Matches")
            st.dataframe(
                results[["feedback", "similarity"]]
                .style.background_gradient(cmap="Greens")
            )

            # Expand embeddings
            st.write("### 🔍 Detailed Results")
            for i, row in results.iterrows():
                with st.expander(f"{row['feedback']} (similarity: {row['similarity']:.3f})"):
                    st.write(row["embedding"])
else:
    st.info("Upload a CSV file to begin.")
