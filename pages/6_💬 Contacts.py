import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.markdown("# Keep in touch! 💬")
st.markdown("Do you have any improvement or bug fix to suggest me? Do you want to understand better this tool? Contact me 😊. I will try to reach you soon.")

with st.form("information"): 
    sender_name = st.text_input("Your name")
    sender_email = st.text_input("Your email")
    body = st.text_area('Your message')

    send_button = st.form_submit_button(label = "Send ✉️")

if send_button:
    try:
        msg = MIMEText(body)
        msg['From'] = sender_email
        msg['To'] = st.secrets["mail_contact_form"]["recipient"]
        msg['Subject'] = f"MyTripsDashboard - Contact from {sender_name} - {sender_email}"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(st.secrets["mail_contact_form"]["sender_mail"], st.secrets["mail_contact_form"]["sender_pwd"])
        server.sendmail(st.secrets["mail_contact_form"]["sender_mail"], st.secrets["mail_contact_form"]["recipient"], msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Error in sending email: {e}")