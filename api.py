from fastapi import FastAPI, Path
from fastapi.responses import Response
import requests

app = FastAPI()


@app.get("//day-{day}.md")
def get_day_readme(
    day: int = Path(
        None, description="The README of the day you want to view.", gt=0, le=100
    )
):
    if day not in range(1, 101):
        return Response(
            content="Hey, this page isn't loading correctly!",
            media_type="text/markdown",
        )
    readme_data = requests.get(
        f"https://raw.githubusercontent.com/rzmk/100-days-of-code/main/projects/Day%20{day}/README.md"
    )
    if readme_data.text == "404: Not Found":
        return Response(
            content="Hey! This day isn't loading or doesn't have a README yet.",
            media_type="text/markdown",
        )
    return Response(content=readme_data.text, media_type="text/markdown")
