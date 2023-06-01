# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek




st.title('brute-force attacks')

col1, col2 = st.columns(2)
with col1:
    st.write('Eine Brute-Force-Attacke ist eine Methode, bei der ein Hacker automatisch eine große Anzahl von Passwörtern oder anderen Zugangsdaten ausprobiert, um Zugang zu einem gesicherten System oder einer geschützten Datei zu erlangen. Dabei werden typischerweise einfache, leicht zu erratende Passwörter als erste ausprobiert. Ziel der Attacke ist es, durch Ausprobieren aller möglichen Kombinationen ein gültiges Passwort zu erraten oder zu entschlüsseln, um das System zu kompromittieren oder auf Daten zuzugreifen, auf die der Hacker normalerweise keinen Zugriff hat. Die Brute-Force-Attacke ist eine weit verbreitete Methode bei Cyberangriffen und wird durch die Verwendung von starken Passwörtern und anderen Sicherheitsmaßnahmen erschwert.')
with col2:
    st.image('https://www.it-daily.net/images/Aufmacher-2019/Security-Identity_1565644603-700.jpg', width=None)

col1, col2, col3, col4 = st.columns(4)

topic = 0

with col1:
    st.header('dicnoary Angriff')
    if st.button('1'):
        topic = 1
        st.write('Why hello there')
    else:
        st.write('Goodby')
        
with col2:
    st.header('credential stuffing')
    if st.button('2'):
        topic = 2
        st.write('Why hello there')
    else:
        st.write('Goodbye')

with col3:
    st.header('hybrid brute force attack')
    if st.button('3'):
        topic = 3
        st.write('Why hello there')
    else:
        st.write('bye')

with col4:
    st.header('traditional brute force attack')
    if st.button('4'):
        topic = 4
        st.write('Why hello there')
    else:
        st.write('Goodbye')

if topic == 0:
    st.write('0')
if topic == 1:
    st.write('1')
if topic == 2:
    st.write('2')
if topic == 3:
    st.write('3')
if topic == 4:
    st.write('4')

st.header ('Dies passiert während einer brute force attack')
