from uuid import UUID

from fastapi import APIRouter, Depends

# from src.infrastructure.postgresql import db_utils

router = APIRouter(prefix="", tags=["test"])

@router.get("/")
async def ping():
    return "alive"