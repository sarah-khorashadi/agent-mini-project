from pydantic import BaseModel, Field
from typing import Literal

class Classification(BaseModel):
    intent: Literal["vip_question", "exchange_registration", "kol_collabration", "support_request", "general_info", "Unkonown"]
    segment: Literal["new_user", "vip_interest", "exchange_signup", "kol_condidate, suppor_needed, general_question"]