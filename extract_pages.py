import sys
import pypdf
import json

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:/Users/nghir/.gemini/antigravity/brain/0d5c8f5c-8f6d-4f16-8916-c0dc43f46d98/.user_uploaded/media_1792155982544_4d0cb928.pdf'
reader = pypdf.PdfReader(pdf_path)

pages_data = []
for i, page in enumerate(reader.pages):
    pages_data.append({
        "page_num": i + 1,
        "text": page.extract_text()
    })

with open("pages_raw.json", "w", encoding="utf-8") as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print("Saved pages_raw.json with", len(pages_data), "pages.")
