import streamlit as st
import ingredients
import disease
import diet
import packed
import home

# Move this line to the top, outside of any function
st.set_page_config(page_title="Food Safety & Health Analyzer", page_icon="🍽️")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "Ingredient Analysis", "Disease Prediction", "Diet Recommendation", "Packed Food Analysis"])

    if page == "Ingredient Analysis":
        st.title("🧪 Ingredient Analysis")
        ingredients.main()
    elif page == "Home":
        st.title("NutriScan-AI")
        home.main()
    elif page == "Disease Prediction":
        st.title("🩺 Disease Prediction")
        disease.main()
    elif page == "Packed Food Analysis":
        st.title("🔎 Packed Food Analysis")
        packed.main()
    elif page == "Home":
        st.title("🍽️ Food Image Classifier and Health Analyzer")
        home.main()
    else:
        st.title("🍽️ AI-Powered Personalized Diet Recommender")
        diet.main()

if __name__ == "__main__":
    main()
