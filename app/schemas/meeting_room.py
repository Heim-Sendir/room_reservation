from typing import Optional

from pydantic import BaseModel, Field, root_validator, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)

    class Config:

        @root_validator
        def validate_name(cls, values):
            if not values['name']:
                raise ValueError('Name is required')
            elif len(values['name']) > 100:
                raise ValueError('Name is too long')
            return values


class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
