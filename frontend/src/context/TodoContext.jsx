import { createContext, useContext, useEffect, useState } from "react";
import { toast } from "react-toastify";
import { UserContext } from "./UserContext";

export const TodoContext = createContext();

export const TodoProvider = ({ children }) => 
  {
    const {authToken} = useContext(UserContext)
    
    const [tags, setTags] = useState([])
    const [todos, setTodos] = useState([])

    // ================================ TAGS =====================================
   useEffect(()=>{
        fetch('http://127.0.0.1:5000/tags',{
                method:"GET",
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then((response) => response.json())
            .then((response) => {
            setTags(response)
            });
   }, [])
   


    // ================================ TODOS ====================================

    // Fetch Todos
    useEffect(()=>{
        fetch('http://127.0.0.1:5000/todos',{
                method:"GET",
                headers: {
                    'Content-type': 'application/json',
                      Authorization: `Bearer ${authToken}`
                }
            })
            .then((response) => response.json())
            .then((response) => {
                setTodos(response)
            });
   }, [])

    // Add Todo
    const addTodo = ( title, description, deadline, tag_id ) => 
    {
       
                toast.loading("Adding todo ... ")
                fetch("http://127.0.0.1:5000/todo/add",{
                    method:"POST",
                    headers: {
                        'Content-type': 'application/json',
                        Authorization: `Bearer ${authToken}`

                      },
                    body: JSON.stringify({
                        title, description, deadline, tag_id
                    })
                })
                .then((resp)=>resp.json())
                .then((response)=>{
                    console.log(response);
                    
                    if(response.success){
                        toast.dismiss()
                        toast.success(response.success)
                    }
                    else if(response.error){
                        toast.dismiss()
                        toast.error(response.error)
        
                    }
                    else{
                        toast.dismiss()
                        toast.error("Failed to add")
        
                    }
                  
                    
                })
    }

    const getTodos = () => 
    {
        console.log("Fetching all todos");
    }

    const getTodoById = () => 
    {
        console.log("Fetching todo by ID");
    }

    const updateTodo = () => 
    {
        console.log("Updating todo");
    }

    const deleteTodo = () => 
    {
        console.log("Deleting todo:");
    }



    
  const data = {
    todos,
    tags,

    addTodo,
    getTodos,
    getTodoById,
    updateTodo,
    deleteTodo,
  }

  return (
  <TodoContext.Provider value={data}>
      {children}
  </TodoContext.Provider>)
}
