import google.generativeai as genai
import os
genai.configure(api_key="")
def classify_file_gemini(filename, filetype):
    prompt = f"""
You are a smart file organization assistant. Given a filename and its file type (like pdf, mp3, jpg, etc), 
predict a category folder such as: Documents, Music, Images, Archives, Receipts, Code, Videos, etc.

Filename: {filename}
File type: {filetype}

Just return the folder name only. No explanations.
"""

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

