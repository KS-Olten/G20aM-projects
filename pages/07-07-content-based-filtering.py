from http import HTTPStatus
import streamlit as st

st.header('Content based filtering by Åsa and Alena')

# Definition des Themas
st.title('Was ist Content based filtering?')
st.write('Mit Hilfe von Content-Based Filtering (dt. Inhaltsbasiertes Filtern) werden dem User einer Applikation oder eines Internetdienstes Inhalte empfohlen, die ihn interessieren könnten. Diese Inhalte werden anhand der zuvor konsumierten Beiträge gefiltert. Massgebende Faktoren sind beispielsweise Suchanfragen, Likes, Downloads, Lesezeichen, Anschauungsdauer, Onlinekäufe etc. So erhält der Nutzer auf ihn zugeschnittene Beiträge, welche ihm die Suche nach Information erleichtern.')

st.write('Ein zu beachtendes Risiko bei dieser Informationssuche ist die sogenannte Filterblase. Die von Eli Pariser geprägte «Filterbubble» kritisiert die Einseitigkeit, der durch Algorithmen personenspezifisch gefilterten Beiträge und Artikel durch welche hauptsächlich die eigene Meinung bestärkt wird. Eine Konfrontation mit einer Gegenmeinung oder einer anderen Weltanschauung findet so kaum statt. Auf Grund dessen ist es möglich, das politische Extreme dazu tendieren weiter und weiter auseinander zu driften, weil der Teil ihrer Realität, der sich im Netz befindet, sich nicht überschneidet. Sie leben also ein bisschen in einem Paralleluniversum, was das Netz betrifft.')

# Erklärung vom Quiz
st.title('So könnte das aussehen!')
st.write('Der Fragebogen unten soll das Prinzip von Content-Based Filtering noch etwas veranschaulichen. Anhand der Antworten, die du wählst, wird dir ein zu deiner Stimmung passender Song vorgeschlagen.')

#Der User hat 3 verschiedene Elemente. Am Anfang sind alle auf Null gestellt. 
class User:
    def __init__(self):
        self.happy = 0
        self.balanced = 0
        self.thoughtful = 0
    
    #Je nachdem, wie eine Frage vom Nutzer beantwortet wird, addieren sich die Punkte zur jeweilige Gefühlslage, am Schluss wird je nach höchstem Score 
    def frage(self, question, options):
        answer = st.radio(question, options)
        if answer == options[0]:
            self.happy += 1
        elif answer == options[1]:
            self.balanced += 1
        elif answer == options[2]:
            self.thoughtful += 1

#Hier sind die Fragen mit Antworten aufgelistet:
user = User()
user.frage("Was machst du, wenn frühmorgens dein Wecker klingelt?", ["Der frühe Vogel fängt den Wurm, ich bin schon seit dem ersten Vogelzwitschern wach.", "Ein kleiner Druck auf die Snooze-Taste hat noch niemandem geschadet.", "Wecker? Welcher Wecker? Ich habe nichts gehört!"])
user.frage("Gerade jetzt läuft im Radio dein Lieblingslied, wie reagierst du?", ["Ich drehe die Lautstärke auf, singe mit und wirble durch den Raum.", "Ich wippe dezent mit der Musik mit.", "Gerade jetzt passt schlecht, ich bin nicht so in Tanzstimmung."])
user.frage(" Hast du Hunger?", ["Nein, momentan bin ich versorgt.", "Zu etwas Kleinem zum Knuspern sage ich nie nein.", "Ja OMG, ich sterbe fast vor Hunger!"])
user.frage("Hattest du heute schon die Gelegenheit etwas Sport zu treiben und dich auszutoben?", ["Ja, ich liebe es herumzuturnen!", "Ein kleines Bisschen, der Kantihügel hat mich heute schon ins Schwitzen gebracht.", "Sport ist Mord! Ich bin doch nicht lebensmüde…"])
user.frage("Wärst du bei einem kleinen Waldspaziergang dabei?", ["Aber sicher, ab ins Grüne!", "Waldspaziergang? Ich weiss nicht, wie ist das Wetter momentan?", "Uii nein, Natur ist nichts für mich..."])
user.frage("Was für eine Farbe hat dein Oberteil gerade jetzt?", [" Mein Oberteil hat eine warme Farbe (rot, orange, gelb etc.)", "Mein Oberteil hat eine kühle Farbe (blau, grün, lila etc.)", "Mein Oberteil hat eine dunkle Farbe (schwarz, dunkelblau etc.)"])
user.frage("Für was gibst du dein Geld am meisten aus?", ["Ferien! Ich liebe es Erfahrungen zu sammeln!", "Ich spare für meine Zukunft! Geld gebe ich nur fürs Wichtigste aus.", "Kleider, Bücher, Essen, Schmuck, Schuhe ... Was mir gerade freude bereitet!"])
user.frage("Was wünschst du dir auf deinen Geburtstag? ", ["Nichts, Hauptsache meine Freunde & Familie sind gesund.", "Ich bin mir noch nicht sicher, ich denke noch darüber nach…", "Oh, wo soll ich anfangen…?"])
user.frage("Hast du heute schon Gemüse oder eine Frucht gegessen?", ["Ja sicher, ich liebe Grünzeug!", "Heute noch nicht, bin noch nicht dazu gekommen…", "Mir schmeckt Gemüse nicht. "])
user.frage("Fühlst du dich einsam?", ["Nein, ich bin immer von Menschen mit einem offenen Ohr für mich umgeben.", "Zwischendurch schon, aber ich habe Freunde, an die ich mich wenden kann.", "Ja, mir fehlt eine Person, der ich mich anvertrauen kann. "])

# Mit moods wird die Gefühlslage mit den meisten Punkten bestimmt. Diese ist nun im Programm als best_mood bekannt.
moods = {
    "glücklich": user.happy,
    "ausgeglichen": user.balanced,
    "nachdenklich": user.thoughtful
}
best_mood = max(moods, key=moods.get)

# Je nach dem mood des Users wird in der Funktion best_mood ein anderer Song mit Begleittext ausgegeben.
# Hier Unten sind die Begleittexte und Songs angegeben
if best_mood == "glücklich":
    st.title("Dein Song ist Boogie Wonderland von Earth, Wind and Fire")
    st.write("Du bist momentan glücklich. Deine Gefühlslage könnte das Lied Wonderland von Earth, Wind & Fire passend untermalen.")
    st.video('https://www.youtube.com/watch?v=god7hAPv8f0')

elif best_mood == "ausgeglichen":
    st.title("Dein Song ist Belong in the Sun von Teo")
    st.write("Du bist momentan eher ausgeglichen. Deine Gefühlslage könnte das Lied Belong in the Sun von ¿Teo? passend untermalen.")
    st.video('https://www.youtube.com/watch?v=DZ8s-aU3EXA')

else:
    st.title("Dein Song ist Moody Wind von Anthony Lazaro")
    st.write("Du bist momentan eher nachdenklichen gestimmt. Deine Gefühlslage könnte das Lied Moody Wind von Anthony Lazaro passend untermalen.")
    st.video('https://www.youtube.com/watch?v=XmacSVTzW7E')