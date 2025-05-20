# gemini_helper.py

import google.generativeai as genai
from PIL import Image

def explain_diff_with_gemini(image_path, api_key):
    try:
        # Configure API key
        genai.configure(api_key=api_key)

        # Load the diff image
        img = Image.open(image_path)

        # Use Gemini Flash for speed and image support
        #model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        model = genai.GenerativeModel(model_name="gemini-2.5-flash-preview-05-20")

        prompt = (
            "You are looking at a visual diff image created by comparing two webpage screenshots: a 'baseline' and a 'current' version. "
            "This diff image shows changes using colors — areas that are black or nearly black represent **no changes**, while colored areas represent **differences**.\n\n"

            "Here is how to interpret the diff image:\n"
            "- **Black areas** = No change.\n"
            "- **Cyan (bright blue)** = Often used to highlight **border or layout changes**, especially around elements. If a border is highlighted in cyan, it may indicate changes to the **border radius, border color, or padding**.\n"
            "- **Red or magenta** = Often indicates **text or image changes**, such as new icons, updated fonts, or layout adjustments.\n"
            "- **White** = Could indicate an **added or removed element**.\n"
            "- **Yellow** = May suggest changes to **spacing, alignment, or shadow effects**.\n\n"

            "📌 Example interpretations:\n"
            "- A **cyan outline** around a button likely means the **border radius or border styling** has changed.\n"
            "- A **white block** where an element used to be may indicate it's been **removed**.\n"
            "- A **red patch** over a heading might mean the **text changed or shifted** slightly.\n\n"

            "Your task is to carefully describe the differences **based only on the colored areas** of the diff image. "
            "Do not describe anything that looks black. Be specific, and if you see color near edges or borders, mention what that could imply (e.g., border radius, padding, alignment). "
            "Write clearly in plain English so developers and testers can understand exactly how the webpage has visually changed."
        )

        # Generate response
        response = model.generate_content([prompt, img], stream=False)

        return response.text

    except Exception as e:
        return f"Gemini API Error: {str(e)}"
