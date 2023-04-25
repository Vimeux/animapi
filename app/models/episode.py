from pydantic import BaseModel

class EpisodeModel(BaseModel):
    time: str
    episode_number: int
    title: str
    url: str
    url_image: str