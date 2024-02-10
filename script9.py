import streamlit as st
import openai
"""
Script9 is beste en laatste versie -> met 3 vragen 

samenvatting en korte uitleg: 

De werking van mijn app is eenvoudig maar effectief. 
Gebruikers beginnen door een tekst van een paper te plakken die ze willen verbeteren in het ene tekstgebied,
en vervolgens voegen ze een verbeteringsrubriek toe in het andere tekstgebied. 
Met een simpele klik op de knop "Start gebruik van AI Verbeteringstool"
wordt de ingevoerde informatie naar het OpenAI GPT- model4 gestuurd. 
Het model genereert vervolgens twee belangrijke stukken tekst. 
De eerste geeft punten toe aan verschillende aspecten van de paper op basis van de meegegeven rubriek,
terwijl de tweede alinea feedback geeft aan de student, waarbij zowel positieve als negatieve aspecten worden benadrukt.
De resultaten worden gestileerd weergegeven in afzonderlijke kaders voor duidelijkheid.
Met deze intuïtieve benadering biedt de app een geautomatiseerd hulpmiddel 
om papers te evalueren en waardevolle inzichten te verkrijgen voor zowel studenten als docenten.

        
"""







################################################################
# de API key - gekregen van meneer Frederik 
openai.api_key = "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"


################################
#uitleg in stappen over de werking van de app 
intro_tekst = """
<div style='border: 2px solid #3498db; padding: 10px; margin-bottom: 20px;'>
<h3>Welkom bij de Verbeter Tool met AI!</h3>
<p> Deze tool maakt gebruik van geavanceerde AI-technologie om je te helpen bij het evalueren en verbeteren van papers.</p>
<p> STAP 1:Kopieer de tekst van de paper die je wilt verbeteren en plak deze in het linkerkader van de Verbeter Tool. </p>
<p> STAP 2: Voer de verbeteringsrubriek of feedback in het rechterkader in. Dit is waar je instructies geeft over welke aspecten van de paper verbeterd moeten worden. </p>
<p> STAP 3: Stel de gewenste tokens in </p> 
<p style='font-style: italic' > extra uitleg: Tokens vormen de essentie van geschreven tekst. Neem bijvoorbeeld het woord 'Verbeter Tool', dat uit twee tokens bestaat. Dit model begrijpt en creëert tekst door gebruik te maken van deze tokens. Wanneer we het aantal tokens beperken, verbetert niet alleen de snelheid van het model, maar ook de betrouwbaarheid van de resultaten. Het is daarom van belang om bij het bepalen van de hoeveelheid tokens rekening te houden met een efficiënte verwerking en verbeterde prestaties. </p>
<p> STAP 4: Klik op de knop "Start gebruik van AI Verbeteringstool" om de geavanceerde AI-technologie te activeren </p> 
<p> STAP 5: Wacht een paar seconden terwijl de AI-tool bezig is met het verbeteren van de paper. </p>
<p> STAP 6: Je zult 3 vakken zien: <br>
1. In het eerste vak ontvang je een overzichtelijke puntenverdeling voor de paper.<br>
2. In het tweede vak krijg je gedetailleerde feedback voor de student. Dit omvat zowel de sterke punten als de gebieden die verbeterd kunnen worden.<br>
3. In het derde vak ontvang je een relevante samenvatting van het menselijke aspect in de studentenpaper voor begrip van de docent.<br>
</p>
<p> STAP 7:Druk op "Einde gebruik" om de huidige sessie af te sluiten. 
Als je de tool opnieuw wilt gebruiken voor een andere paper zonder de verbeteringsrubriek te wijzigen, laat de velden dan ingevuld.
Als je een nieuwe paper wilt verbeteren met een nieuwe set instructies, maak dan de velden leeg en vul de linkerkant met de tekst van de nieuwe paper en de rechterkant met de bijbehorende verbeteringsrubriek.  </p>
</div>
"""
st.markdown(intro_tekst, unsafe_allow_html=True)

######################################################################## 
# hier kan je de pagina stijlen: kleur, grootte... 
st.markdown("<style>body { background-image: url('achtergrondafbeelding.jpg'); background-size: cover;}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='color: #3498db;'>Verbeter Tool met AI</h1>", unsafe_allow_html=True)
st.write("<style>body {background-color:red;}</style>", unsafe_allow_html=True)

max_tokenss = st.selectbox("Kies het gewenste aantal tokens:", [450,500,550,600])
def stel_chatgpt_vraag(vraag):
    antwoord = openai.Completion.create(
        model="text-davinci-003",
        prompt=vraag,
        max_tokens=max_tokenss  
    ).choices[0].text.strip()

    return antwoord

################################
# Streamlit-applicatie
def main():
    col1, col2 = st.columns(2)
    
    ################################
    # kolom 1 en 2 gemaakt voor een betere en duidelijke onderscheiding
    # hier kan je kolom 1 en 2 aanpassen
    with col1:
        x = st.text_area("plak hier de paper die je wilt verbeteren:")
        tokens_kader_1 = len(x.split())
        st.write(f"Aantal tokens in kader 1: {tokens_kader_1}")

    with col2:
        y = st.text_area("plak hier de verbeteringsrubriek :")
        tokens_kader_2 = len(y.split())
        st.write(f"Aantal tokens in kader 2: {tokens_kader_2}")
        

    #max_tokens = st.slider("Bepaal zelf het aantal tokens. Houd er rekening mee dat een hoger aantal tokens kan leiden tot langere verwerkingstijden en mogelijk minder nauwkeurige informatie.", 100, 400, 300)
    #max_tokens = st.selectbox("Kies het gewenste aantal tokens:", [400,500,600])
    if st.button("Start gebruik van AI Verbeteringstool"):
        st.title("Resultaten")

        # Controleren of er waarden voor x en y zijn ingevoerd
        if x and y:
            # dit is de 1ste vraag die naar chatgpt wordt gestuurd
            vraag_1 = (
                f"ik ga je een paper van een student geven en je moet hem evalueren op basis van een verbeteringsrubriek. paper = {x}. de rubriek = {y}."
                #f"geef hem een punt voor elk onderdeel en maak duidelijk onderscheid tussen de onderdelen : identiteit en vaardigeden,ambities voor 2030,concrete bewoording, argumentatie,kwaliteit van schrijven +totaal van alle onderdelen. per onderdeel wil ik ook in een paar zinnen uitleg over dat punt"
                f"Beoordeel de paper op de volgende onderdelen: identiteit en vaardigheden, ambities voor 2030, concrete bewoording, argumentatie, en kwaliteit van schrijven. Wijs een punt toe voor elk onderdeel en maak duidelijk onderscheid tussen deze aspecten. Geef ook een totaalpunt voor alle onderdelen. Bovendien, voor elk onderdeel, geef een korte uitleg in een paar zinnen over de toekenning van dat punt."    
                f"Geef op een schaal van 0% tot 100% aan in welke mate je zeker bent van jouw beoordeling"           
            )
            antwoord_1 = stel_chatgpt_vraag(vraag_1)

            # dit is de 2de vraag die naar chatgpt wordt gestuurd
            vraag_2 = (
                f"ik ga je een paper van een student geven en je moet hem evalueren op basis van een verbeteringsrubriek. paper = {x}. de rubriek = {y}."
                f"Schrijf één alinea in de ik-vorm waarin je de student uitlegt wat hij goed heeft gedaan. Daarnaast, schrijf één alinea in de ik-vorm waarin je de student uitlegt wat hij minder goed heeft gedaan."
            )
            antwoord_2 = stel_chatgpt_vraag(vraag_2)
            
            # dit is de 3de vraag die naar chatgpt wordt gestuurd
            vraag_3 = (
                f"Ik ga je een paper van een student geven en ik wil graag een samenvatting van de menselijke aspecten ervan, maar alleen als deze relevant zijn voor de docent en essentieel zijn voor hun begrip.paper = {x}. "
            )
            antwoord_3 = stel_chatgpt_vraag(vraag_3)
            
            # hier wordt het antwoord gestijld voor een betere stijl 
            # kader  =  maroon rand
            st.markdown(f"<div style='border: 5px solid Maroon; padding: 10px; margin-bottom: 20px;'> <h2 style='color: green; font-style: italic;'>punten per rubrieksonderdeel:</h2> {antwoord_1} </div>", unsafe_allow_html=True)

            # hier wordt het antwoord gestijld voor een betere stijl 
            # kader  =  olive rand
            # st.markdown(f"<div style='border: 3px solid red; padding: 10px; margin-bottom: 20px;'> <h2>uitleg voor de student:</h2> {antwoord_2} </div>", unsafe_allow_html=True)
            st.markdown(f"<div style='border: 5px solid Olive; padding: 10px; margin-bottom: 20px;'><h2 style='color: green; font-style: italic;'>Uitleg voor de student:</h2> {antwoord_2} </div>", unsafe_allow_html=True)

            # hier wordt het antwoord gestijld voor een betere stijl 
            # kader  =  orange rand
            # st.markdown(f"<div style='border: 3px solid red; padding: 10px; margin-bottom: 20px;'> <h2>uitleg voor de student:</h2> {antwoord_3} </div>", unsafe_allow_html=True)
            st.markdown(f"<div style='border: 2px solid green; padding: 10px; margin-bottom: 20px;'><h2 style='color: orange; font-style: sans-serif; font-size: 10;'>Relevante Samenvatting van Menselijk Aspect in Studentenpaper voor Docentelijk Begrip</h2> {antwoord_3} </div>", unsafe_allow_html=True)
            
            
            # Knop om terug te gaan naar de startpagina
            if st.button("Einde gebruik"):
                st.title("Verbeter Tool met AI")

        else:
            st.warning("Vul de paper en verbeteringsrubriek in")

if __name__ == "__main__":
    main()
