# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek



# Haupttitel der Website
st.markdown('<h1 style="text-align: center;">BRUTE-FORCE ATTACKS</h1>', unsafe_allow_html=True)

#Thementrenner
st.write("---") 

#Einführung Brute-force Attacken
col1, col2 = st.columns(2)
#Text
with col1:
    st.write('Eine Brute-Force-Attacke ist eine Methode, bei der ein Hacker automatisch eine große Anzahl von Passwörtern oder anderen Zugangsdaten ausprobiert, um Zugang zu einem gesicherten System oder einer geschützten Datei zu erlangen. Dabei werden typischerweise einfache, leicht zu erratende Passwörter als erste ausprobiert. Ziel der Attacke ist es, durch Ausprobieren aller möglichen Kombinationen ein gültiges Passwort zu erraten oder zu entschlüsseln, um das System zu kompromittieren oder auf Daten zuzugreifen, auf die der Hacker normalerweise keinen Zugriff hat. Die Brute-Force-Attacke ist eine weit verbreitete Methode bei Cyberangriffen und wird durch die Verwendung von starken Passwörtern und anderen Sicherheitsmaßnahmen erschwert. Es gibt verschiedene Methoden ein Passwort zu hacken:')
#Bild
with col2:
    st.image('https://www.it-daily.net/images/Aufmacher-2019/Security-Identity_1565644603-700.jpg', width=None)


#Einzelne Unterarten der Brute-force Attacken zwei spalten aufgeteilt
col1, col2, = st.columns(2)

#Definition der Variabeln der Knöpfe um den Text aufzurufen und wieder zu schliessen
button_1 = 0
button_2 = 0
button_3 = 0
button_4 = 0


# definieren der Knöpfe open und close mit Hilfe der Variable button_1,2,3,4    
with col1:
    st.header('dicnoary Angriff')
    if st.button('open_1'):
        button_1 = 1

    if st.button('close_1'):
        button_1 = 0
     
    if button_1 == 0:
        st.write ('click to open')
    if button_1 == 1:
        st.write ('Bei Dictionary-Angriffen werden wie der Name schon andeutet, vorhandene Wortlisten mit geläufigen Nutzernamen und Passwörtern eingesetzt, um digitale Zugänge zu knacken.')
    
        
with col2:
    st.header('credential stuffing')
    if st.button('open_2'):
        button_2 = 1

    if st.button('close_2'):
        button_2 = 0
     
    if button_2 == 0:
        st.write ('click to open')
    if button_2 == 1:
        st.write ('Beim sogenannten Credential Stuffing sind bereits die vollständigen Zugangsdaten bekannt, nicht jedoch der Dienst oder die Plattform, auf welcher sie zutreffen. Die Angreifer machen sich bei dieser Brute-Force-Methode die Bequemlichkeit auf Anwenderseite zu nutze. Da trotz regelmäßiger Warnungen immer noch viele Anwender ein und dieselbe E-Mail-Passwort-Kombination für mehrere Dienste nutzen, ist es für Cyberkriminelle ein Leichtes zahlreiche Konten zu kapern, sobald diese Informationen einmal bekannt sind. Meist stammen die erbeuteten Logininformationen aus Datenpannen von Internetdiensten. Im Darknet werden ganze Listen mit diesen Datensätzen gehandelt. Um möglichst schnell und unerkannt vorzugehen, setzen Angreifer auf Botnetze, die getarnt und mit unterschiedlichen IP-Adressen unzählige parallele Anmeldeversuche starten.')

col3, col4 =st.columns(2)

with col3:
    st.header('hybrid brute force attack')
    if st.button('open_3'):
        button_3 = 1

    if st.button('close_3'):
        button_3 = 0
     
    if button_3 == 0:
        st.write ('click to open')
    if button_3 == 1:
        st.write ('Ein Hybrid-Brute-Force-Angriff ist ein Angriff, bei dem mehrere Passwort-Guessing-Algorithmen und Methoden kombiniert und automatisiert werden, um den versuchten Zugriff auf ein geschütztes System zu erleichtern. Dazu gehören normalerweise Wortlisten, die Vergleiche mehrerer Wörter direkt hintereinander und andere Techniken. Er ist gefährlich, da er schwer zu entdecken und zu kontrollieren ist.')

with col4:
    st.header('traditional brute force attack')
    if st.button('open_4'):
        button_4 = 1

    if st.button('close_4'):
        button_4 = 0
     
    if button_4 == 0:
        st.write ('click to open')
    if button_4 == 1:
        st.write ('Wenn keine Informationen zu Kennwörtern oder Accountnamen verfügbar sind und die Angreifer lediglich alle möglichen Kombinationen von Login-Daten testen, spricht man von herkömmlichem Brute Force. Umso stärker die dabei eingesetzte Hardware ausfällt, desto schneller können die gesuchten Kennwörter aufgespürt werden. Spezielle Grafikkarten eignen sich sehr gut zum Lösen kryptografischer Rätsel. Daher werden diese auch primär zum Schürfen von Digitalwährungen wie Bitcoin eingesetzt, da sich hier die Anforderungen an die Hardware ähneln.')


#Thementrenner
st.write("---") 


st.header ('Dies passiert während einer brute force attack')

#Trennung von Passwort und Animation durch zwei Kolonnen
col5, col6 = st.columns(2)

#passwort des Beispieles
with col5:
    st.header ('Passwort: 915')
   
#animation, die per knopfdruck erscheint, jedoch selbst abgespielt werden muss
with col6:
    video_file = open('animation.mp4', 'rb')
    video_bytes = video_file.read()
    if st.button('Video starten'):
        st.video(video_bytes, format='animation/mp4')



#Thementrenner
st.write("---") 

st.header ('Passwortsicherheit')
st.write ('Wie man im obigen Beispiel gut sieht, kann ein passwort schnell gehackt werden. Aus diesem Grund ist die Passwortsicherheit sehr wichtig. Durch folgende Punkte kann man sich besser vor solchen Brute-force Attacken schützen:')

#drei Kolonnen, in jeder Kolonne wird eine Möglichkeit, sich vor Brute_force Attacken zu schützen, aufgezeigt
col8, col9, col10 = st.columns(3)

with col8:
    st.write('Benutzten Sie komplexe Passwörter')
    st.caption('Komplexe Passwörter tragen dazu bei, dass Ihr Online-Konto und Ihre persönlichen Daten vor unerwünschten Individuen oder Organisationen geschützt sind, mit denen Sie evtl. nicht bekannt sind. Je komplexer ein Passwort ist, desto schwieriger ist es zu erraten und die Wahrscheinlichkeit, dass es von jemandem enträtselt werden könnte, wird verringert. Komplexe Passwörter helfen auch, die Sicherheit Ihres Kontos zu gewährleisten, insbesondere wenn sie regelmäßig geändert werden. Eine Kombination aus Buchstaben, Zahlen und Sonderzeichen ist am besten, um ein sicheres Passwort zu schaffen, z.B. P@ssw0rd1234. ')

with col9:
    st.write('Verwenden Sie ein Passwortmanager-Tool')
    st.caption('Die Verwendung eines Passwortmanager-Tools ist ein guter Weg, um sicherzustellen, dass alle Ihre Passwörter sicher, einzigartig und nicht leicht zu entschlüsseln sind. Bei der Auswahl eines Tools achten Sie auf die Sicherheitseigenschaften des Tools. Beispielsweise sollte es über eine starke Verschlüsselung und ein System zur zweifachen Authentifizierung verfügen. Viele Tools bieten andere Sicherheitsfunktionen, die dabei helfen, unsichere Passwörter zu erkennen und zu ersetzen. Der Einsatz eines Passwortmanagers ist ein wichtiger Bestandteil einer guten Passwortsicherheitsstrategie.')

with col10:
    st.write('Aktualisieren Sie häufig Ihre Passwörter')
    st.caption('Je mehr Sie Ihre Passwörter aktualisieren, desto schwerer ist es für potenzielle Angreifer, Zugriff auf Ihr Konto zu erhalten. Daher ist es wichtig, Ihre Kennwörter häufig zu aktualisieren. Ein guter Anhaltspunkt ist es, Ihre Passwörter alle 3 bis 6 Monate zu ändern. Wenn Sie ein kritisches Konto geschützt haben müssen und sicherstellen müssen, dass es niemand kompromittiert, empfehlen wir Ihnen, dies häufiger zu tun.')

col11, col12, col13 = st.columns (3)

with col11:
    st.write ('Verwenden Sie nicht dasselbe Passwort für mehrere Konten oder Dienste. ')
    st.caption('Es ist wichtig, unterschiedliche Passwörter zu verwenden, da dies die Wahrscheinlichkeit verringert, dass ein Konto oder ein Dienst gehackt wird. Wenn man dasselbe Passwort für mehrere Konten verwendet, kann ein Hacker ein Konto knacken und dann automatisch Zugang zu allen anderen Konten erhalten. Ein schlauer Hacker kann dann sogar versuchen, Zugriff auf sensible Informationen zu erhalten. Deshalb ist es wichtig, dass jedes Konto, das Sie erstellen, ein einzigartiges und sicheres Passwort hat.')

with col12:
    st.write ('Verwenden Sie Zwei-Faktor-Authentifizierung, falls möglich. ')
    st.caption('Die Verwendung der Zwei-Faktor-Authentifizierung ist eine der besten Möglichkeiten, um das Risiko beim Passwortverkehr zu verringern. Mit der Zwei-Faktor-Authentifizierung müssen Benutzer neben ihrem Passwort auch ein zusätzliches Verfahren verwenden, um sich anzumelden. Dazu gehören ein physischer Faktor, wie z.B. ein Hardware-Token oder eine Smartcard oder ein sekundärer digitaler Faktor wie z.B. eine SMS, ein E-Mail-Code oder eine mobile Authentifizierungsanwendung. Da die Benutzer mit zwei separaten Faktoren anmelden müssen, ist die Wahrscheinlichkeit eines erfolgreichen Angriffs deutlich geringer, da der Angreifer mindestens beide Faktoren kennen')

with col13:
    st.write ('Seien Sie vorsichtig, wenn Sie öffentliches WLAN verwenden.')
    st.caption ('Da öffentliche WLAN-Netzwerke nicht durch sichere Zugangskontrollen geschützt sind, können unbefugte Benutzer möglicherweise leicht Ihr Passwort erraten, ausspähen oder Ihre Kommunikation abfangen. Deshalb sollte man bei der Passwortwahl besonders vorsichtig sein, wenn man ein öffentliches WLAN verwendet, um die Sicherheit der eigenen Daten zu gewährleisten. Ein starkes Passwort mit einer Kombination aus Groß- und Kleinschreibung, Zahlen und Symbolen kann einen hervorragenden Job bei der Aufrechterhaltung der Sicherheit Ihrer Daten erledigen.')