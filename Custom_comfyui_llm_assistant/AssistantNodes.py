from .utils import *


class GenerateStableDiffsutionPromptLLM:
    @classmethod
    def INPUT_TYPES(cls):
        data = load_config()
        template_system = ""
        template_user = ""
        models = []

        if data:
            _prompt = data["default_generate_stable_diffsution_prompt"]
            if _prompt:
                _system = _prompt["system"]
                _user = _prompt["user"]
                if _system:
                    template_system = _system
                if _user:
                    template_user = _user
            _models = data["models"]
            if isinstance(_models, list) and len(_models) > 0:
                models = _models
            default_model = data["default_model"]
            if default_model and len(_models) > 0:
                default_model_index = models.index(default_model)
                if default_model_index > 0:
                    models.pop(default_model_index)
                    models.insert(0, default_model)
        return {
            "required": {
                "object1": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": ""
                }),
                "desc_obj1": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": ""
                }),
                "object2": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": ""
                }),
                "desc_obj2": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": ""
                }),
                "template_system": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": template_system,
                    "display": "textarea",
                }),
                "template_user": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": template_user,
                    "display": "textarea"
                }),
                "stop": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": False,
                    "default": None
                }),
                "response_pattern": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": False,
                    "default": None
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"
                }),

                "max_tokens": ("INT", {
                    "default": 300,
                    "min": -1,
                    "max": 2048,
                    "display": "number"
                }),
                "model_name": (models, {
                    "default": default_model,
                    "display": "select"
                })
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("stable diffsution prompt",)

    FUNCTION = "generateStableDiffsutionPrompt"

    CATEGORY = "cropcropcropcrop"

    def generateStableDiffsutionPrompt(self, object1, desc_obj1, object2, desc_obj2 ,template_system, template_user, stop, response_pattern,  temperature, max_tokens, model_name):
        config = load_config()
        openai_config = config["openai"]
        if openai_config is None:
            return (object,)
        api_base = openai_config["api_base"]
        api_key = openai_config["api_key"]
        if not (is_valid_string(api_base) and is_valid_string(api_key)):
            return (object,)
        _object = object
        if is_valid_string(template_user):
            _object = template_user.format(desc_obj1, object1, desc_obj2, object2)
        response = get_completion(_object, response_pattern, api_base, api_key, temperature, template_system,
                                  max_tokens, stop, model_name)
        return (response,)


class TranslateTextLLM:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        data = load_config()
        template_system = ""
        template_user = ""
        models = []

        if data:
            _prompt = data["default_translate_prompt"]
            if _prompt:
                _system = _prompt["system"]
                _user = _prompt["user"]
                if _system:
                    template_system = _system
                if _user:
                    template_user = _user
            _models = data["models"]
            if isinstance(_models, list) and len(_models) > 0:
                models = _models
            default_model = data["default_model"]
            if default_model and len(_models) > 0:
                default_model_index = models.index(default_model)
                if default_model_index > 0:
                    models.pop(default_model_index)
                    models.insert(0, default_model)
        return {
            "required": {
                "prompt": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": ""
                }),

                "template_system": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": template_system,
                    "display": "textarea",

                }),
                "template_user": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": template_user,
                    "display": "textarea"
                }),
                "stop": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": False,
                    "default": None
                }),
                "response_pattern": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": False,
                    "default": None
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"
                }),

                "max_tokens": ("INT", {
                    "default": 300,
                    "min": -1,
                    "max": 2048,
                    "display": "number"
                }),
                "model_name": (models, {
                    "default": default_model,
                    "display": "select"
                })
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "translateText"

    CATEGORY = "LLM"

    def translateText(self, prompt, template_system, template_user, stop, response_pattern, temperature, max_tokens, model_name):
        config = load_config()
        openai_config = config["openai"]
        if openai_config is None:
            return (prompt,)
        api_base = openai_config["api_base"]
        api_key = openai_config["api_key"]
        if not (is_valid_string(api_base) and is_valid_string(api_key)):
            return (prompt,)
        _prompt = prompt
        if is_valid_string(template_user):
            _prompt = template_user.format(prompt)
        response = get_completion(_prompt, response_pattern, api_base, api_key, temperature, template_system,
                                  max_tokens, stop, model_name)
        return (response,)


class ChatWithLLM:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        data = load_config()
        template_system = ""
        template_user = ""
        models = []

        if data:
            _prompt = data["default_chat_prompt"]
            if _prompt:
                _system = _prompt["system"]
                _user = _prompt["user"]
                if _system:
                    template_system = _system
                if _user:
                    template_user = _user
            _models = data["models"]
            if isinstance(_models, list) and len(_models) > 0:
                models = _models
            default_model = data["default_model"]
            if default_model and len(_models) > 0:
                default_model_index = models.index(default_model)
                if default_model_index > 0:
                    models.pop(default_model_index)
                    models.insert(0, default_model)
        return {
            "required": {
                "prompt": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": ""
                }),
                "template_system": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": template_system,
                    "display": "textarea"
                }),
                "template_user": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": True,
                    "default": template_user,
                    "display": "textarea"
                }),
                "stop": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": False,
                    "default": None
                }),
                "response_pattern": ("STRING", {
                    "dynamicPrompts": False,
                    "multiline": False,
                    "default": None
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"
                }),

                "max_tokens": ("INT", {
                    "default": 300,
                    "min": -1,
                    "max": 2048,
                    "display": "number"
                }),
                "model_name": (models, {
                    "default": default_model,
                    "display": "select"
                })
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "chatLLM"

    CATEGORY = "LLM"

    def chatLLM(self, prompt, template_system, template_user, stop, response_pattern,  temperature, max_tokens, model_name):
        config = load_config()
        openai_config = config["openai"]
        if openai_config is None:
            return (prompt,)
        api_base = openai_config["api_base"]
        api_key = openai_config["api_key"]
        if not (is_valid_string(api_base) and is_valid_string(api_key)):
            return (prompt,)
        _prompt = prompt
        if is_valid_string(template_user):
            _prompt = template_user.format(prompt)
        response = get_completion(_prompt, response_pattern, api_base, api_key, temperature, template_system,
                                  max_tokens, stop, model_name)
        return (response,)


NODE_CLASS_MAPPINGS = {
    "Generate Stable Diffsution Prompt With LLM duci": GenerateStableDiffsutionPromptLLM,
    # "Translate Text With LLM": TranslateTextLLM,
    # "Chat With LLM": ChatWithLLM,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Generate Stable Diffsution Prompt With LLM duci": "HUHU",
    # "Translate Text With LLM": "Translate Text With LLM",
    # "Chat With LLM": "Chat With LLM",
}
