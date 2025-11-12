from sqlmodel import Session, select
from app.models.prodotto import Prodotto, ProdottoCreate

def create_product(session: Session, prodotto_data: ProdottoCreate) -> Prodotto:
    prodotto = Prodotto.from_orm(prodotto_data)
    session.add(prodotto)
    session.commit()
    session.refresh(prodotto)
    return prodotto

def products_list(session: Session, esaurito: bool | None = None):
    query = select(Prodotto)
    if esaurito is True:
        query = query.where(Prodotto.quantita == 0)
    elif esaurito is False:
        query = query.where(Prodotto.quantita > 0)
    return session.exec(query).all()
