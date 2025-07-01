import wikipedia
from transformers import pipeline

# ✅ Load upgraded model for better answers
qa_pipeline = pipeline("text-generation", model="google/flan-t5-large", do_sample=False)

# ✅ Wikipedia answer function with improved prompt and fallback
def get_wiki_answer(question):
    try:
        # Try short clean summary (5 sentences)
        try:
            context = wikipedia.summary(question, sentences=5)
        except:
            # Fallback to full content if summary fails
            page = wikipedia.page(wikipedia.search(question)[0])
            raw_text = page.content
            import re
            sentences = re.split(r'(?<=[.!?])\s+', raw_text)
            context = ""
            for sentence in sentences:
                if len(context) + len(sentence) > 1000:
                    break
                context += sentence + " "

        # ✅ Clean, structured prompt
        prompt = f"""
Using the context below, answer the following question in 2–3 complete sentences.

Question: {question}

Context:
{context.strip()}

Answer:
"""

        result = qa_pipeline(prompt.strip(), max_length=120)[0]['generated_text']
        answer = result.strip()

        # ✅ Basic check for empty/bad answers
        if len(answer) < 20:
            return "⚠️ Couldn't generate a meaningful answer."

        return answer

    except wikipedia.exceptions.DisambiguationError as e:
        return f"⚠️ Multiple topics found: {e.options[:3]}"
    except Exception:
        return "⚠️ Wikipedia lookup failed."

# ✅ Always use Wikipedia for all questions
def get_combined_answer(question):
    return f"📚 {get_wiki_answer(question)}"
