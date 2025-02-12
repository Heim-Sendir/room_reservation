from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.meeting_room import MeetingRoom


# Создаем новый класс, унаследованный от CRUDBase.
class CRUDMeetingRoom(CRUDBase):

    # Преобразуем функцию в метод класса.
    async def get_room_id_by_name(
            # Дописываем параметр self.
            # В качестве альтернативы здесь можно
            # применить декоратор @staticmethod.
            self,
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(MeetingRoom.id).where(
                MeetingRoom.name == room_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id


# Объект crud наследуем уже не от CRUDBase,
# а от только что созданного класса CRUDMeetingRoom.
# Для инициализации передаем модель, как и в CRUDBase.
meeting_room_crud = CRUDMeetingRoom(MeetingRoom)


# async def create_meeting_room(
#     new_room: MeetingRoomCreate,
#     session: AsyncSession,
# ) -> MeetingRoom:
#     new_room_data = new_room.dict()
#     db_room = MeetingRoom(**new_room_data)
#     session.add(db_room)
#     await session.commit()
#     await session.refresh(db_room)
#     return db_room


# async def get_room_id_by_name(
#     room_name: str,
#     session: AsyncSession,
# ) -> Optional[int]:
#     db_room_id = await session.execute(
#         select(MeetingRoom.id).where(
#             MeetingRoom.name == room_name
#         )
#     )
#     db_room_id = db_room_id.scalars().first()
#     return db_room_id


# async def read_all_rooms_from_db(session: AsyncSession) -> list[MeetingRoom]:
#     db_room = await session.execute(select(MeetingRoom))
#     return db_room.scalars().all()


# async def get_meeting_room_by_id(
#     room_id: int,
#     session: AsyncSession,
# ) -> Optional[MeetingRoom]:
#     db_room_id = await session.execute(
#         select(MeetingRoom).where(
#             MeetingRoom.id == room_id
#         )
#     )
#     db_room_id = db_room_id.scalars().first()
#     return db_room_id


# async def update_meeting_room(
#     db_room: MeetingRoom,
#     room_in: MeetingRoomUpdate,
#     session: AsyncSession,
# ) -> MeetingRoom:
#     # Представляем объект из БД в виде словаря.
#     obj_data = jsonable_encoder(db_room)
#     # Конвертируем объект с данными из запроса в словарь,
#     # исключаем неустановленные пользователем поля.
#     update_data = room_in.dict(exclude_unset=True)

#     # Перебираем все ключи словаря, сформированного из БД-объекта.
#     for field in obj_data:
#         # Если конкретное поле есть в словаре с данными из запроса, то...
#         if field in update_data:
#             # ...устанавливаем объекту БЖ новое значение атрибута.
#             setattr(db_room, field, update_data[field])
#     # Добавляем обновленный объект в сессию.
#     session.add(db_room)
#     # Фиксируем изменения
#     await session.commit()
#     # Обновляем объект из БД
#     await session.refresh(db_room)
#     return db_room


# async def delete_meeting_room(
#     db_room: MeetingRoom,
#     session: AsyncSession,
# ) -> MeetingRoom:
#     await session.delete(db_room)
#     await session.commit()
#     return db_room
