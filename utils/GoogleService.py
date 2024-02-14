import asyncio
import gspread
import datetime
from dataclasses import dataclass


class GoogleService:
    def __init__(self) -> None:
        self.gc = gspread.service_account("google_credentials.json")
        # self.sh = self.gc.open("test+smart")
        self.sh = self.gc.open_by_url(
            "https://docs.google.com/spreadsheets/d/1lleHcwZf8t-RReaoEn2-u0m5-fu0-1YqpJ98tycMM3k/edit#gid=0")

    async def save_lead(self, lead):
        ws = self.sh.get_worksheet(0)
        print(lead)
        ws.append_row(lead)


@dataclass
class Lead:
    goal: str = None
    work_with: str = None
    Education_important: str = None
    work_specific: str = "-"
    personal_improvements_goals: str = None
    budget: str = None
    start_education: str = None
    name: str = None
    phone: str = None
    email: str = None
    date: str = str(datetime.datetime.strftime(
        datetime.datetime.now(), "%d-%m-%Y, %H:%M:%S"))

    def as_tuple(self):
        return [
            self.goal,
            self.work_with,
            self.Education_important,
            self.work_specific,
            self.personal_improvements_goals,
            self.budget,
            self.start_education,
            self.name,
            self.phone,
            self.email,
            self.date,
        ]


if __name__ == "__main__":

    lead = Lead(goal="личное развитие",
                work_with="взрослые",
                Education_important='практика',
                personal_improvements_goals="самопознание",
                budget="4000",
                start_education="month",
                name="Никита",
                phone="89999999999",
                email="test@test.com")

    gs = GoogleService()
    asyncio.run(gs.save_lead(lead.as_tuple()))
