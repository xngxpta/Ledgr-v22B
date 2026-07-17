import pandas as pd
import os
import streamlit as st
#from st_paywall import add_auth
#from streamlit_option_menu import option_menu
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from matplotlib import style
# from auth.session import init_session, login_user
# from auth.google_auth import get_google_login
# from auth.stripe_gate import check_subscription
import streamlit_authenticator as stauth
# from auth.session import init_session

# init_session()

import streamlit.components.v1 as components

GA_ID = "G-4MRDCEFGB4"

gtag_html = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
"""
# Embed the script
components.html(gtag_html, height=0)

##################################################################
direc = os.getcwd()

logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/',
        icon_image=logofile)
# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin = f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
url_ytube = "https://www.youtube.com/@LedgrInc"
url_fbook = "https://www.facebook.com/share/1BnXaYvRzV/"
url_insta = 'https://www.instagram.com/alphaledgr/'
url_blog = 'https://www.alphaledgr.com/Blog'
url_linkedin = "https://www.linkedin.com/company/ledgrapp/"
url_stripe = "https://buy.stripe.com/6oU28t21Y2NmbfjdkK0480h"
url_stripe_2 = "https://buy.stripe.com/dR64iacsh6bx9zi5kk"
st.sidebar.link_button("Join Us!", url_stripe_2, type="primary",
                       disabled=False, use_container_width=True)
st.markdown(
            '''
            <div align="center">
            <h3>Learn how to get started on the platform!
            See below for details..</h3></div>''',
            unsafe_allow_html=True)
# st.write(f'{username} Welcome!')
vid_url = "https://youtu.be/FzNTs9QMNR0?si=p0i0GzCSGjRmZgaH"
st.video(vid_url)
with st.container():
    a1, a2a, a2, a3 = st.columns([1, 1, 4, 1])
    with a1:
        st.image(f'{direc}/pages/appdata/imgs/LedgrBase.svg',
                 caption='Your Unified Wealth Dashboard')
    with a2a:
        st.write(" ")
    with a2:
        st.subheader("Part I: Ledgrbase")
        st.write("Map your existing asset holdings and portfolios.")
        st.write("Review and note their overall performance till date.")
        st.subheader("Part II: MarketBoard")
        st.write("Calculate Returns from SIPs, Explore ETFs and Mutual Funds.")
    with a3:
        st.image(f'{direc}/pages/appdata/imgs/MarketBoard.png',
                 caption='Market Profiles, Plots and Instruments')
st.write("-------------------------------------------------------------------")
with st.container():
    c1, c2a, c2 = st.columns([1, 1, 3])
    with c1:
        st.image(f'{direc}/pages/appdata/imgs/AnalyticsBox.png',
                 caption='Analytics and Information')
    with c2a:
        st.write(" ")
    with c2:
        st.subheader("AnalyticsBox")
        st.write("Analyze a Security In-Depth. Visualize Metrics & Indicators")
        st.write("Gather comprehensive knowhow on a selected Security.")
st.write("-------------------------------------------------------------------")
with st.container():
    d1, d2a, d2 = st.columns([3, 1, 1])
    with d1:
        st.subheader("InvestmentLab")
        st.write("Optimize Investment Allocations.")
        st.write("Generate Efficient Portfolios to Maximize Returns.")
        st.write("""Input assets and amount to proceed.""")
        st.write("""Select any from 5 Optimized portfolios presented.""")

    with d2a:
        st.write(" ")
    with d2:
        st.image(f'{direc}/pages/appdata/imgs/InvestmentLab.png',
                 caption='Generate Optimal Portfolios')


st.write("-------------------------------------------------------------------")


with st.container():
    column1, column2, column3, column4, column5 = st.columns([1, 1, 1, 2, 1])
    with column1:
        st.image(ytube, "[Ledgr\'s YouTube Channel](%s)" % url_ytube, width=60)
    with column2:
        st.image(fbook, "[Ledgr\'s FaceBook Page ](%s)" % url_fbook, width=60)
    with column3:
        st.image(linkedin, '[Our LinkedIn Page ](%s)' % url_linkedin, width=60)
    with column4:
        st.write(" ")
        st.image(ledgrblog,  "[Ledgr\'s Blog ](%s)" % url_blog)
        st.write(" ")
    with column5:
        st.image(insta,  "[Ledgr\'s @ Instagram ](%s)" % url_insta, width=60)
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([1, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.caption(""":|2025 - 2026|All Rights Resrved © Ledgr Inc.|alphaLedgr:
                   """)
    with f11:
        st.write(" ")
