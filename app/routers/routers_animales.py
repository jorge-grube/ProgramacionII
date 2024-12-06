from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from database.engine import get_db
from utils.validators import AnimalValidator, SpecialAnimalValidator
from utils.repositories import AnimalRepository, ExoticAnimalRepository
from database.data.models import Animal as AnimalModel

router = APIRouter()

class Animal(BaseModel):
    id: Optional[int] = None
    name: str
    species: str
    breed: str
    age: int
    owner_id: int
    status: Optional[str] = "vivo"

    class Config:
        orm_mode = True

# Sustitución de validadores y repositorios
def create_animal_with_validator_and_repo(
    animal: Animal, db: Session, validator, repo
):
    """Crea un animal utilizando un validador y repositorio específicos."""
    validator.validate(db, animal.dict())
    return repo.add(db, animal.dict(exclude={'id'}))

@router.post("/animals", response_model=Animal, status_code=status.HTTP_201_CREATED)
def create_animal(animal: Animal, db: Session = Depends(get_db)):
    """Crea un nuevo animal estándar."""
    return create_animal_with_validator_and_repo(
        animal, db, AnimalValidator(), AnimalRepository()
    )

@router.post("/animals/exotic", response_model=Animal, status_code=status.HTTP_201_CREATED)
def create_exotic_animal(animal: Animal, db: Session = Depends(get_db)):
    """Crea un nuevo animal exótico."""
    return create_animal_with_validator_and_repo(
        animal, db, SpecialAnimalValidator(), ExoticAnimalRepository()
    )

@router.get("/animals", response_model=List[Animal])
def get_animals(db: Session = Depends(get_db)):
    """Obtiene todos los animales registrados."""
    return db.query(AnimalModel).all()

@router.get("/animals/count")
def get_animal_count(db: Session = Depends(get_db)):
    """Obtiene el número total de animales registrados."""
    count = db.query(AnimalModel).count()
    return {"total_animals": count}

@router.get("/animals/{animal_id}", response_model=Animal)
def get_animal(animal_id: int, db: Session = Depends(get_db)):
    """Obtiene un animal específico por su ID."""
    animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal

@router.put("/animals/{animal_id}", response_model=Animal)
def update_animal(animal_id: int, animal: Animal, db: Session = Depends(get_db)):
    """Actualiza los datos de un animal."""
    db_animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not db_animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    
    for key, value in animal.dict(exclude_unset=True).items():
        setattr(db_animal, key, value)
    
    db.commit()
    db.refresh(db_animal)
    return db_animal

@router.patch("/animals/{animal_id}/deceased", response_model=Animal)
def mark_animal_deceased(animal_id: int, db: Session = Depends(get_db)):
    """Marca un animal como fallecido."""
    db_animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not db_animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    
    db_animal.status = "fallecido"
    db.commit()
    db.refresh(db_animal)
    return db_animal

@router.delete("/animals/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Elimina un animal por su ID."""
    db_animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not db_animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    
    db.delete(db_animal)
    db.commit()
