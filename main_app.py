# streamlit run main_app.py --server.enableXsrfProtection false
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from streamlit_lottie import st_lottie
import requests
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os 
import plotly.express as px
import plotly.graph_objs as go
import base64
import joblib
import pandas as pd
import numpy as np
from streamlit_chat import message
import time 
import validators
import concurrent.futures
import re
import socket
import urllib.parse as urlparse
from datetime import datetime
import whois
import time
import hashlib
import pefile
import re
import os
import joblib
import pandas as pd 
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import random
import string
import math
import hashlib
import pandas as pd
import os
import json

from cryptography.fernet import Fernet
st.set_page_config(page_title="ML/AI Cyber App", page_icon="🛡️", layout="wide")
rf_model = joblib.load('phishing_model.pkl')
with open('2655649.jpg','rb') as f:
            data= f.read()
            imgs= base64.b64encode(data).decode()
            css=f""" 
                <style>
                [data-testid="stAppViewContainer"]{{
                    background-image:url('data:image/png;base64,{imgs}');
                    background-size:cover
                }}     
                
                [data-testid='stButton']{{
                    color:green;
                }}
                
                
                </style> 
                
                """
            st.markdown(css, unsafe_allow_html=True)


# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# def get_gemini_repsonse(input,prompt):
#     model=genai.GenerativeModel('gemini-1.5-flash')
#     response=model.generate_content([input,prompt])
#     return response.text


# Sidebar menu
with st.sidebar:
   
    
    selected = option_menu(
        "Menu",
        ["Home", "Threat Dashboard", "Detection Zone", "SecurePass"],
        icons=["house", "bar-chart", "search", "file-text"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0e1117"},
            "icon": {"color": "#00FFFB", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "#00FFFB",
            },
            "nav-link-selected": {"background-color": "#151D2E", "color": "#FF007F"},
            "menu-title": {
                "font-size": "18px",  # Adjust the font size of the title
                "color": "#00FF00",  # Cyber green color for the "Menu" title
                "padding": "10px 0px",  # Adding padding to space out the title
            },
        },
    )
    


# Home page content
if selected == "Home":
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            def get_gemini_response(input,prompt):
                        model=genai.GenerativeModel('gemini-1.5-flash')
                        response=model.generate_content([input,prompt])
                        return response.text
            css_animation = """
                <style>
                  .typewriter h1 {
                    overflow: hidden;
                    white-space: nowrap;
                    margin: 0 auto;
                    letter-spacing: .15em;
                    animation: 
                      typing 3.5s steps(40, end),
                      blink-caret .65s step-end 15 ,
                      color-change 3.5s infinite;
                  }
            
                  @keyframes typing {
                    from { width: 0 }
                    to { width: 100% }
                  }
            
                  @keyframes blink-caret {
                    from  { opacity: 1 }
                    to {opacity: 0 }
                    50% { opacity: 0 }
                  }
            
                  @keyframes color-change {
                    0% { color: #5F9EA0; }
                    20% { color: #D8BFD8; }
                    40% { color: #48D1CC; }
                    60% { color: #48D1CC; }
                    80% { color: #40E0D0; }
                    100% { color: #40E0D0; }
                  }
                </style>
                """
            html_content = """
                <div class="typewriter">
                  <h1 style="text-align: center; font-size: 60px; font-weight: 900;text-shadow: 0px 0px 10px #33ccff, 0px 0px 20px #33ccff, 0px 0px 30px #33ccff; color: #ffffff; font-family: 'Courier New', Courier, monospace;">
                    <span style="animation: color-change 3.5s infinite;">
                      AI Cyber
                    </span>
                    <br>
                    <span style="style="background: linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;animation: color-change 3.5s infinite;">
                      Vanguard App
                    </span>
                    
                    
                    
                    
                    
                    
                  </h1>
                </div>
                """
            
            
            st.markdown(css_animation + html_content, unsafe_allow_html=True)
              # with col2:
              #   pass
                # link='https://lottie.host/4117a8db-97dc-44da-ba1e-5cae0b3ccca6/To98bEgVdf.json'
                # st_lottie(link,key="user",width=350)
                
              
            html_content = """
                <style>
                .subheadline {
                    font-size: 18px;
                    font-weight: bold;
                    text-align: center;
                    color: #33CC33; /* green */
                    text-shadow: 0px 0px 10px #33CC33; /* glow effect */
                    background: linear-gradient(to bottom, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.5)); /* dark gradient */
                    padding: 10px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px #33CC33; /* glow effect */
                    animation: pulse 2s infinite;
                  }
            
                  @keyframes pulse {
                    0% {
                      transform: scale(1);
                    }
                    50% {
                      transform: scale(1.1);
                    }
                    100% {
                      transform: scale(1);
                    }
                  }
                </style>
            
                <h3 class="subheadline">
                  Unlock Cyber Knowledge!!!.. Ask Me Anything!!!
                </h3>
                """
            
            st.markdown(html_content, unsafe_allow_html=True)
              # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
              # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
              # def get_gemini_response(input_text,prompt):
              #             model=genai.GenerativeModel('gemini-1.5-flash')
              #             response=model.generate_content([input_text,prompt])
              #             return response.text
            
            #   input_text = st.text_input("Ask here!!", key="input")
            #   submit = st.button("Click to get your answer!!")
            
            #   input_prompt = """
            # You are an expert in cybersecurity with all knowledge about cyber attacks and their prevention.
            # Answer all user questions related to cyber threats, attacks, prevention, and symptoms only.
            # """
            
            #   if submit and input_text:
            #               response = get_gemini_response(input_text, input_prompt)
            #               st.markdown(
            #         "<h2 style='text-align: center; font-size: 40px; color: #3498db; font-weight: bold'>Here, You Go!!</h2>",
            #         unsafe_allow_html=True
            #     )
            #               st.write(response)  
                                      # except Exception as e:
                                      #             st.error(f"Error fetching response: {e}")
            input=st.text_input("Ask here!! ",key="input")
            submit=st.button("Click to get your answer!!")
            
            input_prompt="""
                You are an expert in cyber security you have  all knowledge about all cyber attacks and there prevention.
                            now you answer all the questions, input by the user related to cyber threads, attacks,prevention , symptoms only.
                """
            if submit:
                        response=get_gemini_response(input_prompt, input)
                        st.markdown("<h2  style='text-align: center; font-size: 40px; color: #3498db; font-weight: bold'>Here, You Go!!</h2>", unsafe_allow_html=True)
                        st.write(response)
            





























    

        
# Threat Dashboard page content
elif selected == "Threat Dashboard":
  st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    .cyber-title {
        font-family: 'Orbitron', sans-serif;
        color: #00ffcc;
        text-align: center;
        font-size: 3.5em;
        margin-bottom: 1rem;
        letter-spacing: 2px;
        animation: cyber-slide-in 1.5s ease-out forwards;
        opacity: 0;
        text-shadow: 0 0 5px #00ffcc, 0 0 10px #00ffcc;
    }

    @keyframes cyber-slide-in {
        0% {
            transform: translateX(-100%);
            opacity: 0;
        }
        50% {
            transform: translateX(10%);
            opacity: 0.7;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }

    .cyber-subheader {
        font-family: 'Orbitron', sans-serif;
        color: #00ffff;
        font-size: 2em;
        margin-top: 1rem;
        margin-bottom: 1rem;
        letter-spacing: 1px;
        animation: cyber-fade-in 1s ease-out forwards;
        opacity: 0;
        text-shadow: 0 0 3px #00ffff, 0 0 6px #00ffff;
    }

    @keyframes cyber-fade-in {
        0% {
            opacity: 0;
            transform: translateY(-20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .cyber-sidebar-title {
        font-family: 'Orbitron', sans-serif;
        color: #0033ff;
        font-size: 1.5em;
        margin-top: 2rem;
        text-align: center;
        text-shadow: 0 0 4px #0033ff, 0 0 8px #0033ff;
    }
    </style>
""", unsafe_allow_html=True)

# Display the enhanced title with the new animation
  st.markdown('<div class="cyber-title">Cyber Threats Dashboard</div>', unsafe_allow_html=True)

  # Sidebar for threat selection
  st.markdown('<div class="cyber-sidebar-title">Threats Menu</div>', unsafe_allow_html=True)
  threat_options = ["Phishing", "Malware", "Ransomware", "SQL Injection", "Cross-Site Scripting (XSS)", "Insider Threats", "Password Attacks"]
  selected_threat = st.selectbox("Select a Cyber Threat to Explore", threat_options)

  # Function to display the charts
  def display_charts(chart_data, threat_name):
      st.markdown(f'<div class="cyber-subheader">{threat_name}</div>', unsafe_allow_html=True)
      risk_fig = px.bar(x=chart_data['Risk Categories'], y=chart_data['Risk Levels'], 
                        title=f"Risk Levels for {threat_name}", 
                        color=chart_data['Risk Categories'],
                        color_discrete_sequence=px.colors.sequential.RdBu)
      st.plotly_chart(risk_fig, use_container_width=True)
      
      detection_fig = go.Figure(data=[go.Pie(labels=chart_data['Detection Methods'], 
                                            values=chart_data['Detection Efficiency'],
                                            hole=.3)])
      detection_fig.update_traces(marker=dict(colors=px.colors.sequential.Viridis))
      detection_fig.update_layout(title_text=f"Detection Efficiency for {threat_name}")
      st.plotly_chart(detection_fig, use_container_width=True)
      
      mitigation_fig = px.line(x=chart_data['Mitigation Strategies'], y=chart_data['Mitigation Effectiveness'],
                              title=f"Mitigation Effectiveness for {threat_name}",
                              markers=True)
      mitigation_fig.update_traces(line=dict(color=px.colors.sequential.Plasma[4], width=4))
      st.plotly_chart(mitigation_fig, use_container_width=True)

  # Content based on selected threat
  if selected_threat == "Phishing":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [80, 90],
          'Detection Methods': ["Email Filtering", "Domain Analysis", "Behavioral Analysis"],
          'Detection Efficiency': [70, 60, 80],
          'Mitigation Strategies': ["User Education", "MFA", "Regular Updates"],
          'Mitigation Effectiveness': [85, 90, 80]
      }
      display_charts(chart_data, "Phishing Attacks")

  elif selected_threat == "Malware":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [85, 80],
          'Detection Methods': ["Antivirus", "Heuristic Analysis", "Network Monitoring"],
          'Detection Efficiency': [75, 65, 70],
          'Mitigation Strategies': ["Regular Backups", "Endpoint Protection", "User Awareness"],
          'Mitigation Effectiveness': [88, 85, 75]
      }
      display_charts(chart_data, "Malware")

  elif selected_threat == "Ransomware":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [95, 75],
          'Detection Methods': ["File Monitoring", "Network Segmentation", "Behavioral Analysis"],
          'Detection Efficiency': [80, 70, 85],
          'Mitigation Strategies': ["Regular Backups", "Network Segmentation", "Incident Response Planning"],
          'Mitigation Effectiveness': [90, 87, 82]
      }
      display_charts(chart_data, "Ransomware")

  elif selected_threat == "SQL Injection":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [75, 70],
          'Detection Methods': ["Input Validation", "Web Application Firewall", "Database Monitoring"],
          'Detection Efficiency': [65, 78, 70],
          'Mitigation Strategies': ["Secure Coding Practices", "Regular Audits", "WAF Deployment"],
          'Mitigation Effectiveness': [80, 85, 90]
      }
      display_charts(chart_data, "SQL Injection")

  elif selected_threat == "Cross-Site Scripting (XSS)":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [70, 75],
          'Detection Methods': ["Content Security Policy", "Input Validation", "Output Encoding"],
          'Detection Efficiency': [70, 65, 75],
          'Mitigation Strategies': ["Secure Coding", "Regular Code Reviews", "CSP Implementation"],
          'Mitigation Effectiveness': [85, 80, 88]
      }
      display_charts(chart_data, "Cross-Site Scripting (XSS)")

  elif selected_threat == "Insider Threats":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [80, 65],
          'Detection Methods': ["User Behavior Analytics", "Access Controls", "Employee Monitoring"],
          'Detection Efficiency': [70, 60, 68],
          'Mitigation Strategies': ["Employee Training", "Access Management", "Regular Audits"],
          'Mitigation Effectiveness': [78, 85, 75]
      }
      display_charts(chart_data, "Insider Threats")

  elif selected_threat == "Password Attacks":
      chart_data = {
          'Risk Categories': ["Impact", "Likelihood"],
          'Risk Levels': [85, 80],
          'Detection Methods': ["Login Rate Limiting", "Multi-Factor Authentication", "Password Strength Analysis"],
          'Detection Efficiency': [75, 90, 70],
          'Mitigation Strategies': ["Strong Password Policies", "Regular Password Changes", "MFA Implementation"],
          'Mitigation Effectiveness': [80, 85, 90]
      }
      display_charts(chart_data, "Password Attacks")

  # Footer
  st.markdown("---")

    

# Analysis page content
import streamlit as st

# Assuming selected == "Analysis"

# Assuming selected == "Analysis"
if selected == "Detection Zone":
    st.markdown("""
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideIn {
        0% { opacity: 0; transform: translateX(-50px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    .animated-title {
        animation: fadeIn 2s ease-in-out;
    }
    .card {
        animation: slideIn 1.5s ease-in-out;
        background-color: #0d1b2a; /* Dark Navy Blue */
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
    }
    .card-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #03fcba; /* Neon Green */
    }
    .icon {
        font-size: 48px;
        color: #00d4ff; /* Bright Cyan */
        margin-bottom: 10px;
    }
    .detect-btn {
        background-color: #03fcba; /* Neon Green */
        border: none;
        color: white;
        padding: 10px 20px;
        font-size: 18px;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .detect-btn:hover {
        background-color: #05ff99; /* Light Green */
    }
    .card, .detect-btn {
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 8px 8px 20px rgba(0, 212, 255, 0.4); /* Brighter shadow on hover */
    }
    </style>
    """, unsafe_allow_html=True)
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "main"


    # Adding animated title
    
    if st.session_state.current_page == "main":
        st.markdown("<h1 class='animated-title' style='text-align: center; color: #00d4ff;'>Threat Detection</h1>", unsafe_allow_html=True)

    # Initialize session state if it doesn't exist
    
    
    
    # Layout using columns for horizontal display
        col1, col2, col3 = st.columns(3)

        # Card for Phishing URL Detection
        with col1:
            st.markdown("""
                <div class='card'>
                    <div class='icon'>🎣</div>
                    <div class='card-title'>Phishing Detection</div>
                </div>
            """, unsafe_allow_html=True)
            
            
            if st.button("Detect Now!!", key='phishing_bt'):
                st.session_state.current_page = "phishing"

            
            

        # Card for Ransomware File Detection
        with col2:
            st.markdown("""
                <div class='card'>
                    <div class='icon'>📁</div>
                    <div class='card-title'>Ransomware File Detection</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Detect Now!!", key='ransomware_bt'):
                
                st.session_state.current_page = "ransomware"

            # if st.session_state.detect == "ransomware":
            #     st.markdown("<h2>Running Ransomware File Detection...</h2>", unsafe_allow_html=True)
            #     # Add your ransomware detection code here
            #     # Example result
            #     st.markdown("<p>Ransomware detection completed.</p>", unsafe_allow_html=True)

           

        # Card for Email Spam Detection
        with col3:
            st.markdown("""
                <div class='card'>
                    <div class='icon'>✉️</div>
                    <div class='card-title'>Email Spam Detection</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Detect Now!!", key='spam'):
                
                st.session_state.current_page = "spam"

            # if st.session_state.detect == "spam":
            #     st.markdown("<h2>Running Email Spam Detection...</h2>", unsafe_allow_html=True)
            #     # Add your spam detection code here
            #     # Example result
            #     st.markdown("<p>Email spam detection completed.</p>", unsafe_allow_html=True)

            
    

    # Add a reset button to clear detection state
    


    elif st.session_state.current_page == "phishing":
        
        st.markdown("""
        <style>
            

            /* Title styling with flip animation and shadow */
            .title {
                font-size: 50px;
                font-weight: bold;
                text-align: center;
                margin-top: 50px;
                margin-bottom: 50px;
                color: #00b4d8; /* Cyber blue */
                text-shadow: 2px 2px 8px rgba(0, 180, 216, 0.7); /* Subtle shadow */
                font-family: 'Orbitron', sans-serif; /* New font style */
                animation: flipInX 4s ease-out;
            }

            @keyframes flipInX {
                from {
                    transform: perspective(400px) rotateX(90deg);
                    opacity: 0;
                }
                to {
                    transform: perspective(400px) rotateX(0deg);
                    opacity: 1;
                }
            }

            /* Input box styling with slide animation */
            .url-input {
                display: flex;
                justify-content: center;
                margin-top: 40px;
                margin-bottom: 20px;
                animation: slideIn 3s ease-out;
            }

            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(-100%);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            input[type="text"] {
                width: 100%;
                padding: 15px;
                font-size: 18px;
                border-radius: 5px;
                border: 2px solid #00b4d8;
                background-color: #1c1c1c;
                color: #ffffff;
            }

            input[type="text"]:focus {
                outline: none;
                border: 2px solid #90e0ef;
            }

            /* Button styling with hover effect */
            .submit-button {
                display: flex;
                justify-content: center;
                margin-top: 30px;
                animation: fadeIn 2s ease-out;
            }

            button {
                background-color: #00b4d8;
                border: none;
                border-radius: 5px;
                color: #141414;
                padding: 12px 25px;
                font-size: 18px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }

            button:hover {
                background-color: #90e0ef;
                transform: scale(1.05);
            }

            /* Detecting phase styling with pulse animation */
            .detecting-phase {
                margin-top: 50px;
                text-align: center;
                font-size: 24px;
                color: #90e0ef;
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0% {
                    transform: scale(1);
                }
                50% {
                    transform: scale(1.05);
                }
                100% {
                    transform: scale(1);
                }
            }

            /* Result box styling */
            .result-box {
                margin-top: 50px;
                text-align: center;
                font-size: 24px;
                background-color: #1c1c1c;
                color: #00b4d8;
                padding: 20px;
                border-radius: 5px;
                border: 2px solid #00b4d8;
                animation: fadeInResult 1.5s ease-out;
            }

            @keyframes fadeInResult {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

        </style>
        """, unsafe_allow_html=True)
    # Main App Function
        col1,col2=st.columns((3,2))
        with col1:
                st.markdown('<div class="title">🎣Phishing URL Detection System</div>', unsafe_allow_html=True)
        with col2:
                link="https://lottie.host/55adfcb2-04a4-42b6-966b-991346077992/YH70OA9DyB.json"
                st_lottie(link,key="user",height=300)



        def extract_features(url):
            """
        Extract all 89 features from the URL.
        This function replicates the feature extraction used in the original dataset.
        """
            features = {}

            # Parsing the URL
            parsed_url = urlparse.urlparse(url)
            domain = parsed_url.netloc
            path = parsed_url.path
            query = parsed_url.query

            # 1. URL Length
            features['length_url'] = len(url)
            
            # 2. Number of Dots
            features['nb_dots'] = url.count('.')
            
            # 3. Number of Hyphens
            features['nb_hyphens'] = url.count('-')
            
            # 4. Number of '@' symbols
            features['nb_at'] = url.count('@')
            
            # 5. Number of Question Marks
            features['nb_qm'] = url.count('?')
            
            # 6. Number of '&' symbols
            features['nb_and'] = url.count('&')
            
            # 7. Number of 'or' keywords
            features['nb_or'] = url.lower().count('or')
            
            # 8. Number of '=' symbols
            features['nb_eq'] = url.count('=')
            
            # 9. Number of Underscores
            features['nb_underscore'] = url.count('_')
            
            # 10. Number of Tildes (~)
            features['nb_tilde'] = url.count('~')
            
            # 11. Number of Percent (%) symbols
            features['nb_percent'] = url.count('%')
            
            # 12. Number of Slashes
            features['nb_slash'] = url.count('/')
            
            # 13. Number of Asterisks (*)
            features['nb_star'] = url.count('*')
            
            # 14. Number of Colons (:)
            features['nb_colon'] = url.count(':')
            
            # 15. Number of Commas
            features['nb_comma'] = url.count(',')
            
            # 16. Number of Semicolons
            features['nb_semicolumn'] = url.count(';')
            
            # 17. Number of Dollar ($) symbols
            features['nb_dollar'] = url.count('$')
            
            # 18. Number of Spaces
            features['nb_space'] = url.count(' ')
            
            # 19. Number of "www" occurrences
            features['nb_www'] = url.lower().count('www')
            
            # 20. Number of ".com" occurrences
            features['nb_com'] = url.lower().count('.com')
            
            # 21. Number of "//" occurrences
            features['nb_dslash'] = url.count('//')
            
            # 22. Presence of "http" in path
            features['http_in_path'] = int('http' in path.lower())
            
            # 23. Presence of "https" token in domain
            features['https_token'] = int('https' in domain.lower())
            
            # 24. Ratio of digits in URL
            features['ratio_digits_url'] = sum(c.isdigit() for c in url) / len(url)
            
            # 25. Ratio of digits in domain
            features['ratio_digits_host'] = sum(c.isdigit() for c in domain) / len(domain)
            
            # 26. Presence of punycode in domain
            features['punycode'] = int('xn--' in domain.lower())
            
            # 27. Presence of port number in URL
            features['port'] = int(':' in domain)
            
            # 28. TLD in path
            features['tld_in_path'] = int(any(tld in path.lower() for tld in ['.com', '.net', '.org', '.info', '.biz','.in']))
            
            # 29. TLD in subdomain
            features['tld_in_subdomain'] = int(any(tld in domain.lower() for tld in ['.com', '.net', '.org', '.info', '.biz','.in']))
            
            # 30. Abnormal subdomain
            features['abnormal_subdomain'] = int(len(domain.split('.')) > 3)
            
            # 31. Number of subdomains
            features['nb_subdomains'] = len(domain.split('.')) - 1
            
            # 32. Prefix/Suffix with "-"
            features['prefix_suffix'] = int('-' in domain)
            
            # 33. Random domain name
            features['random_domain'] = int(bool(re.search(r'[a-zA-Z]{8,}', domain)))
            
            # 34. Shortening service in domain
            shortening_services = r"bit\.ly|goo\.gl|tinyurl\.com|ow\.ly|t\.co"
            features['shortening_service'] = int(bool(re.search(shortening_services, domain)))
            
            # 35. Path extension
            features['path_extension'] = int(bool(re.search(r'\.\w{2,4}$', path)))
            
            # 36. Number of redirections ("//" in path)
            features['nb_redirection'] = path.count('//')
            
            # 37. Number of external redirections
            features['nb_external_redirection'] = int('http' in query.lower() or 'https' in query.lower())
            
            # 38. Length of raw words in URL
            words_raw = re.split(r'\W+', url)
            features['length_words_raw'] = sum(len(word) for word in words_raw)
            
            # 39. Character repetition in URL
            features['char_repeat'] = max([url.count(c) for c in set(url)])
            
            # 40. Length of shortest word in URL
            features['shortest_words_raw'] = min([len(word) for word in words_raw]) if words_raw else None
            
            # 41. Length of shortest word in domain
            features['shortest_word_host'] = min([len(word) for word in domain.split('.')]) if domain else None
            
            # 42. Length of shortest word in path
            features['shortest_word_path'] = min([len(word) for word in path.split('/')]) if path else None
            
            # 43. Length of longest word in URL
            features['longest_words_raw'] = max([len(word) for word in words_raw]) if words_raw else None
            
            # 44. Length of longest word in domain
            features['longest_word_host'] = max([len(word) for word in domain.split('.')]) if domain else None
            
            # 45. Length of longest word in path
            features['longest_word_path'] = max([len(word) for word in path.split('/')]) if path else None
            
            # 46. Average word length in URL
            features['avg_words_raw'] = features['length_words_raw'] / len(words_raw) if words_raw else None
            
            # 47. Average word length in domain
            words_host = domain.split('.')
            features['avg_word_host'] = sum(len(word) for word in words_host) / len(words_host) if words_host else None
            
            # 48. Average word length in path
            words_path = path.split('/')
            
            # 49. Phishing hints in URL
            features['phish_hints'] = int('login' in url.lower() or 'secure' in url.lower() or 'libgen' in url.lower() or 'pancakexchange' in url.lower() or 'reg-vod' in url.lower())
            
            # 50. Domain in brand
            features['domain_in_brand'] = int('paypal' in domain.lower() or 'apple' in domain.lower() )
            
            # 51. Brand in subdomain
            features['brand_in_subdomain'] = int('paypal' in domain.split('.')[0].lower() or 'apple' in domain.split('.')[0].lower() )
            
            # 52. Brand in path
            features['brand_in_path'] = int('paypal' in path.lower() or 'apple' in path.lower())
            
            # 53. Suspicious TLD
            suspicious_tlds = ['.top', '.gq', '.tk', '.ml', '.cf']
            features['suspecious_tld'] = int(any(tld in domain.lower() for tld in suspicious_tlds))
            
            try:   
                whois_info = whois.whois(domain)
                features['whois_registered_domain'] = whois_info.domain_name
            except:
                features['whois_registered_domain'] = None
            
            # 80. Domain registration length
            try:
                creation_date = whois_info.creation_date
                expiration_date = whois_info.expiration_date
                features['domain_registration_length'] = (expiration_date - creation_date).days if expiration_date and creation_date else 0
            except:
                features['domain_registration_length'] = None
            
            # 81. Domain age
            try:
                age = (datetime.now() - creation_date).days if creation_date else None
                features['domain_age'] = age
            except:
                features['domain_age'] = None
            
            
            try:
                features['dns_record'] = 1 if socket.gethostbyname(domain) else None
            except:
                features['dns_record'] = None
            
            
            
            return features


        def predict_url_status(url, rf_model, feature_columns):
            """
            Predict the status of a URL using the provided model and encoder.

            Args:
                url (str): The URL to analyze.
                model (sklearn model): The trained model for prediction.
                encoder (sklearn encoder): The label encoder to decode the prediction.
                feature_columns (list): List of feature column names in the correct order.

            Returns:
                str: The predicted status of the URL (e.g., 'phishing' or 'benign').
            """
            # Extract features from the URL
            url_features = extract_features(url)

            # Convert the feature dictionary to a DataFrame
            url_features_df = pd.DataFrame([url_features])

            # Handle missing features by adding them with default values
            missing_cols = set(feature_columns) - set(url_features_df.columns)
            for col in missing_cols:
                url_features_df[col] = None  # Or use an appropriate default value

            # Reorder the DataFrame columns to match the model's expected input
            url_features_df = url_features_df[feature_columns]

            # Ensure the DataFrame is of the correct type for the model
            url_features_df = url_features_df.astype(float)

            # Make a prediction
            prediction = rf_model.predict(url_features_df)

            # Decode the predicted status
            

            return prediction

        html_content = """
            <style>
            .subheadline {
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                color: #00b4d8; /* green */
                text-shadow: 0px 0px 10px #00b4d8; /* glow effect */
                background: linear-gradient(to bottom, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.5)); /* dark gradient */
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #00b4d8; /* glow effect */
                animation: pulse 4s infinite ;
            }

            @keyframes pulse {
                0% {
                transform: scale(1);
                }
                50% {
                transform: scale(1.1);
                }
                100% {
                transform: scale(1);
                }
            }
            </style>

            <h3 class="subheadline">
            Enter URL for detection!!!
            </h3>
            """

        st.markdown(html_content, unsafe_allow_html=True)
        url=st.text_input("Enter Here",key=input)


        feature_columns = ['length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens',
            'nb_at', 'nb_qm', 'nb_and', 'nb_or', 'nb_eq', 'nb_underscore',
            'nb_tilde', 'nb_percent', 'nb_slash', 'nb_star', 'nb_colon', 'nb_comma',
            'nb_semicolumn', 'nb_dollar', 'nb_space', 'nb_www', 'nb_com',
            'nb_dslash', 'http_in_path', 'https_token', 'ratio_digits_url',
            'ratio_digits_host', 'punycode', 'port', 'tld_in_path',
            'tld_in_subdomain', 'abnormal_subdomain', 'nb_subdomains',
            'prefix_suffix', 'random_domain', 'shortening_service',
            'path_extension', 'nb_redirection', 'nb_external_redirection',
            'length_words_raw', 'char_repeat', 'shortest_words_raw',
            'shortest_word_host', 'shortest_word_path', 'longest_words_raw',
            'longest_word_host', 'longest_word_path', 'avg_words_raw',
            'avg_word_host', 'avg_word_path', 'phish_hints', 'domain_in_brand',
            'brand_in_subdomain', 'brand_in_path', 'suspecious_tld',
            'statistical_report', 'nb_hyperlinks', 'ratio_intHyperlinks',
            'ratio_extHyperlinks', 'ratio_nullHyperlinks', 'nb_extCSS',
            'ratio_intRedirection', 'ratio_extRedirection', 'ratio_intErrors',
            'ratio_extErrors', 'login_form', 'external_favicon', 'links_in_tags',
            'submit_email', 'ratio_intMedia', 'ratio_extMedia', 'sfh', 'iframe',
            'popup_window', 'safe_anchor', 'onmouseover', 'right_clic',
            'empty_title', 'domain_in_title', 'domain_with_copyright',
            'whois_registered_domain', 'domain_registration_length', 'domain_age',
            'web_traffic', 'dns_record', 'google_index', 'page_rank']


        # Make sure you have installed the validators library

        # Function to validate the URL
        def is_valid_url(url):
            return validators.url(url)

        # Placeholder for "Detecting..." message
        detecting_placeholder = st.empty()

        if st.button("Detect"):
            
            if not url:
                st.warning("Please enter a URL to analyze.")
            else:
                # Validate the URL
                if not is_valid_url(url):
                    st.error("Invalid URL. Please enter a valid URL.")
                else:
                    # Display the "Detecting..." message
                    with detecting_placeholder:
                        st.markdown('<div class="detecting-phase">Detecting...</div>', unsafe_allow_html=True)
                    
                    # Simulate detection process
                    time.sleep(2)
                    
                    # Extract features from the input URL
                    features = extract_features(url)
                    
                    # Predict using the loaded model
                    predicted_status = predict_url_status(url, rf_model, feature_columns)
                    
                    # Clear the "Detecting..." message
                    detecting_placeholder.empty()
                    
                    # Display the prediction result
                    if predicted_status == 1:
                        st.markdown(
                            """
                            <style>
                            body {
                                background-color: #0a0f24;
                                color: #ffffff;
                                font-family: 'Lucida Console', Monaco, monospace;
                            }
                            .subtitle {
                                font-size: 3em;
                                text-align: center;
                                color: #ff0000;
                                text-shadow: 0 0 15px #ff0000, 0 0 30px #ff0000;
                                animation: pulse 2s infinite;
                            }
                            @keyframes pulses {
                                0% { text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000; }
                                50% { text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000; }
                                100% { text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000; }
                            }
                            .phishing-icon {
                                width: 100px;
                                height: 100px;
                                display: block;
                                margin-left: auto;
                                margin-right: auto;
                                animation: rotate 4s linear infinite;
                            }
                            @keyframes rotate {
                                from { transform: rotate(0deg); }
                                to { transform: rotate(360deg); }
                            }
                            </style>
                            """,
                            unsafe_allow_html=True
                        )

                        # Header with animated phishing icon
                        st.markdown('<div class="subtitle">⚠️ Attention!! Phishing Attack ⚠️</div>', unsafe_allow_html=True)
                        
                    else:
                        st.markdown("""
                            <style>
                            .success-message {
                                font-size: 20px;
                                color: #ffffff;
                                background-color: #28a745;
                                padding: 10px;
                                border-radius: 8px;
                                text-align: center;
                                width: fit-content;
                                margin: 20px auto;
                                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                                animation: fadeInUp 3s ease-in-out;
                            }

                            @keyframes fadeInUp {
                                0% {
                                    opacity: 0;
                                    transform: translateY(20px);
                                }
                                100% {
                                    opacity: 1;
                                    transform: translateY(0);
                                }
                            }

                            </style>
                            <div class="success-message">
                                This URL appears to be legitimate.
                            </div>
                        """, unsafe_allow_html=True)













                    # st.markdown("<h2>Running Phishing Detection...</h2>", unsafe_allow_html=True)
                    # # Add your phishing detection code here
                    # # Example result
                    # st.markdown("<p>Phishing detection completed.</p>", unsafe_allow_html=True)
                    
    elif st.session_state.current_page == "ransomware":
            rf_model = joblib.load('ransomware_model.pkl')
            def compute_md5(file_path):
                md5_hash = hashlib.md5()
                with open(file_path, 'rb') as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        md5_hash.update(byte_block)
                return md5_hash.hexdigest()

            def find_bitcoin_addresses(file_path):
                with open(file_path, 'rb') as f:
                    data = f.read()
                    # Bitcoin address regex
                    bitcoin_regex = re.compile(b'([13][a-km-zA-HJ-NP-Z1-9]{25,34})')
                    addresses = bitcoin_regex.findall(data)
                    return [addr.decode('utf-8') for addr in addresses]


            def extract_dll_info(file_path):
                try:
                    pe = pefile.PE(file_path)
            
                    info = {
                        # 'FileName': file_path.split('/')[-1],
                        # 'md5Hash': compute_md5(file_path),
                        'Machine': pe.FILE_HEADER.Machine,
                        'DebugSize': pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size,  # Debug directory
                        'DebugRVA': pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].VirtualAddress,  # Debug RVA
                        'MajorImageVersion': pe.OPTIONAL_HEADER.MajorImageVersion,
                        'MajorOSVersion': pe.OPTIONAL_HEADER.MajorOperatingSystemVersion,
                        'ExportRVA': pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress,  # Export directory
                        'ExportSize': pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size,
                        'IatVRA': pe.OPTIONAL_HEADER.DATA_DIRECTORY[12].VirtualAddress,  # Import Address Table
                        'MajorLinkerVersion': pe.OPTIONAL_HEADER.MajorLinkerVersion,
                        'MinorLinkerVersion': pe.OPTIONAL_HEADER.MinorLinkerVersion,
                        'NumberOfSections': pe.FILE_HEADER.NumberOfSections,
                        'SizeOfStackReserve': pe.OPTIONAL_HEADER.SizeOfStackReserve,
                        'DllCharacteristics': pe.OPTIONAL_HEADER.DllCharacteristics,
                        'ResourceSize': pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size,  # Resource directory
                        'BitcoinAddresses': find_bitcoin_addresses(file_path)or 0
                    }

                    return info

                except Exception as e:
                    return {'error': str(e)}

            def predict_file_status(file_path, rf_model, feature_columns):
                
                # Extract features from the DLL file
                url_features = extract_dll_info(file_path)
                
                # Ensure no `None` values in the extracted features
                for key, value in url_features.items():
                    if value is None:
                        # Set default value for missing or None values
                        url_features[key] = 0  # You can change this to a more appropriate default

                # Convert the feature dictionary to a DataFrame
                url_features_df = pd.DataFrame([url_features])
                
                # Handle missing features by adding them with default values (e.g., 0 for numerical features)
                missing_cols = set(feature_columns) - set(url_features_df.columns)
                for col in missing_cols:
                    url_features_df[col] = 0  # Use an appropriate default value, like 0
                
                # Reorder the DataFrame columns to match the model's expected input
                url_features_df = url_features_df[feature_columns]
                
                # Ensure the DataFrame contains the correct data types for the model (e.g., float)
                url_features_df = url_features_df.astype(float)
                
                # Make a prediction
                try:
                    prediction = rf_model.predict(url_features_df)
                except ValueError as e:
                    print(f"Error during prediction: {e}")
                    return None
                
                # Decode the predicted status (if needed)
                
                return prediction

            # Example usage (assuming rf_model and feature_columns are predefined):
            # status = predict_file_status("path/to/file", rf_model, feature_columns)
            # print(status)
            feature_columns = ['Machine', 'DebugSize', 'DebugRVA', 'MajorImageVersion', 'MajorOSVersion', 'ExportRVA', 'ExportSize',
                        'IatVRA', 'MajorLinkerVersion', 'MinorLinkerVersion', 'NumberOfSections', 'SizeOfStackReserve',
                        'DllCharacteristics', 'ResourceSize', 'BitcoinAddresses']
            # Apply custom styles for typing effect with a spin animation
            st.markdown(
                """
                <style>
                @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

                /* Typing effect */
                .cyber-title {
                    font-family: 'VT323', monospace;
                    font-size: 70px;
                    color: #00ccff; /* Soft neon cyan */
                    letter-spacing: 3px;
                    white-space: nowrap;
                    overflow: hidden;
                    display: inline-block;
                    animation: typing 4s steps(30, end);
                }

                /* Typing animation */
                @keyframes typing {
                    from { width: 0; }
                    to { width: 100%; }
                }

                /* Spin effect for each character */
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    50% { transform: rotate(360deg); } /* Spin to full rotation */
                    100% { transform: rotate(0deg); } /* Back to original position */
                }

                /* Glow effect */
                .cyber-title span {
                    display: inline-block;
                    animation: spin 8s ease-in-out forwards, glow 1.5s infinite alternate;
                }

                /* Glow effect */
                @keyframes glow {
                    0% { text-shadow: 0 0 10px #00ccff, 0 0 20px #00ccff, 0 0 30px #00ccff; }
                    50% { text-shadow: 0 0 15px #00ccff, 0 0 30px #00ccff, 0 0 60px #00ccff; }
                    100% { text-shadow: 0 0 10px #00ccff, 0 0 20px #00ccff, 0 0 30px #00ccff; }
                }
                </style>
                """, unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

                /* Cyber-themed upload file section */
                .upload-section {
                    font-family: 'VT323', monospace;
                    font-size: 24px;
                    color: #00ccff; /* Soft neon cyan */
                    letter-spacing: 2px;
                    text-shadow: 0 0 5px #00ccff, 0 0 10px #00ccff; /* Glow effect */
                }

                /* Glowing effect */
                @keyframes glow {
                    0% { text-shadow: 0 0 5px #00ccff, 0 0 10px #00ccff; }
                    50% { text-shadow: 0 0 10px #00ccff, 0 0 20px #00ccff; }
                    100% { text-shadow: 0 0 5px #00ccff, 0 0 10px #00ccff; }
                }
                
                .upload-section span {
                    display: inline-block;
                    animation: glow 1.5s infinite alternate;
                }
                </style>
                """, unsafe_allow_html=True)
            detecting_placeholder = st.empty()

            def add_glow(text):
                return ''.join(f'<span>{char}</span>' for char in text)


            # Function to wrap text for glow animation

            # Function to wrap each letter with a span for animation
            def add_spin(text):
                return ''.join(f'<span>{char}</span>' for char in text)

            # Front End Design for Ransomware Detection App
            def ransomware_detection_ui():
                # Cyber-themed animated title with typing and spin effect
                title_text = "Ransomware.. Detection"
                st.markdown(f'<div class="cyber-title">{add_spin(title_text)}</div>', unsafe_allow_html=True)


                # Upload File Sectio# 
                
                upload_text = "Upload Suspicious File 📁:"
                st.markdown(f'<div class="upload-section">{add_glow(upload_text)}</div>', unsafe_allow_html=True)
                uploaded_file = st.file_uploader("", type=['dll'])
                if uploaded_file is not None:
                    # Create temp directory if it doesn't exist
                    if not os.path.exists('temp'):
                        os.makedirs('temp')
                
                # Save the uploaded file to the temp directory
                    file_path = os.path.join('temp', uploaded_file.name)
                    with open(file_path, 'wb') as f:
                        f.write(uploaded_file.getbuffer())

                # dll_info = extract_dll_info(file_path)

                    # Detection Button
                if st.button("Detect Ransomware"):
                        if uploaded_file is not None:
                            # with detecting_placeholder:
                            #     st.write("Detecting.....")
                            
                            # # Simulate detection process
                            #     time.sleep(2)
                                
                            
                            #     
                                
                            #     # Clear the "Detecting..." message
                            #     detecting_placeholder.empty()
                            # st.write("### Processing the file...")
                            # progress_bar = st.progress(0)
                            # for i in range(100):
                            #     time.sleep(0.02)  # Simulate a time-consuming process
                            #     progress_bar.progress(i + 1)
                            processing_placeholder = st.empty()

                    # Use the placeholder to display the text and progress bar
                            with processing_placeholder.container():
                                st.markdown(
                                    """
                                    <style>
                                    .processing-text {
                                        color: #FFA500; /* Orange color */
                                        font-size: 1.5em;
                                        text-align: center;
                                        font-weight: bold;
                                    }
                                    </style>
                                    <div class="processing-text">Processing the file...</div>
                                    """, 
                                    unsafe_allow_html=True
                                )
                                progress_bar = st.progress(0)

                            # Simulate a time-consuming process with the progress bar
                            for i in range(100):
                                time.sleep(0.02)  # Simulate the processing time
                                progress_bar.progress(i + 1)
                            
                            # Predict the ransomware status (simulation)
                            predicted_status = predict_file_status(file_path, rf_model, feature_columns)
                            
                            # Once the prediction is done, clear both the progress bar and text
                            processing_placeholder.empty()
                            if predicted_status == 0:
                                st.markdown(
                                    """
                                    <style>
                                    body {
                                        background-color: #0a0f24;
                                        color: #ffffff;
                                        font-family: 'Lucida Console', Monaco, monospace;
                                    }
                                    .subtitle {
                                        font-size: 3em;
                                        text-align: center;
                                        color: #ff0000;
                                        text-shadow: 0 0 15px #ff0000, 0 0 30px #ff0000;
                                        animation: pulse 2s infinite;
                                    }
                                    @keyframes pulses {
                                        0% { text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000; }
                                        50% { text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000; }
                                        100% { text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000; }
                                    }
                                    .phishing-icon {
                                        width: 100px;
                                        height: 100px;
                                        display: block;
                                        margin-left: auto;
                                        margin-right: auto;
                                        animation: rotate 4s linear infinite;
                                    }
                                    @keyframes rotate {
                                        from { transform: rotate(0deg); }
                                        to { transform: rotate(360deg); }
                                    }
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                                )

                                # Header with animated phishing icon
                                st.markdown('<div class="subtitle"> ☠ Ransomware Attack ☠</div>', unsafe_allow_html=True)
                                
                            else:
                                    st.markdown("""
                                        <style>
                                        .success-message {
                                            font-size: 20px;
                                            color: #ffffff;
                                            background-color: #28a745;
                                            padding: 10px;
                                            border-radius: 8px;
                                            text-align: center;
                                            width: fit-content;
                                    margin: 20px auto;
                                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                                    animation: fadeInUp 3s ease-in-out;
                                }

                                @keyframes fadeInUp {
                                    0% {
                                        opacity: 0;
                                        transform: translateY(20px);
                                    }
                                    100% {
                                        opacity: 1;
                                        transform: translateY(0);
                                    }
                                }

                                </style>
                                <div class="success-message">
                                    🤩file appears to be safe🤩..
                                </div>
                            """, unsafe_allow_html=True)

                            # st.write("The URL  is predicted to be ",predicted_status)

                            # # Here, you would call your ransomware detection function
                            # result = "Ransomware Detected!"  # Simulated result
                            # st.success(result)
                        else:
                            st.error("Please upload a file first.")

                    # Clear Button to reset the interface
                if st.button("Clear"):
                        st.experimental_rerun()

            # Sidebar content


            # Streamlit Layout
            def main():
                ransomware_detection_ui()

            if __name__ == "__main__":
                main()

                    # st.markdown("<h2>Running Ransomware File Detection...</h2>", unsafe_allow_html=True)
                    # # Add your ransomware detection code here
                    # # Example result
                    # st.markdown("<p>Ransomware detection completed.</p>", unsafe_allow_html=True)
    elif st.session_state.current_page == "spam":
        st.markdown(
    '''
    <style>
    @keyframes typing {
        0% { width: 0; }
        100% { width: 100%; }
    }

    @keyframes blink {
        50% { border-color: transparent; }
    }

    h1 {
        overflow: hidden;
        
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .15em;
        animation: 
            typing 3.5s steps(40, end), 
            blink .75s step-end infinite;
        color: #00FFFF;
        text-shadow: 2px 2px #FF00FF;
    }

    body {
        background-color: #0F0F0F;
        color: white;
    }

    </style>
    <h1>🔐 Email Spam Detection 🛡️</h1>
    ''', 
    unsafe_allow_html=True
)

# Introductionst.write("### Detect if an email is spam or ham using advanced machine learning techniques 🚀.")
        st.write("### Give it a try by entering the text of an email you'd like to check for spam! 📧")

        # Load the saved model and vectorizer

        model = joblib.load('spam_classifier_model.pkl')


        vectorizer = joblib.load('tfidf_vectorizer.pkl')

        # Input email text
        email_input = st.text_area("Enter the email content here:", height=200, placeholder="Paste the email text here...")

        # Process input and display results

        if st.button("🔍 Detect Spam"):
            if not email_input:
                st.warning("Please enter a EMAIL to analyze.") 
            else:
                with st.spinner('🔎 Analyzing the email... Please wait...'):
                    input_features = vectorizer.transform([email_input])
                    prediction = model.predict(input_features)[0]

                    # Display the result with animation
                    if prediction == 1:
                        st.markdown(
                            '''
                            <style>
                            .spam-result {
                                font-size: 24px;
                                color: #FF4B4B;
                                text-align: center;
                                animation: shake 0.5s;
                                animation-iteration-count: 2;
                            }
                            
                            @keyframes shake {
                                0% { transform: translate(1px, 1px) rotate(0deg); }
                                10% { transform: translate(-1px, -2px) rotate(-1deg); }
                                20% { transform: translate(-3px, 0px) rotate(1deg); }
                                30% { transform: translate(3px, 2px) rotate(0deg); }
                                40% { transform: translate(1px, -1px) rotate(1deg); }
                                50% { transform: translate(-1px, 2px) rotate(-1deg); }
                                60% { transform: translate(-3px, 1px) rotate(0deg); }
                                70% { transform: translate(3px, 1px) rotate(-1deg); }
                                80% { transform: translate(-1px, -1px) rotate(1deg); }
                                90% { transform: translate(1px, 2px) rotate(0deg); }
                                100% { transform: translate(1px, -2px) rotate(-1deg); }
                            }
                            </style>
                            <div class="spam-result">🚨 This email is classified as **Spam**! Be cautious. ⚠️</div>
                            ''', 
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            '''
                            <style>
                            .ham-result {
                                font-size: 24px;
                                color: #00FF00;
                                text-align: center;
                                animation: fadeIn 1.5s ease-in-out;
                            }

                            @keyframes fadeIn {
                                0% { opacity: 0; }
                                100% { opacity: 1; }
                            }
                            </style>
                            <div class="ham-result">✅ This email is safe! You're good to go.👍</div>
                            ''', 
                            unsafe_allow_html=True
                        )

                    # st.markdown("<h2>Running Email Spam Detection...</h2>", unsafe_allow_html=True)
                    # # Add your spam detection code here
                    # # Example result
                    # st.markdown("<p>Email spam detection completed.</p>", unsafe_allow_html=True)

        
    if st.session_state.current_page != "main":
            if st.button("Go Back"):
                st.session_state.current_page = "main"

if selected == "SecurePass":
    st.markdown("""
    <style>
        .card {
            background-color: #1e1e2f;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(57, 255, 20, 0.3);
            transition: transform 0.2s, box-shadow 0.2s;
            text-align: center;
            font-family: Arial, sans-serif;
            color: #fff;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 25px rgba(57, 255, 20, 0.5);
        }
        .title {
            font-size: 1.5rem;
            color: #39FF14;
            margin-bottom: 10px;
        }
        .description {
            font-size: 1rem;
            color: #b0b0b0;
            margin-bottom: 20px;
        }
        .btn {
            background-color: #39FF14;
            color: #000;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .btn:hover {
            background-color: #2ecc71;
        }
        .container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 30px;
        }
    </style>
    """, unsafe_allow_html=True)
    if 'current_page' not in st.session_state:
            st.session_state.current_page = "main"

    if st.session_state.current_page == "main":
        st.markdown("<h1 style='text-align: center; color: #39FF14;'>🔐 Welcome to CyberVault 🔐</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: #b0b0b0;'>Your one-stop solution for secure passwords</h4>", unsafe_allow_html=True)


    # Card layout
        st.markdown("""
            <div class="container">
                <!-- Card 1 -->
                <div class="card">
                    <div class="title">🔍 Strength-o-Meter</div>
                    <div class="description">Test the strength of your passwords and get improvement tips!</div>
                </div>
                <!-- Card 2 -->
                <div class="card">
                    <div class="title">🔧 Password Forge</div>
                    <div class="description">Generate strong, unique passwords tailored to your needs.</div>
                </div>
                <!-- Card 3 -->
                <div class="card">
                    <div class="title">💾 Vault Keeper</div>
                    <div class="description">Securely store and manage your passwords with ease.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Buttons below cards
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            if st.button("Go to Strength-o-Meter",key="strength"):
                st.session_state.current_page = "strength_c"
                





        with col2:
            if st.button("Go to Password Forge",key="forge"):
                st.session_state.current_page = "forge_p"
                

        with col3:
            if st.button("Go to Vault Keeper",key="Vault"):
                st.session_state.current_page = "Vault_k"
    elif st.session_state.current_page == "strength_c":
        st.markdown("""
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Courier New', Courier, monospace;
            }
            .header {
                text-align: center;
                font-size: 2em;
                color: #ff6347;
                animation: glow 1s infinite alternate;
            }
            @keyframes glow {
                from { text-shadow: 0 0 10px #ff6347, 0 0 20px #ff6347; }
                to { text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500; }
            }
            .tips {
                color: #39ff14;
            }
        </style>
    """, unsafe_allow_html=True)

    # Animated header
        st.markdown("<h1 class='header'>🔒 Password Strength Checker 🔒</h1>", unsafe_allow_html=True)
        st.write("---")

        # Function to check password strength
        def check_password_strength(password):
            length_error = len(password) < 8
            digit_error = re.search(r"\d", password) is None
            uppercase_error = re.search(r"[A-Z]", password) is None
            lowercase_error = re.search(r"[a-z]", password) is None
            symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

            score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])
            
            if score == 5:
                return "Strong", "#39ff14"
            elif score >= 3:
                return "Moderate", "#ffcc00"
            else:
                return "Weak", "#ff4500"

        # User input for password
        password = st.text_input("Enter your password:", type="password")
        check_button = st.button("Check Password")

        if check_button and password:
            # Check strength
            strength, color = check_password_strength(password)
            st.markdown(f"<h3 style='text-align: center; color: {color};'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

            # Feedback and tailored security tips
            if strength == "Weak":
                st.error("🔴 Weak Password: Add more characters, include digits, uppercase letters, and symbols.")
                st.markdown("<h4 class='tips'>💡 Tips to Strengthen Weak Passwords:</h4>", unsafe_allow_html=True)
                st.write("""
                    - Increase the length of your password (at least 12 characters).
                    - Use a mix of uppercase, lowercase, numbers, and symbols.
                    - Avoid using your name, birthdate, or any predictable sequences.
                """)
            elif strength == "Moderate":
                st.warning("🟡 Moderate Password: Strengthen it by adding more variety of characters.")
                st.markdown("<h4 class='tips'>💡 Tips to Improve Moderate Passwords:</h4>", unsafe_allow_html=True)
                st.write("""
                    - Add more symbols or numbers to increase complexity.
                    - Use a passphrase with unrelated words.
                    - Consider avoiding dictionary words.
                """)
            else:
                st.success("🟢 Strong Password: Great job!")
                st.markdown("<h4 class='tips'>💡 Tips to Maintain Strong Passwords:</h4>", unsafe_allow_html=True)
                st.write("""
                    - Use a password manager to securely store your strong passwords.
                    - Avoid reusing passwords across multiple platforms.
                    - Regularly update your passwords to maintain security.
                """)
    elif st.session_state.current_page == "forge_p":
        def generate_passwords(characters, length, num_passwords, allow_repetition):
            password_list = []
            for _ in range(num_passwords):
                if allow_repetition:
                    password = ''.join(random.choice(characters) for _ in range(length))
                else:
                    if len(characters) < length:
                        st.error("Not enough unique characters to generate a password of the requested length without repetition.")
                        return []
                    password = ''.join(random.sample(characters, length))
                password_list.append(password)
            return password_list

    # Function to calculate entropy of a password
        def calculate_entropy(password):
            pool_size = 0
            if any(c.isdigit() for c in password):
                pool_size += 10  # Numbers
            if any(c.islower() for c in password):
                pool_size += 26  # Lowercase letters
            if any(c.isupper() for c in password):
                pool_size += 26  # Uppercase letters
            if any(c in string.punctuation for c in password):
                pool_size += len(string.punctuation)  # Special characters
            
            entropy = len(password) * math.log2(pool_size)
            return entropy
        def brute_force_time_estimator(password):
            char_space = 0
            if any(c.isdigit() for c in password):
                char_space += 10  # Digits
            if any(c.islower() for c in password):
                char_space += 26  # Lowercase
            if any(c.isupper() for c in password):
                char_space += 26  # Uppercase
            if any(c in string.punctuation for c in password):
                char_space += len(string.punctuation)  # Special characters

            total_combinations = char_space ** len(password)
            attack_speed = 1e9  # 1 billion guesses per second
            time_to_crack_seconds = total_combinations / attack_speed
            
            return time_to_crack_seconds

        # Custom CSS for styling
        st.markdown("""
            <style>
            body {
                background-color: #121212;
                color: #00FFCC;
                font-family: 'Courier New', Courier, monospace;
            }
            h1 {
                color: #00FFCC;
                text-align: center;
                animation: fadeIn 2s ease-in;
            }
            input, button {
                border-radius: 8px;
                padding: 10px;
                margin: 10px;
            }
            .stButton>button {
                background-color: #00FFCC;
                color: #121212;
                border: none;
                font-size: 1.2em;
                padding: 10px 20px;
                border-radius: 10px;
                transition: background-color 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #006666;
            }
            @keyframes fadeIn {
                0% {opacity: 0;}
                100% {opacity: 1;}
            }
            @keyframes slideIn {
                0% {transform: translateY(-100%);}
                100% {transform: translateY(0);}
            }
            .passwords {
                animation: slideIn 0.8s ease-out;
                color: #00FFCC;
                font-weight: bold;
                margin: 10px;
                background-color: #333;
                padding: 15px;
                border-radius: 8px;
            }
            </style>
            """, unsafe_allow_html=True)

        # App title and description
        st.title("💻Password Generator 🔐")
        st.markdown("Welcome to the password generator! Customize your inputs and create strong passwords that are both secure and unique.")

        # Input form
        with st.form("password_form"):
            st.markdown("### Enter Characters to Use:")
            numbers = st.text_input("Numbers (e.g., 123456):", value="123456")
            alphabets = st.text_input("Alphabets (e.g., abcdefghijklmnopqrstuvwxyz):", value="abcdefghijklmnopqrstuvwxyz")
            special_characters = st.text_input("Special Characters (e.g., @#$%^&*):", value="!@#$%^&*")

            st.markdown("### Password Configuration:")
            password_length = st.number_input("Enter password length:", min_value=1, max_value=50, value=12)
            num_passwords = st.number_input("Enter number of passwords to generate:", min_value=1, max_value=100, value=5)
            allow_repetition = st.checkbox("Allow repetition of characters", value=True)
            
            # Submit button
            submitted = st.form_submit_button("Generate Passwords")

        # Generate passwords on form submission
        if submitted:
            characters = numbers + alphabets + special_characters
            if not characters:
                st.error("Please provide some characters to generate passwords.")
            else:
                passwords = generate_passwords(characters, password_length, num_passwords, allow_repetition)
                if passwords:
                    st.markdown("### Generated Passwords:")
                    for idx, pwd in enumerate(passwords):
                        entropy = calculate_entropy(pwd)
                        time_to_crack = brute_force_time_estimator(pwd)
                        st.markdown(f"<div class='passwords'>{idx+1}: {pwd} (Entropy: {entropy:.2f})</div>", unsafe_allow_html=True)
                    st.markdown(f"⏳ Estimated time to crack: **{time_to_crack:.2f} seconds** at 1 billion guesses per second.")

    elif st.session_state.current_page == "Vault_k":
        MASTER_PASSWORD_HASH = hashlib.sha256("raman132002@".encode()).hexdigest()

    # Encryption key for storing passwords
        if not os.path.exists("key.key"):
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
        else:
            with open("key.key", "rb") as key_file:
                key = key_file.read()

        cipher = Fernet(key)

        # File to store passwords
        PASSWORD_FILE = "passwords.json"

        if not os.path.exists(PASSWORD_FILE):
            with open(PASSWORD_FILE, "w") as f:
                json.dump({}, f)

        # Verify master password
        def verify_password(input_password):
            input_hash = hashlib.sha256(input_password.encode()).hexdigest()
            return input_hash == MASTER_PASSWORD_HASH

        # Save password
        def save_password(title, password):
            with open(PASSWORD_FILE, "r") as f:
                data = json.load(f)
            encrypted_password = cipher.encrypt(password.encode()).decode()
            data[title] = encrypted_password
            with open(PASSWORD_FILE, "w") as f:
                json.dump(data, f)

        # Load saved passwords
        def load_passwords():
            with open(PASSWORD_FILE, "r") as f:
                data = json.load(f)
            decrypted_data = {title: cipher.decrypt(encrypted_password.encode()).decode() for title, encrypted_password in data.items()}
            return decrypted_data

        # App layout
        

        st.markdown("<h1 style='text-align: center; color: #ff6347;'>🔒 Password Manager</h1>", unsafe_allow_html=True)
        st.write("---")

        # Login screen
        if "authenticated" not in st.session_state:
            st.session_state["authenticated"] = False

        if not st.session_state["authenticated"]:
            st.markdown("<h3 style='text-align: center;'>Enter Master Password</h3>", unsafe_allow_html=True)
            password_input = st.text_input("Master Password", type="password")
            if st.button("Login"):
                if verify_password(password_input):
                    st.session_state["authenticated"] = True
                    st.success("Access Granted")
                else:
                    st.error("Invalid Master Password")
        else:
            # Main password manager
            st.markdown("<h3>Save and Manage Your Passwords</h3>", unsafe_allow_html=True)

            # Input for new password
            with st.form("password_form"):
                title = st.text_input("Title", placeholder="E.g., Gmail, Facebook")
                password = st.text_input("Password", placeholder="Enter password", type="password")
                submit = st.form_submit_button("Save Password")
                if submit:
                    if title and password:
                        save_password(title, password)
                        st.success("Password saved successfully!")
                    else:
                        st.error("Please fill in both fields.")

            # Display saved passwords
            st.write("### Saved Passwords")
            saved_passwords = load_passwords()
            if saved_passwords:
                df = pd.DataFrame(list(saved_passwords.items()), columns=["Title", "Password"])
                st.dataframe(df)
            else:
                st.info("No passwords saved yet.")

            
    if st.session_state.current_page != "main":
                if st.button("Go Back"):
                    st.session_state.current_page = "main"
        
            

            
