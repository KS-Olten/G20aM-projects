# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek
from helper_collaborative_filtering import Helper 

# Erstellen des Webseitentitels
st.title('Collaborative Filtering')
# Erstellen eines Headers
st.header('Theorie')

#Button, der die Definiton anzeigt, wenn man ihn anklickt
if st.button("Definition"): 
    st.image("Bild.jpg")
    st.write("Collaborative Filtering ist ein Algorithmus in der Kategorie der Empfehlungssysteme, welcher das Ziel hat möglichst genaue Empfehlungen von Objekten an dessen NutzerIn weiterzugeben. Die Idee ist, dass viele andere NutzerInnen ähnliche Interessen und Vorlieben haben und deren Daten genutzt werden, um einen passgenauen Vorschlag für eine einzelne Person abzugeben. Der Algorithmus geht davon aus, dass BenutzerInnen ähnliche Entscheidungen, die in der Vergangenheit getroffen wurden, auch in der Zukunft treffen. Durch die Verwendung deren Daten und verschiedenen Algorithmen und statistischen Methoden, wird ein Vorschlag generiert, der auf Analysen von Verhalten und Entscheidung anderen NutzerInnen basiert. So kann man vom Verhalten anderer Personen lernen und eine realitätsnahe Empfehlung abgeben. ") 


#Button, der die Beispiele anzeigt, wenn man ihn anklickt
if st.button("Beispiele"): 

    st.write("Einfache Beispiele, bei denen Collaborative Filtering verwendet wird:")
    st.write("- Musikempfehlung bei Spotify oder Apple Music")
    st.write("- Freundschaftsvorschläge bei Instagram und Facebook")
    st.write("- Personalisierte Produktempfehlung bei Amazon")
    st.write("- Videoempfehlung bei Netflix") 
# Erstellen eines Headers
st.header("Übung")
# Aufgabenstellung in Form von Text hinzufügen
st.write("In dieser Übung sehen Sie, wie ihre Empfehlung aufgrund Ihrer ausgewählten Hobbies angepasst wird. Je nach dem mit welchem Verhaltensmuster (von zwei vorprogrammierten UserInnen) Ihre Auswahl am ehesten übereinstimmt, erscheint ein anderer Vorschlag. ")



#multi select box; Nutzer*in hat verschiedene Optionen zur Auswahl
hobbies = st.multiselect("Hobbies:",
                         ['Tanzen', 'Instrument', 'Hobbylos', 'Sport', 'Singen', 'Essen'])



#Erstellen von zwei User*innen in Form von Listen

pref_1=['Tanzen', 'Sport', 'Singen', 'Yoga' ]
pref_2=['Instrument', 'Hobbylos', 'Essen','Zeichnen']



#Erstellen von zwei Listen, welche Übereinstimmungen von hobbies und pref_1 & pref_2 überprüfen und zusammenfassen.
score_1 = set(hobbies) & set(pref_1)
score_2 = set(hobbies) & set(pref_2)
# Erstellen von zwei Scores, welche die Länge der obrigen Listen enthalten.
score1= len(score_1)
score2= len(score_2)

# Erstellen des Helper-Objekts
rechner= Helper(score1, score2)
# Startet Funktion
rechner.ausrechner()
# Gibt Hobbies der 2 UserInnen an
st.write("UserIn 1: Tanzen, Sport, Singen, Yoga")
st.write("UserIn 2: Instrument, Hobbylos, Essen, Zeichnen ")