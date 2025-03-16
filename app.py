import streamlit as st
from PIL import Image
import io
import os

# CSS for a more professional look
st.markdown("""
<style>
    /* Center the title */
    h1 {
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }

    /* Subtext styling */
    .subheader-text {
        text-align: center;
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-top: -10px;
        margin-bottom: 2rem;
    }

    /* Customize file uploader */
    .css-19nhvcg.e1fqkh3o3 {
        border: 2px dashed #00dbde; /* border color */
        border-radius: 1rem;
        background-color: rgba(0,219,222,0.05);
    }

    /* Button styling */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(to right, #fc00ff, #00dbde);
        color: white;
        border: none;
        border-radius: 0.5rem;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        box-shadow: 0px 3px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.1s ease-in-out;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        transform: scale(1.02);
    }

    /* Center alignment for success message */
    .stAlert {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def convert_image(image_file, output_format):
    image = Image.open(image_file)
    img_byte_arr = io.BytesIO()
    valid_formats = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".webp": "WEBP"}

    if output_format not in valid_formats:
        raise ValueError("Unsupported file format")

    image.save(img_byte_arr, format=valid_formats[output_format])
    return img_byte_arr.getvalue()

with st.sidebar:
    st.image("logo.png")
    st.title("Documentation")
    st.markdown("---")
    st.write("""
    **How to Use Image Converter:**
    1. **Upload Your Image**: Click the uploader and select an image file (.jpg, .jpeg, .webp, .png).
    2. **Select Output Format**: Choose the desired format from the dropdown (WEBP, JPG, PNG).
    3. **Download the Converted File**: Click the 'Download' button to save your new image.

    **Supported Formats:**
    - Input: JPG, JPEG, PNG, WEBP
    - Output: JPG, PNG, WEBP

    **Notes:**
    - Large images may take a few seconds to convert.
    - Ensure your file is in a supported format to avoid errors.
    """)

st.title("Image Converter")
st.markdown("<p class='subheader-text'>Convert your images to .webp, .jpg, or .png in a flash!</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "webp", "png"])

output_format = st.selectbox("Convert to", (".webp", ".jpg", ".png"))

if uploaded_file:
    # Detect file extension
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    st.write(f"**Detected file type:** {file_extension}")

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_column_width=True,
        output_format="auto",
        channels="RGB",
        clamp=False
    )

    converted_data = convert_image(uploaded_file, output_format)

    st.download_button(
        label=f"Download {output_format.upper()}",
        data=converted_data,
        file_name=f"converted_image{output_format}",
        mime=f"image/{output_format.replace('.', '')}"
    )
    st.success(f"Image successfully converted to {output_format.upper()}!")
