from fastapi import APIRouter, status, HTTPException
from validate import CharacterSchema
from database import supabase


router = APIRouter(
    prefix="/api"
)


@router.get("/characters", status_code=status.HTTP_200_OK)
def characters():
    try:
        data = supabase.table("characters").select("*").execute()
        return data.data
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/create_character", status_code=status.HTTP_201_CREATED)
def create_character(character: CharacterSchema):
    try:
        data = supabase.table("characters").insert({
            "name": character.name.lower(),
            "details": character.details
        }).execute()
        return data
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="name already in use")