from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def generate_depop_listing(image_path):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    raw_image = Image.open(image_path).convert('RGB')
    text_prompt = "Describe this item as if listing it on a fashion resale platform."
    
    inputs = processor(raw_image, text_prompt, return_tensors="pt")
    output = model.generate(**inputs)
    description = processor.decode(output[0], skip_special_tokens=True)
    
    listing = f"""
🔹 **Title:** [Brand] {description}
🔹 **Description:** 
- Condition: [Specify]
- Features: [Specify]
- Measurements: [Specify]
- Fit: [Specify]
- Defects: [Specify]
🔹 **Hashtags:** #[Brand] #[Style] #[Trend] #[Depop hashtag]
🔹 **Shipping:** Ships in 1-2 days. Tracking included. Open to bundle offers.
"""
    return listing

# Example usage:
image_file = input("Enter image path (e.g., item.jpg): ")
listing_text = generate_depop_listing(image_file)
print(listing_text)