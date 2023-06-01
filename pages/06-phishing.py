import streamlit as st # Ladet die Streamlit Bibliothek


st.title ('Social Engineering Attacken - Phishing')


# Theorieteil:
st.header ('Was sind Social Engineering Attacken')
st.write ('Social Engineering Attacken sind Techniken, mit denen Angreifer versuchen, die Vertrauenswürdigkeit und Menschlichkeit von Opfern auszunutzen, um an private Informationen oder Zugangsdaten zu gelangen oder Schadsoftware auf deren Geräten zu installieren. Die Angriffe können in Form von gefälschten E-Mails, Telefonanrufen, SMS-Nachrichten, Instant Messages oder sogar persönlichen Gesprächen erfolgen. Die Angreifer geben sich oft als vertrauenswürdige Personen oder Organisationen aus und täuschen die Empfänger durch raffinierte Manipulationen. Die Opfer werden so dazu gebracht, persönliche und vertrauliche Daten preiszugeben oder auf schädliche Links zu klicken. Social Engineering Attacken zielen darauf ab, menschliche Schwächen auszunutzen, um Zugang zu sensiblen Informationen oder Systemen zu erhalten.')


st.header ('Was sind Phishing Attacken')
st.write ('Phishing-Angriffe sind eine Art von Cyber-Angriffen, bei denen Kriminelle gefälschte Webseiten, E-Mails oder Nachrichten erstellen, um Benutzer dazu zu bringen, sensible Informationen wie Passwörter, Kreditkarteninformationen oder persönliche Daten preiszugeben. Diese betrügerischen Aktivitäten werden oft als legitime Anfragen von vertrauenswürdigen Organisationen oder Unternehmen getarnt, um das Opfer dazu zu bringen, auf einen Link zu klicken oder auf eine gefälschte Anmeldung zu reagieren. Sobald diese Informationen gestohlen wurden, können die Angreifer sie für Identitätsdiebstahl, Finanzbetrug und andere kriminelle Aktivitäten verwenden.')

st.image ('01 Phishing.png')


st.header ('Worauf soll man achten')
st.write ('Es gibt einige Merkmale, die auf eine Phishing-E-Mail hinweisen können:')
st.write ('1. Überprüfen Sie immer den Absender der E-Mail. Betrüger verwenden oft gefälschte E-Mail-Adressen, die dem Original ähnlich klingen, um Sie zu täuschen.')
st.write ('2. Wenn Sie in der E-Mail mit einer unpersönlichen Anrede angesprochen werden, ist dies ein Hinweis darauf, dass es sich um eine Fälschung handeln könnte.')
st.write ('3. Phishing-Betrüger versuchen häufig, Sie zu einer schnellen Entscheidung zu bewegen, indem sie vorgeben, dass Ihr Konto gehackt wurde oder dass Sie sofort handeln müssen. Dadurch wird ein Gefühl der Dringlichkeit erzeugt, das das Opfer eher dazu verleitet, entsprechend zu reagieren.')
st.write ('4. Achten Sie nicht nur auf verdächtige Links, sondern auch auf bekannte oder vertrauenswürdige Links, hinter denen sich bösartige Absichten verbergen könnten. Bevor Sie auf einen Link klicken, überprüfen Sie durch Bewegen des Mauszeigers, ob der Link tatsächlich zu einer legitimen Website führt.')
st.write ('5. Phishing-E-Mails fragen häufig nach vertraulichen Informationen wie Passwörtern, Kreditkarteninformationen oder Sozialversicherungsnummern. Seriöse Unternehmen fordern solche vertraulichen Informationen niemals in einer E-Mail an.')
st.write ('6. Phishing-E-Mails können Rechtschreib- und Grammatikfehler enthalten und in einer ungewöhnlichen Sprache verfasst sein. Wenn die E-Mail verdächtig aussieht, ist es am besten, sie zu löschen oder zu überprüfen, ob es sich um eine legitime E-Mail handelt.')


# Interaktiver Teil:
st.header ('Phishing E-Mails erkennen - Beispiel Bank')
st.write ('Im Folgenden sehen Sie eine gefälschte E-Mail, die typische Anzeichen einer Phishing-Attacke aufweist. Kreuzen Sie die Abschnitte an, in denen sich Merkmale befinden.')

# Die Checkboxen lassen den Nutzer mehrere Optionen auswählen.
Check_1 = st.checkbox ('Von: USB-Bank Sicherheitsteam') 
Check_2 = st.checkbox ('Betreff: Wichtige Sicherheitsmitteilung: Aktualisierung Ihres Bankkontos erforderlich')
Check_3 = st.checkbox ('Datum: Fr, 02.06.2023, 15:00')
st. write ('__________________________________________________________________________________')
Check_4 = st.checkbox ('Sehr geehrter Kunde,')
Check_5 = st.checkbox ('Wir möchten Sie darüber informieren, dass unsere Bank neue Sicherheitsmaßnahmen eingeführt hat, um Ihre Konten zu schützen.')
Check_6 = st.checkbox ('Daher müssen Sie Ihr Konto aktualisieren. dies ist erforderlich, um weiterhin uneingeschrenkten Zugriff auf Ihr Bankkonto zu haben.')
Check_7 = st.checkbox ('Bitte klicken Sie auf den unten stehenden Link, um sofort auf eine sichere Seite weitergeleitet zu werden und Ihr Konto zu aktualisieren.')
Check_8 = st.checkbox ('wmw.Sicherheitsmassnahmen.Bank-USB.com')
Check_9 = st.checkbox ('Bitte beachten Sie, dass das Versäumnis, Ihr Konto innerhalb von 24 Stunden zu aktualisieren, dazu führen kann, dass der Zugriff auf Ihr Konto eingeschränkt wird.')
Check_10 = st.checkbox ('Bei Fragen stehen wir Ihnen gerne zur Verfügung. Wir bedanken uns für Ihre Zusammenarbeit.')
Check_11 = st.checkbox ('Mit freundlichen Grüssen,')
Check_12 = st.checkbox ('Ihr USB-Bank Sicherheitsteam')


# Der Knopf soll den Rest der Website anzeigen, sobald er angeklickt wird.
if st.button ('FERTIG'):

    st.header ('Punktzahl')

    # Berechnung der Punktzahl von der vorherigen Aufgabe.
    i = 0
    
    if Check_1:
        i = i + 1 # Wenn die entsprechende Checkbox angeklickt wird, wird die Punktzahl i um 1 erhöht
    if Check_4:
        i = i + 1
    if Check_6:
        i = i + 1
    if Check_7:
        i = i + 1
    if Check_8:
        i = i + 1
    if Check_9:
        i = i + 1
    if Check_12:
        i = i + 1

    st.write ('Erreichte Punktzahl:', i , '/ 7')# Zeigt die erreichte Punktzahl an.


    # Bild einfügen von den richtigen Lösungen.
    st.header ('Lösungen')
    st.image ('02 Lösungen.png')


    # Begründung der Lösung
    st.header ('Erklärung')
    st.write ('- Die Absenderadresse ist nicht die einer legitimen Bank. Sie sieht vertrauenswürdig aus, aber die USB Bank existiert in Wirklichkeit nicht.')
    st.write ('- Die Anrede ist unpersönlich. Ein seriöses Unternehmen schreibt Sie immer mit Ihrem Namen an.')
    st.write ('- Die E-Mail enthält mehrere Rechtschreibfehler.')
    st.write ('- In der E-Mail werden Sie aufgefordert, auf einen Link zu klicken.')
    st.write ('- In der E-Mail befindet sich ein Link. Wenn Ihre Bank wirklich etwas von Ihnen verlangt, würde sie niemals einen Link in die E-Mail einfügen.')
    st.write ('- In der Mail werden Sie aufgefordert, innerhalb einer bestimmten Frist zu handeln. Außerdem wird damit gedroht, dass Ihr Zugriff auf das Konto eingeschränkt wird.')
    st.write ('- In der Schlussformel steht wieder der gefälschte Name der Bank.')


    # Abschluss
    st.header ('Schlusswort')
    st.write ('Social Engineering Attacken sind eine allgegenwärtige Bedrohung, die theoretisch jeden treffen kann, unabhängig von Alter, Geschlecht, Beruf oder sozialem Status. Auch Unternehmen sind vor dieser Bedrohung nicht gefeit und müssen sich vor solchen Angriffen schützen.')
    st.write ('Um sich vor Social Engineering Attacken zu schützen, ist vor allem Wachsamkeit gefragt. Nutzer sollten niemals unaufgefordert persönliche oder vertrauliche Informationen preisgeben und sich immer vergewissern, dass sie mit der tatsächlich betroffenen Person oder Institution kommunizieren. Unternehmen sollten ihre Mitarbeiter entsprechend schulen und sensibilisieren, um deren Bewusstsein zu erhöhen.')
    st.write ('Zusätzlich können technische Schutzmaßnahmen wie Firewalls, Antivirenprogramme und zentrale Authentifizierungssysteme helfen, Angriffe abzuwehren und sensible Daten zu schützen.')
    st.write ('Insgesamt ist es wichtig, sich bewusst zu sein, dass Social Engineering Attacken eine dauerhafte Bedrohung darstellen.')