from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Windmill(BaseModel):
    id: int
    name: str
    location: str

windmills = [
    Windmill(id=1, name="Windmill A", location="Field 1"),
    Windmill(id=2, name="Windmill B", location="Field 2"),
    Windmill(id=3, name="Windmill C", location="Field 3"),
]

@app.get("/windmills", response_model=list[Windmill])
async def get_windmills():
    return windmills

@app.get("/windmills/{windmill_id}", response_model=Windmill)
async def get_windmill(windmill_id: int):
    return windmills[windmill_id - 1]

@app.post("/windmills", response_model=Windmill)
async def create_windmill(windmill: Windmill):
    windmills.append(windmill)
    return windmill

@app.put("/windmills/", response_model=Windmill)
async def update_windmill(windmill: Windmill):
    for idx, wm in enumerate(windmills):
        if wm.id == windmill.id:
            windmills[idx] = windmill
            break
    return windmill

@app.delete("/windmills/{windmill_id}")
async def delete_windmill(windmill_id: int):
    windmills[:] = [wm for wm in windmills if wm.id != windmill_id]
    return {"message": "Windmill deleted"}