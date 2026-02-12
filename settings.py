SETTINGS = {
    "IMAGE_DIMENSION"       :   {
                                "height" : 150,
                                "width" : 120,
                                },
    "IMAGE_QUALITY"         :   15,          #value between 1-100
    "PDF_FOLDER_PATH"       :   r"C:\Users\PLN\Downloads\pdf",
    "IMAGES_PATH"           :   r"C:\Users\PLN\Downloads\11Feb2026",
    "LOCATION_COORDINATES"  :   r"C:\Users\PLN\Downloads\tagging desa.csv",
    "EXPORT_PATH"           :   r"C:\Users\PLN\Documents\Projects\timestamp-extractor\optimize.xlsx",
}

OPENAI_API_IMAGE = {
    "MODEL"                 :   "gpt-5",
    "PROMPT"                :   """
                                find coordinates in this picture, then convert it to decimal coordinate format,
                                just return the pair value like this example: 4.2168,126.7910, "
                                if not found, just return 0,0
                                """,
    "OUTPUT"                :   "coordinates-custom", # if empty string, then return as is
}