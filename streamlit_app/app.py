import streamlit as st

st.set_page_config(layout="wide")
st.title("Markdown to PDF converter")
st.header("Full control about PDF output with custom css file")

# Load default CSS (applies globally)
with open("src/output.css", "r", encoding="utf-8") as f:
    default_css = f.read()
st.markdown(f"<style>{default_css}</style>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload markdown file", type=["md"])
st.divider()

if uploaded_file:
    custom_css = st.file_uploader("Upload custom css file", type="css")
    markdown_content = uploaded_file.getvalue().decode("utf-8")

    # Use a container with key to isolate custom CSS
    with st.container(key="custom_content"):
        # Apply custom CSS only to this container
        css_to_apply = custom_css.getvalue().decode("utf-8") if custom_css else default_css
        st.markdown(f"<style>.st-key-custom_content {{{css_to_apply}}}</style>", unsafe_allow_html=True)
        st.markdown(markdown_content)
