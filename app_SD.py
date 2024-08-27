from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5" #any model id from stable diffusion
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16) # if using cpu, remove torch_dtype=torch.float16
pipe = pipe.to("cuda") #"cpu" incase of no cuda

prompt = "a photo of an farmer laughing in a field with rainy atmosphere" #prompt
image = pipe(prompt).images[0]  
    
image.save("astronaut_rides_horse.png")
