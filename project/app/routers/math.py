from app.tasks import math
from celery.utils import uuid
from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException

router = APIRouter(
    prefix="/math",
)


@router.get("/")
async def math_divide(request: Request):
    # Start asynchronous task
    task = math.divide.apply_async(
        args=[
            1,
            2,
        ],
        task_id="divide-" + uuid(),
    )
    return {"url": request.url_for("math_task_status", **{"task_id": task.id})}


@router.get("/divide/task-status/{task_id}")
async def math_task_status(task_id: str):

    if not task_id.startswith("divide-"):
        raise HTTPException(status_code=404, detail="Wrong task id")
    task = math.divide.AsyncResult(task_id)
    response = {
        "state": task.state,
    }

    return response
