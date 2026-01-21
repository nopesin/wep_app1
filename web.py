import streamlit as st
import function

todos = function.get_todo()

def add_todo():
    todo_local = st.session_state['new_todo'] +'\n'
    todos.append(todo_local)
    function.write_todo(todos)

st.title('My TO-DO APP')
st.subheader('This is my todo app')
st.write('this is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox :
        todos.pop(index)
        function.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a Todo :",placeholder="Add a new todo",on_change=add_todo,key='new_todo')

print(todos)

st.session_state