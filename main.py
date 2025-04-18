from flask import Flask, render_template, request, send_from_directory
from diffusers import StableDiffusionPipeline
import torch
import os

app = Flask(__name__)
model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32)
model = model.to("cpu")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        image = model(prompt).images[0]
        path = "static/generated_image.png"
        image.save(path)
        return render_template("index.html", image_url=path, prompt=prompt)
    return render_template("index.html", image_url=None)

if __name__ == "__main__":
    app.run(debug=True)

