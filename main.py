from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


# Static folder
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Templates
templates = Jinja2Templates(
    directory="templates"
)


# Home
@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "active_page": "home"
        }
    )


# About
@app.get("/about")
async def about(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={
            "request": request,
            "active_page": "about"
        }
    )


# Services
@app.get("/services")
async def services(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="services.html",
        context={
            "request": request,
            "active_page": "services"
        }
    )


# Contact
@app.get("/contact")
async def contact(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={
            "request": request,
            "active_page": "contact"
        }
    )


# Health check
@app.get("/health")
async def health():

    return {
        "status": "running"
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )