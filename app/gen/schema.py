from pydantic import BaseModel

class UserModel(BaseModel):
    user_name: str
    password: str

# class GenZModel(BaseModel):
#     _id: int
#     date: str
#     category: str
#     sentence: str
#     sentence_short: str
#     sentence_keywords: str
#     sentence_sentiment: str
#     sentence_sentiment_net: float
#     sentence_sent_score: float
#     sentence_sentiment_label: int
#     sentence_entities: str
#     sentence_non_entities: str


# class YoungPeopleModel(BaseModel):
#     _id: int
#     date: str
#     logits: float
#     net_sent: float
#     logits_mean: float
#     net_sent_mean: float
#     MA_logits: float
#     MA_net_sent: float
#     MA_net_sent_ema_alpha_0: object


# class DataModel(BaseModel):
#     genZ: GenZModel
#     young_people: YoungPeopleModel
