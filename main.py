import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
import time
import cart as car
st.set_page_config(page_title="CosMos - Equation Plotter", page_icon="✨", layout="wide")
if "show_splash" not in st.session_state:
    st.session_state.show_splash = True
if st.session_state.show_splash:
    st.markdown("""
        <style>
            .splash {
                text-align: center;
                font-size: 60px;
                font-weight: bold;
                color: #4CAF50;
                margin-top: 200px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='splash'> CosMos </div>", unsafe_allow_html=True)


    time.sleep(1)
    st.session_state.show_splash = False
    # st.experimental_rerun()







st.set_page_config(
    page_title="CosMos - Equation Plotter",
    page_icon="✨",
    layout="wide"
)

st.markdown(""" 
    <style>
        /* Center title */
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
        }
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f0f2f6;
        }
        /* Buttons */
        .stButton>button {
            background-color: #4CAF50;
            color: Blue;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-weight: bold;
        }
        /* Input fields */
        .stTextInput>div>input {
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)
st.sidebar.header("🔧 Controls")
st.sidebar.write("Manage your files and settings here.")

# File saving placeholder
file_name = st.sidebar.text_input("Save file as:", "my_plot")
st.sidebar.button("💾 Save Plot")

# Login/Signup placeholder
acco = st.sidebar.selectbox("Manage Account",["🏠 Home","👤 Account", " 🫆 Privacy Policy"," ✳️ About"])

# --- Main Interface ---
if acco == "🏠 Home":
  col1, col2 = st.columns([1, 2.5])
  x,y = sp.symbols("x y")
    
  with col1:
    st.write("Your own DESMOS ")
    x = st.selectbox("Choose type Eqation", ["Implicit Equation", "Cartesian Equation", "Polar"])
    if x == "Implicit Equation":
     st.subheader("➕ Add Equation")
     equation = st.text_input("Enter equation (e.g., Ax + By + c = 0)")
     button = st.button("Plot")
     if button:
      if equation:
        try:

            with col2:
             fig = car.plot_implicit(equation,-100,100,-100,100,2000)
             st.plotly_chart(fig)
            #  st.pyplot(fig)
        except Exception as e:

           st.error(f"Could not parse or plot equation: {e}")
           st.empty()
    if x == "Cartesian Equation":
     st.subheader("➕ Add Equation")
     equation = st.text_input("Enter equation (e.g., y = x^2)")
     button = st.button("Plot")
     if button:
      if equation:
        try:
            with col2:
              fig = car.plot_cartesian(equation,-50,50,2000)
              st.plotly_chart(fig)
            #   st.pyplot(fig)
        except Exception as e:

           st.error(f"Could not parse or plot equation: {e}")
           st.empty()
    if x == "Polar":
     st.subheader("➕ Add Equation")
     equation = st.text_input("Enter equation (e.g., r = e^x + y)")
     button = st.button("Plot")
     if button:
      if equation:
        try:
            with col2:
              fig = car.plot_polar(equation,0,12*np.pi,2000)
              st.plotly_chart(fig)
            #   st.pyplot(fig)
        except Exception as e:

           st.error(f"Could not parse or plot equation: {e}")
           st.empty()
















































elif acco == "👤 Account":
   st.title("Manage your account")
   login_option = st.radio("Choose:", ["Login", "Signup"])
   if login_option == "Login":
    st.subheader("Login your account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
   elif  login_option == "Signup":
    st.subheader("Create a new account")
    username = st.text_input("Name: ")
    dob = st.date_input("Select your Date of Birth")
    Email = st.text_input("Email")
    password = st.text_input("Password", type="password")
   st.button("Submit")
elif acco == " 🫆 Privacy Policy":
    st.title("Privacy policy")
    st.subheader("Regarding copyright")
    st.write("There is no privacy, because privacy is a myth, But dont worry and keep that in mind that evrything is stored somewhere and you dont know where that is but you dont need to worry about that. Since this is just a project website so we are not giving guarentee to the privacy etc but belive us your all the data will remaain intact. We hope you guys will love it and if you ever want us to give the suggestions then please because your one suggestion will be extreamly valuable for us. We hope you will love it and if you do then please do not forgot to give the suggestions so we can build more better, more beautifull and more good.")
    st.write("There is no privacy, because privacy is a myth, But dont worry and keep that in mind that evrything is stored somewhere and you dont know where that is but you dont need to worry about that. Since this is just a project website so we are not giving guarentee to the privacy etc but belive us your all the data will remaain intact. We hope you guys will love it and if you ever want us to give the suggestions then please because your one suggestion will be extreamly valuable for us. We hope you will love it and if you do then please do not forgot to give the suggestions so we can build more better, more beautifull and more good.")
elif acco == " ✳️ About":
    st.title("About CosMos")
    st.subheader("CosMos Eqation Plotter")
    st.write("There is no privacy, because privacy is a myth, But dont worry and keep that in mind that evrything is stored somewhere and you dont know where that is but you dont need to worry about that. Since this is just a project website so we are not giving guarentee to the privacy etc but belive us your all the data will remaain intact. We hope you guys will love it and if you ever want us to give the suggestions then please because your one suggestion will be extreamly valuable for us. We hope you will love it and if you do then please do not forgot to give the suggestions so we can build more better, more beautifull and more good.")
    st.write("There is no privacy, because privacy is a myth, But dont worry and keep that in mind that evrything is stored somewhere and you dont know where that is but you dont need to worry about that. Since this is just a project website so we are not giving guarentee to the privacy etc but belive us your all the data will remaain intact. We hope you guys will love it and if you ever want us to give the suggestions then please because your one suggestion will be extreamly valuable for us. We hope you will love it and if you do then please do not forgot to give the suggestions so we can build more better, more beautifull and more good.")
# --- Footer ---
st.markdown("---")
st.markdown("In developing phase...... NITIN CosMos project")








