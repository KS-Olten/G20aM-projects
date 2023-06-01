
import streamlit as st # Lade streamlit Bibliothek

class Helper:
    def __init__(self,skore1,skore2):
        self.Skore1=skore1
        self.Skore2=skore2
        
    def ausrechner(self):
        if self.Skore1<1 and self.Skore2<1:
            st.write("")
        else:
            if self.Skore1 > self.Skore2:
                st.write("Aufgrund Ihrer Auswahl ist Ihr Verhaltensmuster dem von UserIn 1 am ähnlichsten. Vielleicht würde Ihnen Yoga noch Spass machen.")
            elif self.Skore1 < self.Skore2:
                st.write("Aufgrund Ihrer Auswahl ist Ihr Verhaltensmuster dem von UserIn 2 am ähnlichsten. Vielleicht würde Ihnen Zeichnen noch Spass machen. ")
            else:
                st.write("Ihre Auswahl und somit auch Ihr Verhaltensmuster passt zu den Verhaltensmustern von Userin 1 und UserIn 2. Vielleicht würde Ihnen Zeichnen und/oder Yoga noch Spass machen.")