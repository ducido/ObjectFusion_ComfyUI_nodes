import numpy as np
from PIL import Image
from torchvision import transforms


class ObjectCrop:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Original_image": ("IMAGE",),
                "Chosen_ID": ("INT", {
                    "default": 0,
                }),
                "BBOX": ("STRING", {
                    "multiline": True,
                })
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Chosen_Obj",)

    FUNCTION = "run"

    CATEGORY = "CROP_OBJECT"

    def run(self, Original_image, Chosen_ID, BBOX):

        try:
            bboxes = BBOX.split(';\n')[Chosen_ID].split(' - ')[-1].split(',')
            bboxes = list(map(float, bboxes))
            cropped = Original_image[:, int(bboxes[1]):int(bboxes[3]), int(bboxes[0]):int(bboxes[2]), :]
        except:
            cropped = Original_image

        return (cropped, )

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ObjectCrop": ObjectCrop
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ObjectCrop": "Object Cropping"
}
