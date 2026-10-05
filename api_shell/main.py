'''
Task 1: Service request tracker API (45-60 min)
Build a small FastAPI app for citizens to submit service requests, such as "broken streetlight".

POST /requests creates one with title, description, and category. Status starts as open. Reject an empty title with a 422.
GET /requests lists them, with optional ?status= and ?category= filters and limit/offset pagination.
GET /requests/{id} returns one, or a 404 with a clear message.
PATCH /requests/{id}/status moves it open -> in_progress -> resolved. Reject illegal jumps (you already have the state machine from the mock).
In-memory storage is fine. Write 4-5 tests with TestClient.
'''

from enum import StrEnum
from itertools import count

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Service Requests")

class Status(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    
TRANSITIONS: dict[Status, set[Status]] = {
    Status.OPEN: {Status.IN_PROGRESS},
    Status.IN_PROGRESS: {Status.RESOLVED},
    Status.RESOLVED: set(),
}

class RequestCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    category: str
    
class RequestRead(BaseModel):
    id: int
    title: str
    description: str
    category: str
    status: Status
    
class StatusUpdate(BaseModel):
    status: Status
    
DB: dict[int, RequestRead] = {}
_ids = count(1)

@app.post("/requests", response_model=RequestRead, status_code=201)
def create_request(body: RequestCreate):
    new_id = next(_ids)
    item = RequestRead(id=new_id, status=Status.OPEN, **body.model_dump())
    DB[new_id] = item
    return item

@app.get("/requests", response_model=list[RequestRead])
def list_requests(
    status: Status | None = None,
    category: str | None = None,
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    items = list(DB.values())
    if status:
        items = [i for i in items if i.status == status]
    if category:
        items = [i for i in items if i.category == category]
    return items[offset : offset + limit]

@app.get("/requests/{request_id}", response_model=RequestRead)
def get_request(request_id: int):
    item = DB.get(request_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Request not found")
    return item

@app.patch("/requests/{request_id}/status", response_model=RequestRead)
def update_status(request_id: int, body: StatusUpdate):
    item = get_request(request_id)
    if body.status not in TRANSITIONS[item.status]:
        raise HTTPException(
            status_code = 409,
            detail=f"Cannot go from {item.status} to {body.status}"
        )
    item.status = body.status
    return item