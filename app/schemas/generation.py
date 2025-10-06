from pydantic import BaseModel, Field
from typing import Literal

class AIOptions(BaseModel):
    enable_pbr: bool = True
    should_remesh: bool = True
    should_texture: bool = True
    ai_model: Literal["latest", "meshy-5"] = "latest"