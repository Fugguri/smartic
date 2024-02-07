import os
from .GPTService import GPTService
from .AssistantService import AssistantService
from config import cfg
# gpt_service = GPTService(api_key=cfg.tg_bot.openai)
assistant = AssistantService(api_key=cfg.tg_bot.openai)
