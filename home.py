import streamlit as st
import requests
import datetime
import json


def reverse_list(lst):
  """Reverses a given list and returns a new reversed list.

  Args:
    lst: The list to be reversed.

  Returns:
    A new list that is the reversed version of the input list.
  """

  reversed_list = []
  for item in lst[::-1]:
    reversed_list.append(item)
  return reversed_list

def get_confessions():
    # Replace with your logic to create a list of confessions (e.g., empty list)
    # [{
    #     "text": "I've been secretly crushing on my best friend for years, but I'm too scared to tell them n my best friend for years, but I'm too scared to tell the n my best friend for years, but I'm too scared to tell the n my best friend for years, but I'm too scared to tell the n my best friend for years, but I'm too scared to tell the.",
    #     "timestamp": "2023-12-25 12:00:00"  # Replace with actual timestamp
    # },
    # {
    #     "text": "I accidentally deleted my entire photo album and now I can't stop crying.",
    #     "timestamp": "2024-01-01 18:30:00"  # Replace with actual timestamp
    # },
    # {
    #     "text": "I'm starting to think I might be addicted to social media.",
    #     "timestamp": "2024-02-14 10:45:00"  # Replace with actual timestamp
    # },
    # {
    #     "text": "I've been hiding a secret from my family that's been eating away at me.",
    #     "timestamp": "2024-03-20 23:15:00"  # Replace with actual timestamp
    # },
    # {
    #     "text": "I'm so jealous of my sister's success, even though I'm happy for her.",
    #     "timestamp": "2024-04-05 08:00:00"  # Replace with actual timestamp
    # }
    # ]

    url = "https://confessionbe.onrender.com/retrieve_data"  # Replace with your actual endpoint URL

    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        print(response.json())  # Assuming the response is JSON
        confessions = response.json()
    else:
        print("Request failed with status code:", response.status_code)

    return reverse_list(confessions)

def main():
    st.title("Welcome to Confessions")

    # Create tabs for submission and feed
    tabs = st.tabs(["Submit Confession", "Confessions Feed"])

    with tabs[0]:
        st.header("Submit Your Confession")
        st.markdown("These confessions are highly anonymous (trust me bro 😁) and completely uncensored and unfiltered. The only rule is that there are no rules. You can confess anything.")
        confession_text = st.text_area("Enter your confession here 👇🏻:")

        if st.button("Submit"):
            # Get current time and date
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Prepare data for API request
            data = {"time": current_time, "content": confession_text}

            # Replace with your actual endpoint URL
            url = "https://confessionbe.onrender.com/receive_data"

            # Send POST request to the API
            response = requests.post(url, json=data)

            if response.status_code == 200:
                st.success("Confession submitted successfully!")
            else:
                st.error(f"Error submitting confession: {response.status_code}")

    with tabs[1]:
        st.header("Confessions Feed")
        st.markdown("______________")

        confessions = get_confessions()

        for confession in confessions:
            st.markdown(f"**{confession['content']}**")
            st.markdown(f"Submitted at: {confession['time']}")
            st.markdown("__________________________________________")  # Add a horizontal line between confessions
            st.markdown("\n")  # Add a line break



if __name__ == "__main__":
    main()