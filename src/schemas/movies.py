import datetime
from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional


class MovieBase(BaseModel):
    name: str
    date: datetime.date
    score: float = Field(ge=0, le=100)
    overview: str
    status: str
    budget: float = Field(ge=0)
    revenue: float = Field(ge=0)

    @field_validator("date")
    def validate_date(self, v: date):
        if v > datetime.date.today() + datetime.timedelta(days=365):
            raise ValueError("Movie date cannot be more than 1 year in the future")
        return v


class CountrySchema(BaseModel):
    id: int
    code: str
    name: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class GenreSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ActorSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class LanguageSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class MovieCreateDetailSchema(MovieBase):
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]


class MovieDetailSchema(MovieBase):
    country: CountrySchema
    genres: list[GenreSchema]
    actors: list[ActorSchema]
    languages: list[LanguageSchema]

    model_config = ConfigDict(from_attributes=True)


class MovieUpdateRequest(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime.date] = None
    score: Optional[float] = Field(None, ge=0, le=100)
    overview: Optional[str] = None
    status: Optional[str] = None
    budget: Optional[float] = Field(None, ge=0)
    revenue: Optional[float] = Field(None, ge=0)


class MovieListItemSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str


class MovieItemSchema(MovieDetailSchema):
    id: int


class MovieListResponseSchema(BaseModel):
    movies: List[MovieListItemSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int
