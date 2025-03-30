# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Step1: Setup GROQ API key
from dotenv import load_dotenv
import os
import base64
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Step1: Setup GROQ API key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please set the environment variable.")

# Step2: Encode image to Base64
def encode_image(image_path):
    """
    Encodes an image file into a Base64 string.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Base64-encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            return encoded_string
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while encoding the image: {e}")
        return None

# Step3: Analyze image with query
def analyze_image_with_query(query, model, encoded_image):
    client = Groq()  
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    print("Messages:", messages)  # Debug: Print the messages being sent

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        print("Chat Completion Response:", chat_completion)  # Debug: Print the full response
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    query = "Is there something wrong with my face?"
    model = "llama-3.2-90b-vision-preview"
    encoded_image = encode_image("acne.jpg")  # Replace with the actual image path

    if encoded_image:
        result = analyze_image_with_query(query, model, encoded_image)
        print("Result:", result)
    else:
        print("Failed to encode the image.")