from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from data_base.models import Training, Product, Uniduct, User_data


async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_uniducts(session: AsyncSession):
    query = select(Uniduct)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_trainings(session: AsyncSession):
    query = select(Training)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_product(session: AsyncSession, product_name: str):
    query = select(Product).where(Product.name == product_name)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_training(session: AsyncSession, training_id: int):
    query = select(Training).where(Training.id == training_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_add_id(session: AsyncSession, data: dict):  #не нужно, вручную
    obj = User_data(
        id=data["id"],
        user_id=data["user_id"],
        calc_data=data["price"],
        send=data["send"],
    )
    session.add(obj)
    await session.commit()






