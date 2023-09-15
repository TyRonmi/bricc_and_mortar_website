import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as com
import codecs

    
# ---- PROJECTS SLIDESHOW FUNCTION ----
def st_slideshow(slideshow_html, height=400):
    slideshow_file = codecs.open(slideshow_html, 'r')
    page = slideshow_file.read()
    com.html(page, height=height)


def main():
    # ---- HEADER SECTION ----
    icon = Image.open('images/bricc.PNG')
    st.set_page_config(page_title="Bricc & Motar", page_icon=icon, layout="centered")
    logo= Image.open('images/bricc.PNG')
    st.image(logo)
    st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
    st.markdown("*This is not a real company... Just a demo*")
    st.write("---")  
    

    
    # ---- LOTTIE EUNCTION ----
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    #---- USE LOCAL CSS ----
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")
    
    #---- LOAD ASSETS ----
    lottie_whatWeDo = load_lottieurl("https://lottie.host/8319a3a7-1293-4147-97a3-af6748813826/gknzMOYuH9.json")
    lottie_contactUS = load_lottieurl("https://lottie.host/0487a668-2299-4c92-b8ac-1f50a4edea98/lZS3u86CNS.json")
    lottie_projects = load_lottieurl("https://lottie.host/31ca3071-aa98-4495-95c6-f234c5041662/ZnF2PlRILw.json")
    # ---- WHAT WE DO ----
    st.subheader("What We Do")  
    st_lottie(lottie_whatWeDo, height=150, key="WhatWeDo")
    
    st.write(
        """
        We are a real estate company with offices in Nigeria, Kenya and Ghana. we construct and develop affordable buildings using alternative, yet durable materials like wood, bamboo, containers and mud bricks for buildings that will leave you satisfied.
        
        Our services include:
        - Building affordable residential houses for rent and purchase
        - Building beautiful workspaces for offices
        - Providing shortlet apartments
        - Interior decoration and furnishing
        - Architectural designs and plans
        - Free airport pick-up and drop-off for new and existing clients

        """
    )
        
    st.write("---")

    #---- ONGOING PROJECTS ----
    st.subheader("Projects")
    st_lottie(lottie_projects, height=150, key="projects")
    st.write(
        """
        At Bricc & Motar, we take immense pride in our diverse portfolio of completed projects that showcase our commitment to excellence, innovation, and quality craftsmanship. With a passion for construction and an unwavering dedication to our clients, we've successfully brought countless visions to life. Explore a selection of our featured projects below to get a glimpse of what we can achieve together:
        """
        )
    st_slideshow("projects/project_show.html")
    st.write("---")
    #---- MEET OUR TEAM ----
    st.subheader("Meet Our Team")
    st.write("##")
    columnA, columnB = st.columns(2) 
    with columnA:
        imageCEO = Image.open('images/ceo.png')
        st.image(imageCEO)
        st.markdown("**Kalvin York**")
        st.write("CEO, Bricc & Motar")
        
        
    with columnB:
        imageHr = Image.open('images/hr.png')
        st.image(imageHr)
        st.markdown("**Temi Olaniyi**")
        st.write("Head, HR Department")
        
    columnC, columnD = st.columns(2)
        
    with columnC:
        imageIt = Image.open('images/it.png')
        st.image(imageIt)
        st.markdown("**Jacob Abdulmajeed**")
        st.write("Head, IT Department")
        
    with columnD:
        imageSales = Image.open('images/sales.png')
        st.image(imageSales)
        st.markdown("**Hauwa Olarotimi**")
        st.write("Head, Sales Department")
    st.write("---")

    #---- GET IN TOUCH ----
    st.subheader("Send us a Message")
    left_column, right_column = st.columns((2,1)) 
    with left_column:
        contact_form = """
        <form action="https://formsubmit.co/ronmi.eyitayo@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
       
    with right_column:
        st_lottie(lottie_contactUS, height=100, key="contactUs")
        
    st.write("---")

    #---- LOCATE and FOLLOW ----
    office_column, sm_column = st.columns(2)
    with office_column:
        st.subheader("Contact us")
        building = Image.open('images/building.png')
        st.image(building)
        st.caption("Plot ABC, Oxford Industrial Avenue, Abuja, Nigeria")

        phone = Image.open('images/telephone.png')
        st.image(phone) 
        st.caption("+2348033413132")
        
    with sm_column:      
        st.subheader("Follow us")
        facebook = Image.open('images/facebook.png')
        st.image(facebook) 
        st.caption("[Facebook](https://www.facebook.com/Brookfieldhomesabuja?mibextid=2JQ9oc)")
    
        instagram = Image.open('images/instagram.png')
        st.image(instagram)
        st.caption("[Instagram](https://instagram.com/)")
if __name__=='__main__':
    main()