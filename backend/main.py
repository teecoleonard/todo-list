from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from schemas import TodoCreate, TodoUpdate, TodoResponse
from crud import get_todos, create_todo, delete_todo, update_todo
from models import Todo  # Certifique-se de ter a classe `Todo` importada do seu modelo

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route para pegar todos os todos
@app.get("/todos", response_model=list[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    todos = get_todos(db)
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found")
    return todos

# Route para adicionar um novo todo
@app.post("/todos", response_model=TodoResponse)
def add_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)

# Route para deletar um todo
@app.delete("/todos/{todo_id}", response_model=bool)
def remove_todo(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(db, todo_id)

# Route para marcar o todo como completado ou não
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def toggle_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(db, todo_id, todo)
