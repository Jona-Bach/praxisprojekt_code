import streamlit as st

#__________________________SIDEBAR____________________________
st.sidebar.subheader("Welcome to FinSight!")
st.sidebar.image("./assets/finsightbar.png")
st.sidebar.divider()
#____________________________________________________________


#__________________________PAGE____________________________
tab1, tab2, tab3 = st.tabs(["Welcome", "Setup", "Settings"])
st.title("")


with tab1:
    st.image("./assets/logofinsightold.png")




#____________________________________________________________

