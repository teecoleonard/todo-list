from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoResponse
from datetime import datetime

def get_todos(db: Session):
    todos = db.query(Todo).all()
    if not todos:
        return []  # Retorna uma lista vazia caso não haja dados
    return todos

def create_todo(db: Session, todo: TodoCreate):
    try:
        # Create a dictionary from the todo model and add timestamps
        todo_data = todo.dict()
        todo_data["created_at"] = datetime.now()
        todo_data["updated_at"] = datetime.now()
        
        db_todo = Todo(**todo_data)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as e:
        db.rollback()  # Garante que a transação seja revertida em caso de erro
        raise e  # Re-raise exception para ser tratada em outro nível (como o FastAPI)

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False

def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        # Update only the fields that are provided in the update object
        update_data = todo_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            if value is not None:  # Only update if value is not None
                setattr(db_todo, key, value)
        
        # Always update the updated_at timestamp
        db_todo.updated_at = datetime.now()
        db.commit()
        db.refresh(db_todo)
        return db_todo
    return None  # Retorna None se o todo não for encontrado
