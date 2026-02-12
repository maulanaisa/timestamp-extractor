from openai import OpenAI
import os
from tqdm import tqdm

from settings import SETTINGS, OPENAI_API_IMAGE

client = OpenAI()

folder_path = SETTINGS["IMAGES_PATH"]

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
        model=OPENAI_API_IMAGE["MODEL"],
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text",
                 "text": OPENAI_API_IMAGE["PROMPT"]
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
            with open("output_openai_api.csv", "a") as file:
                if OPENAI_API_IMAGE["OUTPUT"] == "coordinates-custom":
                    file.write(file_name + "," + output_text.strip() + "\n")
                elif OPENAI_API_IMAGE["OUTPUT"] == "" or OPENAI_API_IMAGE["OUTPUT"] is None:
                    file.write(file_name + "," + output_text + "\n")
                else:
                    raise ValueError("Output type not found!")