import streamlit as st # streamlit #
import base64 # HTML #
# tittle #
st.title('GALAXY')
# search bar command #
def searchbar():
    save = st.text_input('SEARCH FOR PLANETS IN OUR SOLAR SYSTEM')
    q = st.button('search')
    if q:
        if save == 'sun':
            # Path to your PDF
            pdf_path = r"python/vidoes/SUN.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
        elif save == 'earth':
            # Path to your PDF
            pdf_path = r"python/vidoes/EARTH.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
        elif save == 'mars':
            # Path to your PDF
            pdf_path = r"python/vidoes/mars.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
        elif save == 'jupiter':
            # Path to your PDF
            pdf_path = r"python/vidoes/jupiter.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('SORRY FOR EXTRA PAGE')
            st.write('scroll down')
        elif save == 'mercury':
            # Path to your PDF
            pdf_path = r"python/vidoes/mercury.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
        elif save == 'venus':
            # Path to your PDF
            pdf_path = r"python/vidoes/venus.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('SORRY FOR EXTRA PAGE')
            st.write('scroll up')
        elif save == 'saturn':
            # Path to your PDF
            pdf_path = r"python/vidoes/saturn.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
        elif save == 'neptune':
            # Path to your PDF
            pdf_path = r"python/vidoes/neptune.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
        elif save == 'uranus':
            # Path to your PDF
            pdf_path = r"python/vidoes/uranus.pdf"

            # Open and read PDF file as bytes
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Embedding PDF into the HTML
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

            # Show PDF in Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.write('scroll down')
searchbar()
# solar system images and labels #
st.divider()
st.header('SOLAR SYSTEM')
st.divider()
st.image("python/images/solarsystem.png")
st.divider()
st.header('PLANTS')
st.divider()
# earth #
col1, col2 = st.columns(2)
with col1:
    st.image("python/images/earth.png")
with col2:
    st.subheader('EARTH:')
    st.write('''Earth is the third planet from the Sun in our solar system.
                It is the only known planet to support life.
                About 71% of Earth's surface is covered by water.
                It has a protective atmosphere that sustains life and shields from harmful radiation.
                Earth rotates on its axis, causing day and night.
    ''')
    st.markdown(r'<a href="vidoes/EARTH.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# sun #
wan1, wan2 = st.columns(2)
with wan1:
    st.image("python/images/sun.png")
with wan2:
    st.subheader('SUN:')
    st.write('''The Sun is a massive ball of hot gases at the center of our solar system.
              It provides light and heat essential for life on Earth.
              The Sun is mostly made of hydrogen and helium.
              Its gravity keeps the planets in orbit around it.
              It is about 4.6 billion years old and will shine for billions more.
    ''')
    st.markdown(r'<a href="vidoes/SUN.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# mars #
san1, san2 = st.columns(2)
with san1:
    st.image("python/images/mars.png")
with san2:
    st.subheader('MARS:')
    st.write('''Mars is the fourth planet from the Sun in our solar system.
                It is known as the "Red Planet" due to its reddish surface.
                Mars has the largest volcano and canyon in the solar system.
                It has seasons, polar ice caps, and dust storms.
                Scientists believe Mars may have once had liquid water and could support life.
    ''')
    st.markdown(r'<a href="vidoes/mars.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# jupiter #
tan1, tan2 = st.columns(2)
with tan1:
    st.image(r'python/images/neptune.png')
with tan2:
    st.subheader('JUPITER:')
    st.write('''Jupiter is the fifth planet from the Sun and the largest in our solar system.
                It is a gas giant made mostly of hydrogen and helium.
                Jupiter has a Great Red Spot, a massive storm larger than Earth.
                It has at least 79 moons, including the large moon Ganymede.
                Its strong magnetic field and fast rotation make it unique among the planets.
    ''')
    st.markdown(r'<a href="vidoes/jupiter.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# saturn #
zan1, zan2 = st.columns(2)
with zan1:
    st.image(r'python/images/saturn.png')
with zan2:
    st.subheader('SATURN:')
    st.write('''Saturn is the sixth planet from the Sun and the second-largest in our solar system.
                It is best known for its stunning rings made of ice and rock.
                Saturn is a gas giant, mostly composed of hydrogen and helium.
                It has over 80 moons, including Titan, which has a thick atmosphere.
                Despite its size, Saturn is the least dense planet—it could float in water!
    ''')
    st.markdown(r'<a href="vidoes/saturn.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# neptune #
qan1, qan2 = st.columns(2)
with qan1:
    st.image('python/images/jupiter.png')
with qan2:
    st.subheader('NEPTUNE:')
    st.write('''Neptune is the eighth and farthest planet from the Sun in our solar system.
                It is a cold, blue gas giant known for its strong winds and storms.
                Neptune has a thick atmosphere made of hydrogen, helium, and methane.
                It has 14 known moons, with Triton being the largest.
                A day on Neptune lasts about 16 hours, and a year takes 165 Earth years.
    ''')
    st.markdown(r'<a href="vidoes/neptune.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# uranus #
yan1, yan2 = st.columns(2)
with yan1:
    st.image(r'python/images/theman.png')
with yan2:
    st.subheader('URANUS:')
    st.write('''Uranus is the seventh planet from the Sun in our solar system.
                It is a gas giant with a bluish color due to methane in its atmosphere.
                Uranus rotates on its side, making its axis almost horizontal.
                It has faint rings and at least 27 known moons.
                Uranus is one of the coldest planets, with extreme temperatures and strong winds.
    ''')
    st.markdown(r'<a href="vidoes/uranus.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# venus #
han1, han2 = st.columns(2)
with han1:
    st.image(r'python/images/venus.png')
with han2:
    st.subheader('VENUS:')
    st.write('''Venus is the second planet from the Sun and is similar in size to Earth.
                It has a thick, toxic atmosphere rich in carbon dioxide.
                Venus is the hottest planet due to a strong greenhouse effect.
                It rotates very slowly and in the opposite direction of most planets.
                Venus is often called the "morning star" or "evening star" because of its bright appearance.
    ''')
    st.markdown(r'<a href="vidoes/venus.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# mercury #
mang1, mang2 = st.columns(2)
with mang1:
    st.image(r'python/images/mercury.png')
with mang2:
    st.subheader('MERCURY:')
    st.write('''Mercury is the closest planet to the Sun and the smallest in our solar system.
                It has a rocky surface covered with craters, similar to the Moon.
                Mercury has no atmosphere to retain heat, causing extreme temperature changes.
                A day on Mercury is longer than its year.
                Despite being close to the Sun, it's not the hottest planet—Venus is.
    ''')
    st.markdown(r'<a href="vidoes/mercury.pdf" target="_blank">Download PDF</a>', unsafe_allow_html=True)
# thanks for visiting #
st.header('thanks for visiting')
# like button and like icon #
can1, can2 = st.columns(2)
with can1:
    x = st.button('like')
with can2:
    st.markdown("👍 **like**")
# unlike button and unlike icon #
han1, han2 = st.columns(2)
with han1:
    y = st.button('unlike')
with han2:
    st.markdown("👎 **unlike**")
# like and unlike button commands #
if x:
    st.balloons()
    st.success('thank you')
    st.markdown("👍 **Good Hand**")
if y:
    st.error('sorry')
    st.markdown("😞 👎 **Sorry**")



