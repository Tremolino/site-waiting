from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI(
    docs_url=None,
    openapi_url=None,
)



app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/fonts", StaticFiles(directory="./fonts"), name="fonts")
templates = Jinja2Templates(directory="./templates")

@app.get("/")
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_email(email: str = Form(...)):
    with open("emails.txt", "a") as file:
        file.write(email + "\n")
    return RedirectResponse("/", status_code=303)