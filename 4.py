from transformers import pipeline
from PIL import Image

# ✅ Force a stable caption model
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

print("🤖 Image Description chatbot")
print("Type image file name (e.g. 'image.jpg') or 'exit' to quit.\n")

def describe_image(image_path):
    image = Image.open(image_path).convert("RGB")
    result = captioner(image)
    return result[0]["generated_text"]

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    try:
        caption = describe_image(user_input)
        print("Bot:", caption)
    except FileNotFoundError:
        print("Bot: Image not found.")
    except Exception as e:
        print("Bot error:", e)