
import spacy

# Load the model (use the correct path if loading locally)
nlp = spacy.load("D://Manikanta//NLPusingSpacy//en_core_web_sm")  # Or provide the directory path to your local model

# Input text with clear entities
text = "John lives in India and works for Microsoft. His phone number is +91-9849558869."

# Process the text
doc = nlp(text)

# Extract and print recognized entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
