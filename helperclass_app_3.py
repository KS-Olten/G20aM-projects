import streamlit as st # importiere streamlit funktionalitäten

# die nächsten 4 Listen beinhalten die Zeichen auf die geprüft werden
sonderzeichen=["!", "#", "$", "%", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "=", "?", "@", "[", "]", "^", "_", "{", "|", "}", "~"]
grossbuchstaben=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
kleinbuchstaben=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
zahlen=["0","1","2","3","4","5","6","7","8","9"]



class Helper: # definiert die Helperclass

    def __init__(self,password): 
        self.password=password #setzt self.password als das eingegeben Passwort ein
        

    def checker(self): #der Passwortprüfer an sich
        if len(self.password) == 0: #überprüft ob überhaupt etwas eingegeben wurde
            st.markdown("") # lässt noch den Platz unter dem Passworteingabefeld am Anfang noch leer erscheinen
        else:

            if len(self.password) < 8: #überprüft die Passwortlänge
                st.markdown ("❌ :red[Ihr Passwort sollte mindestens 8 Zeichen lang sein...]🔓") #gibt dies aus wenn es zu kurz ist
            elif len(self.password)>=12:
                st.markdown("✅ :green[Gut, Ihr Passwort verfügt über die empfohlene Länge von 12 Zeichen.]🔒") #dies wenn es länger als 12 Zeichen lange ist
            else: 
                st.markdown("〰️ :orange[Ihr Passwort verfügt über 8-12 Zeichen. Dies ist zwar gut, empfohlen würde aber mindesten 12 Zeichen zu haben]") #und dies wenn es im Graubereich zwischen 8 und 12 Zeichen lange ist
        
            liste=list(self.password) #setzt jedes Zeichen des eingegebenen Passworts als einzelnes Element in eine Liste (in App_3 defininiert)

            liste_checker_sonderzeichen=set(liste) & set(sonderzeichen) #sucht nach Übereinstimmungen des Passworts und der Gesamtliste der Sonderzeichen und fügt es in eine neue, leere Liste (in App_3 definiert)
            if len(liste_checker_sonderzeichen)<1: #schaut ob die Liste mit den Übereinstimmungen mindestens ein Elemt erhält (also ob es Übereinstimmungen gibt)
                st.markdown("❌ :red[Ihr Passwort sollte mindestens ein Sonderzeichen enthalten...]🔓") #gibt dies aus wenn es keine Übereinstimmungen gibt, das Passwort also keine Sonderzeichen enthält
            else:
                st.markdown ("✅ :green[Gut, Ihr Passwort verfügt über mindestens ein Sonderzeichen.]🔒") #gibt dies aus wenn es Übereinstimmungen gibt, das Passwort also mindestens ein Sonderzeichen enthält.
            # das selbe wie bei den Sonderzeichen passiert nun auch für Grossbuchstaben, Kleinbuchstaben und Zahlen
            liste_checker_grossbuchstaben=set(liste) & set(grossbuchstaben)
            if len(liste_checker_grossbuchstaben)>0:
                st.markdown ("✅ :green[Gut, Ihr Passwort verfügt über mindestens einen Grossbuchstaben.]🔒")
            else:
                st.markdown("❌ :red[Ihr Passwort sollte mindestens einen Grossbuchstaben enthalten...]🔓")

            liste_checker_kleinbuchstaben=set(liste) & set(kleinbuchstaben)
            if len(liste_checker_kleinbuchstaben)>0:
                st.markdown("✅ :green[Gut, Ihr Passwort verfügt über mindestens einen Kleinbuchstaben.]🔒")
            else:
                st.markdown("❌ :red[Ihr Passwort sollte mindestens einen Kleinbuchstaben enthalten...]🔓")

            liste_checker_zahlen=set(liste) & set(zahlen)
            if len(liste_checker_zahlen)>0:
                st.markdown("✅ :green[Gut, Ihr Passwort verfügt über mindestens eine Zahl.]🔒")
            else:
                st.markdown("❌ :red[Ihr Passwort sollte mindestens eine Zahl enthalten...]🔓")

