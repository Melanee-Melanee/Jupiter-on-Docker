from diffusers import StableDiffusionPipeline
import torch
import sys
from torch import autocast

device = "cuda"


def load_pipeline(cuda: bool = False):
    model_id = "CompVis/stable-diffusion-v1-4"

    print(f"cuda enabled = {cuda}")
    print("loading pipeline...")
    if cuda:
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id, revision="fp16", torch_dtype=torch.float16, use_auth_token=True
        )
        pipe = pipe.to(device)
    else:
        pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
    return pipe


def generate_image(
    pipeline: StableDiffusionPipeline, cuda: bool = False, prompt: str = ""
):
    print("running pipeline...")
    if cuda:
        with autocast("cuda"):
            data = pipeline(prompt, guidance_scale=7.5)
    else:
        data = pipeline(prompt)
    print(data)
    return data


def save_image(d):
    print("saving image...")
    image = data["sample"]
    image[0].save("tmp.png")
    print("image saved to tmp.png")


def main(cuda: bool = False):
    prompt = "a 1980s style logo saying chaos engineering"

    pipeline = load_pipeline(cuda=cuda)

    data = generate_image(pipeline, cuda, prompt)

    save_image(data)


if __name__ == "__main__":
    try:
        cuda_enabled = bool(sys.argv[1].title())
    except Exception as e:
        print(f"didnt get config {e}")
        cuda_enabled = False

    main(cuda=cuda_enabled)
