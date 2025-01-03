from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from model.orm.write_model.merchant_write_model import SKU

def seed_merchant_write_model_data(db_engine: Engine):

    seed_skus = [
        SKU(name="water", price=101),
        SKU(name="data", price=102),
        SKU(name="food", price=103),
    ]

    with Session(db_engine) as db_session:

        with db_session.begin():            

            existing_skus = db_session.execute(
                select(SKU)
            ).scalars().all()

            print(existing_skus)

            for sku in seed_skus:
                if len([sku for sku in existing_skus if sku.name == sku.name]) == 0:
                    db_session.add(sku)
            
            db_session.flush()
