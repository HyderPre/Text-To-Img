🖼️ Text-to-Image Generator using Stable Diffusion
A web-based application that generates realistic images from natural language prompts using the Stable Diffusion model. Built using Flask, Hugging Face, and PyTorch.

📌 Features
Generate high-quality images from text prompts

Based on Stable Diffusion (open-source)

Easy-to-use web interface with a loading spinner

Save and view generated images directly in the browser

Inspired by COCO-style caption prompts

🧪 Technologies Used
🧠 Model: Stable Diffusion (CompVis/stable-diffusion-v1-4)

⚙️ Backend: Python, Flask, PyTorch

🎨 Frontend: HTML, CSS, JavaScript

🔍 Tokenizer: CLIP (used internally by the model)

🧰 Requirements
Install the required libraries:

bash
Copy
Edit
pip install flask diffusers torch matplotlib
🚀 How to Run
Clone the repo or download the files:

bash
Copy
Edit
git clone https://github.com/your-username/text-to-image-stable-diffusion.git
cd text-to-image-stable-diffusion
Run the Flask app:

bash
Copy
Edit
python app.py
Open in your browser:

cpp
Copy
Edit
http://127.0.0.1:5000
Enter a prompt like:

css
Copy
Edit
A cat wearing sunglasses on a beach
📂 Project Structure
csharp
Copy
Edit
.
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Web interface
├── static/
│   ├── style.css            # Spinner and styling
│   ├── script.js            # Show loading animation
│   └── generated_image.png  # Output image
🧠 How It Works
User inputs a text prompt (e.g., "A red panda playing guitar").

Prompt is sent to the Stable Diffusion model via Flask backend.

Model returns a generated image.

Image is saved and displayed on the same page.

📸 Sample Prompts
"A dog riding a skateboard in Times Square"

"A bowl of ramen floating in space"

"A futuristic city under a purple sky"

📘 Dataset Info
This project is inspired by COCO Captions-style prompts. The original model was trained on the LAION-5B dataset — a large-scale open-source image-text dataset.

✅ License
This project uses open-source models from Hugging Face and is for educational and research purposes only.

