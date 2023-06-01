# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek
from helper_dark_patterns import Helper # Lade Helfer-Klasse aus helper.py

h = Helper(100) # Erstelle Helfer-Objekt

st.title('Dark Patterns') 

if 'first_run' not in st.session_state:     # Setze session state "first_run" bei erster Ausführung

    st.session_state['first_run'] = True    # Ändere session state "first run" mit dem Klick eines Buttons
    if st.session_state.first_run:    
     st.write ('Cookies sind noch nicht akzeptiert.')
     if st.button('akzeptiere die Cookies'):
         st.session_state['first_run'] = False  # Verwende session state "first run"




else:
    
    st.write ('alle Cookies sind akzeptiert')
   
    genre = st.radio(
        'Wähle ein Thema',
        ('Dark Patterns', 'Cookie-Banner', 'Preselection')) 
        # Erstelle einen Multiselekt
    
    if genre == 'Dark Patterns':
        st.write ('Was sind Dark Patterns?')
        st.write ("Dark Patterns sind Benutzeroberflächen, die Benutzer*innen dazu bringen etwas zu tun, dass sie ursprünglich nicht beapsichtigt haben. Somit werden Benutzer*innen gegen ihren Willen ausgenutzt. Die Preselection und das Cookie-Banner sind 2 Arten davon.")
        
    elif genre == 'Preselection':
        st.image('https://dapde.de/media/images/210329_dapde_DE_Preselection_ZvWjgJD.max-800x600.png')
        st.write ('Was ist Preselection?')
        st.write ('Preselcetion ist ein Dark Pattern aus der Gruppe der Hindernisse. Diese Gruppe beabsichtigt, Benutzer*innen von gewissen Handlungen abzuhalten. Bei der Preselection wird von dem Ersteller der Webseite eine gewisse, abänderbare Vorauswahl getroffen um Benutzer*innen zu beeinflussen.')
    else:
        st.write ('was ist ein Cookie-Banner?')
        st.image ('https://blog.didomi.io/hs-fs/hubfs/Imported_Blog_Media/2_Deezer-1024x485.png?width=1536&height=728&name=2_Deezer-1024x485.png')
        st.write ('Die Cookie-Banner speichern Informationen über den Nutzer, sobald man sie akzeptiert. Vom Cookie-Banner gibt es 2 Arten')
        st.write ('1. Man kann sie Akzeptieren und die Einstellungen ändern, wobei das Akzeptieren meist durch Farben hervorgehoben ist. Wenn man dann trotzdem auf die Einstellungen tippen will, sind sie zu überfüllt und man weiss dann nicht, was man ändern müsste.') 
        st.write ('2. Man kann nur entweder akzeptieren oder nur ablehnen. Diese bieten aber nicht alle Webseiten an.')

   
   
    

