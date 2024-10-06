import streamlit as st
import requests
import datetime
import json
import uuid

def get_confessions():
    url = "https://confessionbe.onrender.com/retrieve_data"  # Replace with your actual endpoint URL

    response = requests.get(url)
    confessions = []

    if response.status_code == 200:
        print("Request successful!")
        confessions = response.json()
    else:
        print("Request failed with status code:", response.status_code)

    reversed_list = []
    for item in confessions[::-1]:
        reversed_list.append(item)

    return reversed_list


def submit_confession(content):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"time": current_time, "content": content}

    url = "https://confessionbe.onrender.com/receive_data"  # Replace with your actual endpoint URL
    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.success("Confession submitted successfully!")
    else:
        st.error(f"Error submitting confession: {response.status_code}")


def submit_comment(confession_id, comment_text):

    url = f"https://confessionbe.onrender.com/add_comment/{confession_id}"  # Replace with actual URL
    data = {"data": comment_text}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.success("Comment added successfully!")
        st.success("please refresh the page")
    else:
        st.error(f"Error adding comment: {response.status_code}")


def main():
    st.title("Welcome to Confessions")

    # Create tabs for submission and feed
    tabs = st.tabs(["Submit Confession", "Confessions Feed"])

    with tabs[0]:
        st.header("Submit Your Confession")
        st.markdown(
            "These confessions are highly anonymous and completely uncensored and unfiltered. You can confess anything."
        )
        confession_text = st.text_area("Enter your confession here 👇🏻:")

        if st.button("Submit"):
            submit_confession(confession_text)


        st.success("New update! We've addressed some bugs and made minor improvements. Thank you for your valuable feedback.")

    with tabs[1]:
        st.header("Confessions Feed")
        st.markdown("______________")

        confessions = get_confessions()

        comment_states = {}  

        comment_button_counter = 0

        for confession in confessions:
            st.markdown(f"{confession['content']}")
            st.markdown(f"Submitted at: {confession['time']}")

            
            with st.expander("See Comments"):
                if "comments" in confession:
                    for comment in confession["comments"]:
                        st.write(f"- {comment}")

                else:
                    st.write("No comments yet 🙁")

                
                comment_text_key = f"comment_text_{comment_button_counter}"
                comment_button_key = f"comment_button_{comment_button_counter}"
                comment_button_counter += 1

                comment_text = st.text_area("comment here:", key=comment_text_key)
                comment_states[comment_button_key] = False  

                if st.button("Add Comment", key=comment_button_key):
                    comment_states[comment_button_key] = True  
                    submit_comment(confession["id"], st.session_state[comment_text_key])


            st.markdown("__________________________________________")
            st.markdown("\n")  


if __name__ == "__main__":
    main()