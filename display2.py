import streamlit as st

import physics
import graph2
import statement2
import laws2


def main():
    st.title("Physics App")
    st.write(
        "Welcome to the Physics App! This app provides various tools and simulations for learning physics concepts.")

    st.header("Ideal gas And Real gas")
    selected_topic = st.selectbox("Choose a topic", ["statement", "cal", "laws", "graph"])

    if selected_topic == "statement":
        statement2.main()
    elif selected_topic == "cal":
        physics.main()
    elif selected_topic == "laws":
        laws2.main()
    elif selected_topic == "graph":
        graph2.main()


if __name__ == "__main__":
    main()
