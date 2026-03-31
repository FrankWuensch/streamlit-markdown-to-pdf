import streamlit as st

st.set_page_config(layout="wide")
st.title("Markdown to PDF converter")
st.header("Full control about PDF output with custom css file")

# Placeholder for dynamic CSS
css_placeholder = st.empty()

# Load default CSS
with open("src/output.css", "r", encoding="utf-8") as f:
    default_css = f.read()

css_content = default_css  # Start with default

uploaded_file = st.file_uploader("Upload markdown file", type=["md"])

if uploaded_file:
    custom_css = st.file_uploader("Upload custom css file", type="css")
    markdown_content = uploaded_file.getvalue().decode("utf-8")

    # Update CSS if custom uploaded
    if custom_css:
        css_content = custom_css.getvalue().decode("utf-8")

    # Apply only the current CSS
    with css_placeholder:
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    st.markdown(markdown_content)
