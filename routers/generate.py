from fastapi import APIRouter, status, HTTPException
from database import supabase
from validate import GenerateSchema
from ai import model


router = APIRouter(
    prefix="/api"
)


@router.post("/generate_story", status_code=status.HTTP_201_CREATED)
def generate_story(character: GenerateSchema):
    name = character.name.lower()
    data = supabase.from_("characters").select("details").eq("name", name).execute()
    if data.data:
        details = data.data[0]["details"]
    else:
        details = None

    if details != None:
        response = model.generate_content(f"You are an expert short story creator and narrate a 4 to 5 sentence story on character {name} and the character details are here: {details}")
        return ({"story" : response.text})
    else:
        raise HTTPException(status_code=404, detail=f"Sorry! No character named {name} found in the database.")