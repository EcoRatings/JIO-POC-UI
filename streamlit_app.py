# import streamlit as st

# import streamlit as st

# # Set the tab title and favicon
# st.set_page_config(page_title="sustaining.ai", page_icon="🌿")

# # Add a title with custom colors (white for 'Eco' and golden brown for 'Ratings'), centered at the top
# st.markdown("""
#     <style>
#     .title {
#         font-size: 60px;
#         font-weight: bold;
#         color: white;
#         text-align: center;  /* Center the text */
#         margin-top: -40px;   /* Adjust this value to move the title closer to the top */
#     }
#     .eco {
#         color: #ffffff;      /* White color for 'Eco' */
#     }
#     .ratings {
#         color: #d4a017;      /* Golden brown color for 'Ratings' */
#     }
#     </style>

#     <h1 class="title"><span class="eco">Eco</span><span class="ratings">Ratings</span></h1>
#     """, unsafe_allow_html=True)

# import time
# import os
# import threading
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from io import BytesIO
# import random
# import uuid
# import pandas as pd
# import requests

# # Fetch email password from environment variable
# email_password = os.getenv('EMAIL_PASSWORD')

# UPLOAD_FOLDER = 'uploads'
# RESULT_FOLDER = 'results'
# DEFAULT_EMAIL = 'n.r.rinwan@gmail.com'  # Set the default email ID here

# # Create upload and result folders if they do not exist
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# if not os.path.exists(RESULT_FOLDER):
#     os.makedirs(RESULT_FOLDER)






# # Streamlit UI
# st.title("Data Extractor")

# # Authentication
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False

# def login(username, password):
#     # Simple username and password check
#     if username == "admin" and password == "password":
#         st.session_state.authenticated = True
#         st.success("Logged in successfully!")
#         time.sleep(1)
#         st.rerun()

#     else:
#         st.error("Invalid username or password")

# # Add session state to track if we need to show the success message
# if 'show_success_message' not in st.session_state:
#     st.session_state.show_success_message = True

# if not st.session_state.authenticated:
#     st.subheader("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         login(username, password)

# else:
    # Remove all files in the result folder if a new file is uploaded
    # def cleanup_all_files():
    #     for folder in [UPLOAD_FOLDER, RESULT_FOLDER]:
    #         for filename in os.listdir(folder):
    #             file_path = os.path.join(folder, filename)
    #             try:
    #                 if os.path.isfile(file_path):
    #                     os.remove(file_path)
    #             except Exception as e:
    #                 print(f"Failed to delete {file_path}: {e}")

#     uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

#     if uploaded_file is not None:
#         # Cleanup all files if a new file is uploaded
#         cleanup_all_files()

#         # Generate unique filenames to avoid collisions
#         unique_id = uuid.uuid4()
#         filename = f"{unique_id}_{uploaded_file.name}"
#         input_path = os.path.join(UPLOAD_FOLDER, filename)

#         # Save uploaded file
#         with open(input_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         st.write("File uploaded successfully.")
#         with st.spinner('Processing file...'):
#             processing_time = random.randint(2, 6)
#             time.sleep(processing_time)

#         # Send file to external API for processing
#         url = "http://34.74.243.157:5010/upload/"
#         try:
#             with open(input_path, 'rb') as f:
#                 files = {'file': (uploaded_file.name, f, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
#                 response = requests.post(url, files=files)

#             if response.status_code == 200:
#                 # Assuming the response content is CSV data
#                 with st.spinner('Processing file...'):
#                     processing_time = random.randint(10, 20)
#                     time.sleep(processing_time)

#                 st.success("File processed successfully!")

#                 # Save the response to a CSV file
#                 output_path = os.path.join(RESULT_FOLDER, f"processed_{unique_id}.csv")
#                 with open(output_path, "w") as f:
#                     f.write(response.text)

#                 # Convert CSV to Excel for downloading
#                 df = pd.read_csv(output_path)
#                 excel_output = BytesIO()
#                 with pd.ExcelWriter(excel_output, engine='xlsxwriter') as writer:
#                     df.to_excel(writer, index=False, sheet_name='Processed Data')
#                 excel_output.seek(0)

#                 # Display button to show the Excel file content
#                 if st.button("Display Processed File Content"):
#                     st.dataframe(df)

#                 # Download button for Excel file
#                 st.download_button(label="Download Processed Excel File", data=excel_output, file_name=f"processed_{uploaded_file.name}", mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', on_click=cleanup_all_files)

#             else:
#                 st.error(f"Failed to process the file. Status code: {response.status_code}")

#         except Exception as e:
#             st.error(f"Error while processing the file: {e}")





















# # Simulate file processing
# def process_file(input_path, output_path, filename):
#     processing_time = random.randint(3, 6)  # Simulate processing time between 10 to 20 seconds
#     time.sleep(processing_time)
#     with open(output_path, 'w') as f:
#         f.write("This is the processed file.")
#     send_email_with_attachment(output_path, filename)  # Send email after processing is complete
#     return processing_time

# # Send email with the processed file
# def send_email_with_attachment(file_path, filename):
#     from_address = 'nemichand@ratings.eco'
#     to_address = DEFAULT_EMAIL
#     subject = "Processed File Ready"
#     body = f"The file {filename} has been processed and is ready. Please find the attachment."

#     # Check if email addresses are properly set
#     if not from_address or not to_address:
#         print("Email addresses are not properly set.")
#         return

#     msg = MIMEMultipart()
#     msg['From'] = from_address
#     msg['To'] = to_address
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         with open(file_path, "rb") as attachment:
#             part = MIMEBase('application', 'octet-stream')
#             part.set_payload(attachment.read())
#             encoders.encode_base64(part)
#             part.add_header('Content-Disposition', f"attachment; filename= {filename}")
#             msg.attach(part)

#         # Send email using SMTP
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         if email_password:
#             server.login(from_address, email_password)
#             server.sendmail(from_address, to_address, msg.as_string())
#         server.quit()
#     except FileNotFoundError:
#         print(f"Failed to attach file: {file_path} does not exist.")
#     except smtplib.SMTPAuthenticationError:
#         print("SMTP Authentication failed. Check email credentials or security settings.")
#     except Exception as e:
#         print(f"Failed to send email: {e}")















import streamlit as st
import os
import time
import uuid
import random
import requests
import pandas as pd
from io import BytesIO

# Set the tab title and favicon
st.set_page_config(page_title="sustaining.ai", page_icon="🌿")

# Add a title with custom colors (white for 'Eco' and golden brown for 'Ratings')
st.markdown("""
    <style>
    .title {
        font-size: 60px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-top: -40px;
    }
    .eco {
        color: #ffffff;
    }
    .ratings {
        color: #d4a017;
    }
    </style>
    <h1 class="title"><span class="eco">Eco</span><span class="ratings">Ratings</span></h1>
    """, unsafe_allow_html=True)

# Setup folder paths
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
SAMPLE_FILE_PATH = 'sample/Jio-poc-sample.xlsx'

# Ensure folders exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(RESULT_FOLDER):
    os.makedirs(RESULT_FOLDER)

# Initialize session states if not already present
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

if 'processing_complete' not in st.session_state:
    st.session_state.processing_complete = False

if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None

st.title("Data Extractor")

# Authentication
def login(username, password):
    if username == "admin" and password == "password":
        st.session_state.authenticated = True
        st.success("Logged in successfully!")
        time.sleep(1)
        st.rerun()  # Trigger rerun after login
    else:
        st.error("Invalid username or password")

# Function to clear session state after processing
def reset_processing_state():
    st.session_state.file_uploaded = False
    st.session_state.processing_complete = False
    st.session_state.processed_data = None

# UI logic
if not st.session_state.authenticated:
    # Show login screen if not authenticated
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        login(username, password)
else:
    def cleanup_all_files():
        for folder in [UPLOAD_FOLDER, RESULT_FOLDER]:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

    if not st.session_state.file_uploaded:
        # File upload section
            # Add Download Sample File button
        st.markdown("### Download Sample File for Reference:")
        with open(SAMPLE_FILE_PATH, "rb") as file:
            st.download_button(
                label="Download Sample File",
                data=file,
                file_name="Jio-poc-sample.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

        if uploaded_file is not None:
            cleanup_all_files()
            st.session_state.file_uploaded = True

            # Save uploaded file
            unique_id = uuid.uuid4()
            filename = f"{unique_id}_{uploaded_file.name}"
            input_path = os.path.join(UPLOAD_FOLDER, filename)

            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.session_state.input_path = input_path
            st.session_state.filename = filename
            st.success("File uploaded successfully!")

            st.rerun()  # Trigger rerun after file upload to proceed to next step

    elif not st.session_state.processing_complete:
        # File processing section
        st.write("File uploaded: ", st.session_state.filename)
        with st.spinner("Processing file..."):
            time.sleep(random.randint(4, 6))  # Simulate processing time

        try:
            # Simulate an external API request
            url = "http://34.74.243.157:5010/upload/"
            with open(st.session_state.input_path, 'rb') as f:
                files = {'file': (st.session_state.filename, f, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
                response = requests.post(url, files=files)

            if response.status_code == 200:
                st.success("File processed successfully!")

                # Simulate saving response to a CSV file
                output_path = os.path.join(RESULT_FOLDER, f"processed_{uuid.uuid4()}.csv")
                with open(output_path, "w") as f:
                    f.write(response.text)

                # Read processed data into Pandas DataFrame
                df = pd.read_csv(output_path)

                # Store processed data in session state
                st.session_state.processed_data = df
                st.session_state.processing_complete = True
                st.session_state.output_path = output_path

                st.rerun()  # Rerun to proceed to the next step

            else:
                st.error(f"Failed to process the file. Status code: {response.status_code}")

        except Exception as e:
            st.error(f"Error while processing the file: {e}")

    else:
        # Display the processed data section
        if st.session_state.processed_data is not None:
            st.write("File processing complete. Here is the processed content:")
            st.dataframe(st.session_state.processed_data)

            # Convert DataFrame to Excel for download
            excel_output = BytesIO()
            with pd.ExcelWriter(excel_output, engine='xlsxwriter') as writer:
                st.session_state.processed_data.to_excel(writer, index=False, sheet_name='Processed Data')
            excel_output.seek(0)

            # Download button for Excel file
            st.download_button(label="Download Processed Excel File", data=excel_output, file_name=f"processed_{st.session_state.filename}", mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

            # Reset button to allow re-upload and processing
            if st.button("Reset and Upload New File"):
                reset_processing_state()
                st.rerun()  # Rerun to reset the app state and allow new file uploads
