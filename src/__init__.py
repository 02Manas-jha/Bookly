from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from .errors import register_error_handlers
from .middleware import register_middleware
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting ... ")
    await init_db()
    yield
    print(f"server has been stopped")

version = 'v1'

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix ="/api/{version}"

app = FastAPI(
    title='Bookly',
    description=description,
    version=version,
    contact={
        "name": "Manas Jha",
        "url": "https://github.com/02Manas-jha",
        "email": "manasjha0203@gmail.com",
    },
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)


register_error_handlers(app)
register_middleware(app)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router,prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router,prefix=f"/api/{version}/reviews", tags=['reviews'])
app.include_router(tags_router, prefix=f"/api/{version}/tags", tags=['tags'])