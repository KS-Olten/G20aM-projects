# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek

elemente = ['Biene','Eis','Eifersucht','Frühling','Gummiboot','basteln','Sommersprossen'] #Erstelle Liste mit Elementen 

st.title('Kollisionen') #Titel
st.header('Was sind Hashtabellen?')#subtitel
st.text('''Als Hashverfahren wird ein Algorithmus bezeichnet, der dazu dient Datenobjekte
in grossen Datenmengen zu suchen. Es gibt eine Hashfunktion, die dazu dient, 
die Position eines Objektes in einer Tabelle zu berechnen. Die Zieldaten 
werden in einer Hashtabelle gespeichert. Um die Datenobjekte eindeutig zu 
identifizieren, gibt es einen Hashwert, welcher als Index dient. Dieser
wird von einer Hashfunktion aus einem Schlüssel berechnet. Der Speicherort 
eines Datenobjekts, der durch den Hashwert festgelegt wird, wird 
als Bucket bezeichnet. ''')#Erklärungstext zu Hashtabellen
st.header('Was sind Kollisionen?')#subtitel
st.text('''Im Idealfall hat jedes Objekt einen eigenen Bucket. Jedoch sind Hashfunktionen 
im Allgemeinen nicht eindeutig, somit können zwei verschiedene Schlüssel 
zum selben Hashwert,also zum selben Bucket führen. Dieses Ereignis wird 
als Kollision bezeichnet. In diesem Fall werden mehrere Werte in einem 
Bucket aufgenommen. Um das Kollisions-Problem zu bewältigen, gibt es 
verschiedene Kollisionsauflösungsstrategien.
Die untenstehende Grafik zeigt ein Beispiel für eine Hashtabelle, wobei 
der rote Pfeil eine Kollision darstellt. ''')#Erklärungstext zu Kollisionen

st.image('Hashtabelle.png')#Bild Hashtabelle einfügen

element = st.text_input('') #Eingabe eigenes Element
st.button('Hinzufügen') #Hinzufügebutton


col1, col2 = st.columns(2)#2 Spalten erstellen

with col1:#Was in die erste Spalte geschrieben wird
   st.subheader('Element') #Spaltentitel
   st.write(str(element))#eigenes Element
   for e in elemente:
       st.write(str(e))#Elemente aus Liste in diese Spalte schreiben
       if len(str(element))==len(str(e)):
           st.markdown(':red[! Kollision !]')#Wenn es eine Kollision gibt: rot Kollision schreiben


with col2:#Was in die zweite Spalte geschrieben wird
   st.subheader('Hashwert')# Spaltentitel
   st.write(len(str(element)))#Hashwert(=Wortlänge) des eigenen Elements schreiben
   for e in elemente:
       st.write(len(str(e)))# Hashwerte aller Elemente der Liste schreiben
       if len(str(element))==len(str(e)):
           st.markdown(':red['+str(len(str(e)))+']')#Wenn es eine Kollision gibt rot den Hashwert schreiben
       
      

