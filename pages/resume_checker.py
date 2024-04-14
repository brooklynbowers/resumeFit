
    return response.choices[0].message.content


# Cell 4: Function to generate the image
def generate_image(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Assuming the API returns an image URL; adjust based on actual response structure
    return response.data[0].url

# Cell 4: Streamlit UI 
user_input = st.text_area("Enter a brief for your post:", "How should you maintain a deployed model?")

if st.button('Generate Post Content'):
    with st.spinner('Generating Text...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

    with st.spinner('Generating Thumbnail...'):
        thumbnail_url = generate_image(user_input)  # Consider adjusting the prompt for image generation if needed
        st.image(thumbnail_url, caption='Generated Thumbnail')
