
#st.title("rehan:sunglasses:,:smile:")
#st.write("content about Rehan",7)
#st.markdown('# Login Page')
#st.text(' Enter Your Name:')
#st.success("successfull login")
#st.write('range 10')
#st.checkbox('')
#status = st.checkbox('click here')



import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Streamlit Arithmetic Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Functions
def add(value):
    st.session_state.expression += str(value)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"

# Text input with keyboard support
st.text_input(
    "Enter Expression:",
    key="expression",
    on_change=calculate   # ENTER press kare to calculate ho
)

# Layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add, args=("7",))
    st.button("4", on_click=add, args=("4",))
    st.button("1", on_click=add, args=("1",))
    st.button("C", on_click=clear)

with col2:
    st.button("8", on_click=add, args=("8",))
    st.button("5", on_click=add, args=("5",))
    st.button("2", on_click=add, args=("2",))
    st.button("0", on_click=add, args=("0",))

with col3:
    st.button("9", on_click=add, args=("9",))
    st.button("6", on_click=add, args=("6",))
    st.button("3", on_click=add, args=("3",))
    st.button(".", on_click=add, args=(".",))

with col4:
    st.button("/", on_click=add, args=("/",))
    st.button("*", on_click=add, args=("*",))
    st.button("-", on_click=add, args=("-",))
    st.button("+", on_click=add, args=("+",))

st.button("=", on_click=calculate)