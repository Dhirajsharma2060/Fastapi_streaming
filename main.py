import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx
from datetime import UTC, datetime

from supabase import create_client

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templetes = Jinja2Templates(directory="templates")

templetes.env.globals.update(now=lambda: datetime.now(UTC))


#Initialize the supabase client
SUPABASE_URL =os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY =os.getenv("SUPABASE_ANON_KEY")
SUPABASE_BUCKET =os.getenv("SUPABASE_BUCKET")

# SUPABASE_BUCKET=create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
@app.get("/")
async def root():
    return {"message": "Hello World"}