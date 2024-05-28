from pydantic import BaseModel

class CharacterSchema(BaseModel):
    name: str
    details: str

class GenerateSchema(BaseModel):
    name: str