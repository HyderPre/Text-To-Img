# 🖼️ Text-to-Image Generator using Stable Diffusion

A web-based application that generates realistic images from natural language prompts using the **Stable Diffusion** model.  
Built using **Flask**, **Hugging Face**, and **PyTorch** — a great open-source alternative to DALL·E.

---

## 📌 Features

- Generate high-quality images from text prompts  
- Based on Stable Diffusion (open-source)  
- Easy-to-use web interface with a loading spinner  
- Save and view generated images directly in the browser  
- Inspired by COCO-style caption prompts  

---

## 🧪 Technologies Used

- 🧠 **Model**: Stable Diffusion (`CompVis/stable-diffusion-v1-4`)  
- ⚙️ **Backend**: Python, Flask, PyTorch  
- 🎨 **Frontend**: HTML, CSS, JavaScript  
- 🔍 **Tokenizer**: CLIP (used internally by the model)  

---

## 🧰 Requirements

Install the required libraries:

```bash
pip install flask diffusers torch matplotlib
```

Or, use a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment (Windows Git Bash)
source venv/Scripts/activate

# Install the requirements
pip install flask diffusers torch matplotlib
```

To freeze dependencies:

```bash
pip freeze > requirements.txt
```

---

## 🚀 How to Run

1. Clone the repo or download the files:

```bash
git clone https://github.com/your-username/text-to-image-stable-diffusion.git
cd text-to-image-stable-diffusion
```

2. (Optional) Create and activate the virtual environment as shown above.

3. Run the Flask app:

```bash
python main.py
```

4. Open in your browser:

```
http://127.0.0.1:5000
```

5. Enter a prompt like:

```
A cat wearing sunglasses on a beach
```

---

## 📂 Project Structure

```
.
├── main.py                   # Flask backend
├── templates/
│   └── index.html           # Web interface
├── static/
│   ├── style.css            # Spinner and styling
│   ├── script.js            # Show loading animation
│   └── generated_image.png  # Output image
├── venv/                    # Virtual environment folder (optional)
```

---

## 🧠 How It Works

- User inputs a **text prompt** (e.g., "A red panda playing guitar").
- Prompt is sent to the **Stable Diffusion** model via Flask backend.
- Model returns a generated image.
- Image is saved and displayed on the same page.

---

## 📸 Sample Prompts

- *"A dog riding a skateboard in Times Square"*  
- *"A bowl of ramen floating in space"*  
- *"A futuristic city under a purple sky"*

---

## 📘 Dataset Info

This project is inspired by **COCO Captions-style** prompts.  
The original model was trained on the **LAION-5B** dataset — a large-scale open-source image-text dataset.

---

## 🔍 Keywords for Search Engines

This project is related to:

- Text to Image generation  
- DALL·E alternative  
- Stable Diffusion web app  
- AI image generator from text  
- Python Flask image generator  
- Hugging Face Diffusers example  
- CLIP guided image generation  
- COCO-style caption prompts  
- Generate images from text prompt  
- Open-source DALL·E  
- AI Art from text  

---

## ✅ License

This project uses open-source models from Hugging Face and is for **educational and research purposes only**.
