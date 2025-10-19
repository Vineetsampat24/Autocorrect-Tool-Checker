import language_tool_python
import re

# Initialize the tool
tool = language_tool_python.LanguageTool('en-US')

def smart_capitalize(text):
    # Capitalize the first letter of each sentence
    sentences = re.split('([.!?]\s*)', text)
    capitalized = ''.join([s.capitalize() for s in sentences])
    return capitalized

def correct_spelling(text):
    # Step 1: Correct grammar and spelling
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)

    # Step 2: Capitalize first letters of sentences
    corrected_text = smart_capitalize(corrected_text.strip())

    # Step 3: Ensure the paragraph ends with a punctuation (., !, ?)
    if not corrected_text.endswith(('.', '!', '?')):
        corrected_text += '.'

    return corrected_text
