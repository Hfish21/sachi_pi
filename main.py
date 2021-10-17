from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/wifi/login")
def read_details(ssid : str, password: str):
    return "username {0}     password: {1}".format(ssid, password)
