from openai import OpenAI
import os
from tqdm import tqdm

from settings import SETTINGS

client = OpenAI()

folder_path = SETTINGS["FOLDER_PATH"]

# Function to create a file with the Files API
def create_file(file_path):
  with open(file_path, "rb") as file_content:
    result = client.files.create(
        file=file_content,
        purpose="vision",
    )
    return result.id


def call_api(file__id):
    api_response = client.responses.create(
        model="gpt-5",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text",
                 "text": ("find coordinates in this picture, then convert it to decimal coordinate format,"
                            "just return the pair value, for example: '4.2168, 126.7910', "
                            "if not found or does not match the required format, just return '0, 0'")
                },
                {
                    "type": "input_image",
                    "file_id": file__id,
                },
            ],
        }],
    )

    return api_response

if __name__ == "__main__":
    for file_name in tqdm(sorted(os.listdir(folder_path))):
        
        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            img_path = os.path.join(folder_path, file_name)
            file_id = create_file(img_path)
            response = call_api(file_id)

            output_text = response.output_text
            with open("output.csv", "a") as file:
                file.write(file_name + "," + output_text.replace(" ", "") + "\n")