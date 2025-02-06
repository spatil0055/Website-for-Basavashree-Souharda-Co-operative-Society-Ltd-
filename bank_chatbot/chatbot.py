import spacy

nlp = spacy.load("en_core_web_md")  # Load spaCy's medium or large model
user_input = "I want to apply for a gold loan."
doc = nlp(user_input.lower())  # Normalize input

intents = {
    "gold loan": "I want to apply for a gold loan.",
    "repay loan": "How do I repay the loan?",
    "check balance": "What is my account balance?"
}
user_intent = max(intents, key=lambda intent: nlp(intents[intent]).similarity(doc))
print("Recognized Intent:", user_intent)

for ent in doc.ents:
    print(ent.text, ent.label_)  # e.g., "gold loan" → LOAN_TYPE

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)
pattern = [{"LOWER": "gold"}, {"LOWER": "loan"}]
matcher.add("GOLD_LOAN", [pattern])

matches = matcher(doc)
for match_id, start, end in matches:
    print("Matched:", doc[start:end].text)

responses = {
    "gold loan": "To apply for a gold loan, please contact our service providers.",
    "repay loan": "You can repay the loan through your savings account."
}
response = responses.get(user_intent, "I'm sorry, I didn't understand that.")
print("Response:", response)
