import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"   #place the input_text string to the local variable - todo, the session state works similarly to input("")_ but in gui
    todos.append(todo)
    functions.write_todos(todos)

    print(todo)


st.title("My Todo App")
st.subheader("This is a my todo app.")
st.write("This app is increase your productivity.")


for index, todo in enumerate(todos):              #open the file, and bring each items in the txt out to the window
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)                    #if checkbox has been checked, delete it
        functions.write_todos(todos) #write it into the todos list
        del st.session_state[todo]  #delete
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo' )    #on_change = add_todo is refer to the function add_todo above


