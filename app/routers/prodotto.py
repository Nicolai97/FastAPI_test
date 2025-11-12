from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models.prodotto import Prodotto, ProdottoCreate
from app.core.database import get_session
from app.crud.prodotto import create_product, products_list


router = APIRouter(prefix="/prodotti", tags=["prodotti"])

@router.post("/", response_model=Prodotto)
def create(prodotto: ProdottoCreate, session: Session = Depends(get_session)):
    if prodotto.prezzo <= 0:
        raise HTTPException(status_code=422, detail="Il prezzo deve essere maggiore di 0")
    return create_product(session, prodotto)

@router.get("/", response_model=list[Prodotto])
def get_list(esaurito: bool | None = None, session: Session = Depends(get_session)):
    return products_list(session, esaurito)
