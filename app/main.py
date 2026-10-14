from pathlib import Path
from html import escape

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.gemini_utils import (
    generate_home_recommendations,
    generate_party_recommendations,
    generate_jewelry_recommendations
)


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="PocketSmart AI",
    description="Your Smart Budget & Recommendation Assistant",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# ---------------- HOME PAGE ----------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


# ---------------- HOME PLANNER PAGE ----------------

@app.get("/home-planner", response_class=HTMLResponse)
async def home_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home_planner.html",
        context={"request": request}
    )


# ---------------- HOME PLANNER AI ----------------

@app.post("/generate-home", response_class=HTMLResponse)
async def generate_home(
    request: Request,
    budget: int = Form(...),
    room: str = Form(...),
    items: str = Form(...),
    style: str = Form(...)
):

    recommendations = generate_home_recommendations(
        budget=budget,
        room=room,
        items=items,
        style=style
    )

    safe_recommendations = escape(recommendations)

    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PocketSmart AI Recommendations</title>

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f7f4ee;
                    color: #222;
                    margin: 0;
                    padding: 50px 20px;
                }}

                .container {{
                    max-width: 900px;
                    margin: auto;
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
                }}

                h1 {{
                    margin-bottom: 10px;
                }}

                .subtitle {{
                    color: #666;
                    margin-bottom: 30px;
                }}

                .recommendations {{
                    white-space: pre-wrap;
                    line-height: 1.7;
                    background: #f8f8f8;
                    padding: 25px;
                    border-radius: 12px;
                }}

                a {{
                    display: inline-block;
                    margin-top: 25px;
                    padding: 12px 20px;
                    background: #222;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                }}

                a:hover {{
                    background: #b8860b;
                }}
            </style>
        </head>

        <body>

            <div class="container">

                <h1>✨ Your PocketSmart AI Plan</h1>

                <p class="subtitle">
                    Personalized recommendations for your {escape(room)}
                    within a budget of ₹{budget}.
                </p>

                <div class="recommendations">
                    {safe_recommendations}
                </div>

                <a href="/home-planner">
                    ← Plan Again
                </a>

            </div>

        </body>
        </html>
        """
    )
# ---------------- PARTY PLANNER PAGE ----------------

@app.get("/party-planner", response_class=HTMLResponse)
async def party_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="party_planner.html",
        context={"request": request}
    )
# ---------------- PARTY PLANNER AI ----------------

@app.post("/generate-party", response_class=HTMLResponse)
async def generate_party(
    request: Request,
    budget: int = Form(...),
    guests: int = Form(...),
    event: str = Form(...),
    venue: str = Form(...),
    requirements: str = Form(...)
):

    recommendations = generate_party_recommendations(
        budget=budget,
        guests=guests,
        event=event,
        venue=venue,
        requirements=requirements
    )

    safe_recommendations = escape(recommendations)

    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Party Planner | PocketSmart AI</title>

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f7f4ee;
                    color: #222;
                    margin: 0;
                    padding: 50px 20px;
                }}

                .container {{
                    max-width: 900px;
                    margin: auto;
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
                }}

                .recommendations {{
                    white-space: pre-wrap;
                    line-height: 1.7;
                    background: #f8f8f8;
                    padding: 25px;
                    border-radius: 12px;
                }}

                a {{
                    display: inline-block;
                    margin-top: 25px;
                    padding: 12px 20px;
                    background: #222;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                }}
            </style>
        </head>

        <body>

            <div class="container">

                <h1>🎉 Your PocketSmart AI Party Plan</h1>

                <p>
                    Personalized recommendations for
                    {guests} guests within a budget of ₹{budget}.
                </p>

                <div class="recommendations">
                    {safe_recommendations}
                </div>

                <a href="/party-planner">
                    ← Plan Again
                </a>

            </div>

        </body>
        </html>
        """
    )
# ---------------- JEWELRY PLANNER PAGE ----------------

@app.get("/jewelry-planner", response_class=HTMLResponse)
async def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={"request": request}
    )


# ---------------- JEWELRY PLANNER AI ----------------

@app.post("/generate-jewelry", response_class=HTMLResponse)
async def generate_jewelry(
    request: Request,
    budget: int = Form(...),
    occasion: str = Form(...),
    style: str = Form(...),
    requirements: str = Form(...)
):

    recommendations = generate_jewelry_recommendations(
        budget=budget,
        occasion=occasion,
        style=style,
        requirements=requirements
    )

    safe_recommendations = escape(recommendations)

    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Jewelry Planner | PocketSmart AI</title>

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f7f4ee;
                    color: #222;
                    margin: 0;
                    padding: 50px 20px;
                }}

                .container {{
                    max-width: 900px;
                    margin: auto;
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
                }}

                .recommendations {{
                    white-space: pre-wrap;
                    line-height: 1.7;
                    background: #f8f8f8;
                    padding: 25px;
                    border-radius: 12px;
                }}

                a {{
                    display: inline-block;
                    margin-top: 25px;
                    padding: 12px 20px;
                    background: #222;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                }}
            </style>
        </head>

        <body>

            <div class="container">

                <h1>💎 Your PocketSmart AI Jewelry Plan</h1>

                <p>
                    Personalized recommendations for your
                    {escape(occasion)} within a budget of ₹{budget}.
                </p>

                <div class="recommendations">
                    {safe_recommendations}
                </div>

                <a href="/jewelry-planner">
                    ← Plan Again
                </a>

            </div>

        </body>
        </html>
        """
    )