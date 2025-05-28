# pip install transformers torch pillow

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import random

def generate_depop_listing(image_paths, brand, condition, measurements, fit, defects):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Fashion buzzwords
    buzzwords = ["effortless", "iconic", "statement-making", "timeless", "versatile", "chic", "on-trend", "must-have", "elegant", "vibrant", "sleek", 
    "sophisticated", "playful", "fashion-forward", "bold", "feminine", 
    "polished", "unique", "whimsical", "vintage", "y2k", "Y2K", "90s", , "rare", "preloved", "secondhand", "sustainable", "retro", "grunge", "minimalist",
    "aesthetic", "cozy", "boho", "edgy", "classic", "trendy", "unique", "handpicked", "limited-edition",
    "one-of-a-kind", "fashion-forward", "curated", "stylish", "bold", "elegant", "casual", "luxury", "boho", "cottage core", "mermaid core", "fairy core"]

    descriptions = []
    for path in image_paths:
        raw_image = Image.open(path).convert('RGB')
        inputs = processor(raw_image, return_tensors="pt")
        output = model.generate(**inputs, max_new_tokens=100)
        desc = processor.decode(output[0], skip_special_tokens=True)
        descriptions.append(desc)
    
    # Combine all descriptions into one
    combined_desc = " ".join(descriptions)
    style = combined_desc.split(' ')[-1] if combined_desc else 'style'
    category = "Top" if "top" in combined_desc.lower() else "Other"
    hashtags = f"#{brand} #{style.replace(' ', '_')} #[Depop] #[Trend]"

    # Select random buzzwords
    buzzword_phrase = ", ".join(random.sample(buzzwords, 3))
    title = f"{brand} {combined_desc.title()} – {buzzword_phrase.capitalize()}"
    paragraph = (f"Elevate your wardrobe with this {brand} {category} – {combined_desc}, "
                 f"crafted with {measurements} for a {fit.lower()} fit. "
                 f"In {condition.lower()} condition with {defects if defects.lower() != 'none' else 'no visible defects'}. "
                 f"A {buzzword_phrase} piece, perfect for turning heads and making a statement. "
                 f"Swipe through images to see every detail.")

    listing = f"""
🔹 **Title:** {title}
🔹 **Description:** {paragraph}
🔹 **Hashtags:** {hashtags}
🔹 **Shipping:** Ships in 1-2 days. Tracking included. Open to bundle offers.
"""
    return listing

# Example usage:
image_input = input("Enter image paths (comma-separated, e.g., item1.jpg,item2.jpg): ")
image_files = [path.strip() for path in image_input.split(",")]
brand = input("Enter brand: ")
condition = input("Enter condition: ")
measurements = input("Enter measurements: ")
fit = input("Enter fit: ")
defects = input("Enter defects (or 'None'): ")

listing_text = generate_depop_listing(image_files, brand, condition, measurements, fit, defects)
print(listing_text)