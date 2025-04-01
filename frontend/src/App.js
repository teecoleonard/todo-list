import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:8000/todos';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [newDescription, setNewDescription] = useState('');
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    axios.get(API_URL)
      .then(response => {
        setTodos(response.data);
      })
      .catch(error => {
        console.error('Error fetching todos:', error);
      });
  }, []);

  const addTodo = () => {
    axios.post(API_URL, { title: newTodo, description: newDescription, completed: false })
      .then(response => {
        setTodos([...todos, response.data]);
        setNewTodo('');
        setNewDescription('');
        setShowForm(false);
      })
      .catch(error => {
        console.error('Error adding todo:', error);
      });
  };

  const deleteTodo = (id) => {
    axios.delete(`${API_URL}/${id}`)
      .then(() => {
        setTodos(todos.filter(todo => todo.id !== id));
      })
      .catch(error => {
        console.error('Error deleting todo:', error);
      });
  };

  const toggleTodo = (id) => {
    const todo = todos.find(todo => todo.id === id);
    axios.put(`${API_URL}/${id}`, { completed: !todo.completed })
      .then(response => {
        setTodos(todos.map(todo => (todo.id === id ? response.data : todo)));
      })
      .catch(error => {
        console.error('Error toggling todo:', error);
      });
  };

  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
  };

  return (
    <div className="todo-container">
      <h1 className="todo-title">To-do Lista</h1>
      
      {!showForm ? (
        <button 
          className="todo-button new-todo-button" 
          onClick={() => setShowForm(true)}
        >
          Novo To-do
        </button>
      ) : (
        <div className="todo-form">
          <div className="form-fields">
            <input
              type="text"
              className="todo-input"
              value={newTodo}
              onChange={(e) => setNewTodo(e.target.value)}
              placeholder="Título"
            />
            <textarea
              className="todo-textarea"
              value={newDescription}
              onChange={(e) => setNewDescription(e.target.value)}
              placeholder="Descrição (opcional)"
            />
          </div>
          <div className="form-actions">
            <button className="todo-button cancel-button" onClick={() => setShowForm(false)}>
              Cancelar
            </button>
            <button 
              className="todo-button" 
              onClick={addTodo} 
              disabled={!newTodo}
            >
              Adicionar
            </button>
          </div>
        </div>
      )}
      
      <ul className="todo-list">
        {todos.length === 0 ? (
          <p className="empty-list">Nenhuma tarefa encontrada. Adicione uma nova!</p>
        ) : (
          todos.map(todo => (
            <li key={todo.id} className={`todo-item ${todo.completed ? 'completed' : ''}`}>
              <div className="todo-content">
                <input
                  type="checkbox"
                  className="todo-checkbox"
                  checked={todo.completed}
                  onChange={() => toggleTodo(todo.id)}
                />
                <div className="todo-text-container">
                  <span className="todo-text">{todo.title}</span>
                  {todo.description && (
                    <span className="todo-description">{todo.description}</span>
                  )}
                  <span className="todo-date">
                    Criado em: {formatDate(todo.created_at)}
                  </span>
                </div>
              </div>
              <button className="todo-delete" onClick={() => deleteTodo(todo.id)}>🗑️</button>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;