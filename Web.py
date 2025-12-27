import streamlit as st
import Functions



def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)

todos = Functions.get_todos()
st.title("My Todo App")
st.subheader("This is my Todo List")
st.write("I will try to finish my list consistently")

st.checkbox("Love myself")
st.checkbox("Celebrate my wins")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun(scope="app")


st.text_input(label="What do you want to work on?",
              placeholder="Add a todo", on_change=add_todo,
              key="new_todo")

st.session_state
