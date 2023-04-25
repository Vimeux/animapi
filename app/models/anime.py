from typing import List
from pydantic import BaseModel
from app.models.episode import EpisodeModel

class AnimeModel(BaseModel):
    anime_id: int
    title: str
    title_english: str
    title_romanji: str
    title_french: str = None
    others: str
    type: str
    status: str
    popularity: float
    url: str
    genres: List[str]
    url_image: str
    score: float
    start_date_year: str
    nb_eps: str
    synopsis: str
    trailer_url: str
    banner_url: str
    episodes: List[EpisodeModel]