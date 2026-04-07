import streamlit as st
from modules.prompts import marketing_prompt
from modules.generator import generate_campaing

st.title("🚀 AI Marketing Automation")

product = st.text_input("Prouct Name")
category = st.text_input("Category")
features = st.text_area("Features")

result = None
if st.button("Generate Full Campaign"):
    
    # Returns full marketing info(description, etc) for a campaign
    prompt = marketing_prompt(product, category, features)

    with st.spinner(text="Generating full campaign..."):
        result = generate_campaing(prompt=prompt)
        st.markdown("## 📊 Campaign Output")
        st.write(result)

if st.button("Save Campaign") and result:
    with open("campaign.txt", "w") as f:
        f.write(result)

st.markdown("### 🛍 Product Description")
st.write("section_1")

st.markdown("### 📢 Ads")
st.write("section_2")

st.markdown("### 📧 Email")
st.write("section_3")

