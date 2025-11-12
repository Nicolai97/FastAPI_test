from typing import Optional
from sqlmodel import SQLModel, Field

class ProdottoBase(SQLModel):
    nome: str
    prezzo: float
    quantita: int = 0

class Prodotto(ProdottoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ProdottoCreate(ProdottoBase):
    pass
