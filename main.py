from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Programming",
        "author": "1", },
    {
        "id": 2,
        "title": "Python Programming1",
        "author": "2", },
]

class BookSchema(BaseModel):
    title: str
    author: str

@app.get("/books",
         tags=["books"],
         summary='get all books',
         description="<h1>Get all books</h1>")
def get_books():
    return books

@app.post("/books", tags=["books"])
def add_book(book: BookSchema):
    new_book_id = len(books) + 1
    books.append({
        "id": new_book_id,
        "title": book.title,
        "author": book.author,
    })
    return {"success": True, "message": "book added"}