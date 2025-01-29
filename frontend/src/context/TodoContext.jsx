import { createContext, useContext, useEffect, useState } from "react";
import { toast } from "react-toastify";
import { UserContext } from "./UserContext";
import { useNavigate } from "react-router-dom";

export const TodoContext = createContext();

export const TodoProvider = ({ children }) => 
  {
    const navigate = useNavigate()
    const {authToken} = useContext(UserContext)
    
    const [tags, setTags] = useState([])
    const [todos, setTodos] = useState([])

    const [onChange, setOnchange] = useState(true)

    // ================================ TAGS =====================================
   useEffect(()=>{
        fetch('https://todo-flask-65o6.onrender.com/tags',{
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
        fetch('https://todo-flask-65o6.onrender.com/todos',{
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
   }, [onChange])


    // Add Todo
    const addTodo = ( title, description, deadline, tag_id ) => 
    {
       
                toast.loading("Adding todo ... ")
                fetch("https://todo-flask-65o6.onrender.com/todo/add",{
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
                        setOnchange(!onChange)
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



    const updateTodo = () => 
    {
        console.log("Updating todo");
    }

    const deleteTodo = (id) => 
    {
        toast.loading("Deleting todo ... ")
        fetch(`https://todo-flask-65o6.onrender.com/todo/${id}`,{
            method:"DELETE",
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${authToken}`

              }
        })
        .then((resp)=>resp.json())
        .then((response)=>{
            
            if(response.success){
                toast.dismiss()
                toast.success(response.success)
                setOnchange(!onChange)
                navigate("/")

            }
            else if(response.error){
                toast.dismiss()
                toast.error(response.error)

            }
            else{
                toast.dismiss()
                toast.error("Failed to delete")

            }
          
            
        })
    }



    
  const data = {
    todos,
    tags,

    addTodo,
    updateTodo,
    deleteTodo,
  }

  return (
  <TodoContext.Provider value={data}>
      {children}
  </TodoContext.Provider>)
}
