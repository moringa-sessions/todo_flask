import React, { useContext } from 'react'
import { TodoContext } from '../context/TodoContext'


export default function Home() {

  const {todos} = useContext(TodoContext)
  return (
    <div>
      {
        todos && todos.map((todo)=>(
           <div key={todo.id}>
              <h1>{todo.title}</h1>
              <p>{todo.deadline}</p>
           </div>
        ))
      }
    </div>
  )
}
