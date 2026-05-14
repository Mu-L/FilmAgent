from typing import Any, Dict

from fastapi import APIRouter
from pydantic import BaseModel, Field

from config import Config, CONFIG_PATH

router = APIRouter(tags=["Configuration"])


class ConfigUpdateRequest(BaseModel):
    values: Dict[str, Any] = Field(default_factory=dict)


@router.get("/api/config")
async def get_config():
    return {
        "config": Config.as_dict(),
        "path": str(CONFIG_PATH),
    }


@router.put("/api/config")
async def update_config(req: ConfigUpdateRequest):
    return {
        "config": Config.update_config(req.values),
        "path": str(CONFIG_PATH),
    }
