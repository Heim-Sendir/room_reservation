import datetime

from pydantic import BaseModel, root_validator, validator


class ReservationBase(BaseModel):
    from_reseve: datetime
    to_reserve: datetime


class ReservationUpdate(ReservationBase):

    @validator('from_reseve')
    def check_from_reserve_later_than_now(cls, values):
        if values <= datetime.datetime.now():
            raise ValueError(
                'Дата начала бронирования должна быть позже текущей даты!'
            )
        return values

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reseve'] >= values['to_reserve']:
            raise ValueError(
                ('Дата начала бронирования должна быть раньше'
                 'даты окончания бронирования!')
            )
        return values


class ReservatioCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int

    class Config:
        orm_mode = True
