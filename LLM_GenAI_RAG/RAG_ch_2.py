import google.generativeai as genai
import faiss
import numpy as np

# -----------------------------------
# 1. CONFIGURE GEMINI API KEY
# -----------------------------------
genai.configure(api_key="YOUR_API_KEY_HERE")


# -----------------------------------
# 2. DOCUMENTS (These act like your PDF/CSV/Text)
# -----------------------------------
docs = [
    "Delivery was slow and took many days.",
    "The product quality is excellent and customers love it.",
    "Customer support responded quickly and resolved the issue.",
    "Shipping took more than a week and caused delays."
]


# -----------------------------------
# 3. CREATE EMBEDDINGS FOR EACH DOCUMENT
# -----------------------------------
def embed_text(text):
    return genai.embed_content(
        model="text-embedding-004",
        content=text
    )["embedding"]

embeddings_list = [embed_text(d) for d in docs]


# -----------------------------------
# 4. STORE EMBEDDINGS IN FAISS INDEX
# -----------------------------------
dimension = len(embeddings_list[0])            # size of embedding
index = faiss.IndexFlatL2(dimension)           # create FAISS index
index.add(np.array(embeddings_list).astype('float32'))  # add vectors


# -----------------------------------
# 5. USER QUERY → FIND SIMILAR DOCS
# -----------------------------------
query = "delivery problems"
query_emb = np.array([embed_text(query)]).astype('float32')

k = 2                                          # return top 2 matches
distances, positions = index.search(query_emb, k)

print("Top matched document indexes:", positions)
print()


# -----------------------------------
# 6. BUILD CONTEXT FROM MATCHED DOCS
# -----------------------------------
retrieved_docs = "\n".join([docs[i] for i in positions[0]])
print("Retrieved Docs Context:\n", retrieved_docs)
print()


# -----------------------------------
# 7. SEND CONTEXT → GEMINI FOR FINAL ANSWER
# -----------------------------------
model = genai.GenerativeModel("gemini-2.0-pro")

prompt = f"""
Using ONLY the information below, answer the question:

Context:
{retrieved_docs}

Question:
What issues are customers facing?

"""

response = model.generate_content(prompt)

print("Final Answer from Gemini:\n")
print(response.text)
