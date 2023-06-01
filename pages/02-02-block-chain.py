# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade Streamlit Bibliothek


# Schreibe einen Titel
st.title("Blockchain")

# Erstelle einen Subheader
st.subheader('Theorie')

# Erstelle einen Button, welcher ein Theorieteil enthält
if(st.button("Was ist eine Blockchain")):
    st.subheader('Was ist eine Blockchain?')
    with st.container():
        st.write("Eine Blockchain ist eine Sammlung an Daten, also eine Datenbank. Der Sinn dahinter ist, dass sie aus verschiedenen Blöcken besteht. Es können immer neue Blöcke angehängt werden. Diese werden allerdings nur angehängt, wenn sie überprüft und bestätigt werden. Da diese Blockchains auf vielen Computer weltweit abgespeichert werden, kann man nicht einfach etwas Falsches abspeichern, respektiv fällt das nachher auf, weil alle anderen etwas anderes haben. Was ebenfalls für die Sicherheit sorgt, ist dass jegliche Blocks sogenannte Hashs, Nummern, besitzen, durch die es nur eine Ordnung geben kann. Diese Aspekte machen Blockchains so sicher, ebenfalls zentral ist dabei, dass die Sicherheit nicht über Dritte laufen muss. Dies erhöht die Sicherheit nochmals gegen Betrug. Die negativen Aspekte des Blockchain-Systems sind der unnatürlich hohe Stromverbrauch, der das Ganze erzeugt, um die Hashs zu ermitteln. Ebenfalls benötigt es sehr viel Speicherplatz. Heute werden Blockchains in internationalen Finanztransaktionen verwendet. Die Kryptowährungen, die immer mehr an Bedeutung gewinnen, funktionieren als Blockchain")

# Erstelle einen Button, welcher ein Theorieteil und ein Foto enthält
if(st.button("Wie ist eine Blockchain aufgebaut")):
    st.subheader('Wie ist eine Blockchain aufgebaut?')
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.write("Eine Blockchain besteht 3 verschiedenen Elementen. Erstens die Daten, welche vermittelt werden sollen. Zweitens einen Hash. Ein Hash funktioniert wie ein digitaler Fingerabdruck, jeder Hash ist einzigartig. Das dritte Element ist der Hash des vorherigen Blocks. Durch dieses Prinzip kann eine Kette (Chain) gebildet werden. Ein Block kann nur drangehängt werden, wenn der Hash mit dem vorhergehenden Hash übereinstimmt. Um ein Block an die Kette zuhängen, muss zuerst ein Miner die Daten überprüfen. Damit das gelingt, ermitteln sie eine passende Zufallszahl, eine sogenannte Nonce. Ist dies gelungen, wird der Block an die angehängt")
    with col2:
        st.image('Aufbau.jpg')

# Erstelle einen Sunheader
st.subheader('Übung')

# Setze session state "first_run" bei erster Ausführung
if 'exercise' not in st.session_state:
    st.session_state['exercise'] = False

# Verwende session state "first run"
if st.button('Übung'):
    st.session_state['exercise'] = True

# Erstelle ein Genre mit 5 Antwortmöglichkeiten
if st.session_state['exercise']:
    genre = st.radio("Wählen Sie die falsche Blockchain aus", ('Wählen Sie aus','1', '2', '3', '4'))
    if genre == '2':
        st.success('Die Antwort ist richtig')
    elif genre == 'Wählen Sie aus':
        st.warning('Wählen Sie aus')
    else:
        st.error('Die Antwort ist falsch')
# Erstelle columns
    col1, col2 = st.columns(2)
    with col1:
        st.write("1)")
        st.image('col2.jpg')
    with col2:
        st.write("2)")
        st.image('col1.jpg')
    col1, col2 = st.columns(2)
    with col1:
        st.write("3)")
        st.image('col3.jpg')
    with col2:
        st.write("4)")
        st.image('col4.jpg')


    
