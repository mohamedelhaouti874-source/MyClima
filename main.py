from flask import Flask, render_template_string
import plotly.graph_objects as go
import random

app = Flask(__name__)

# Fonction pour générer des températures fictives pour la semaine (7 jours)
def generer_temperatures():
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    temperatures = [random.randint(10, 30) for _ in range(7)]  # Températures aléatoires entre 10 et 30°C
    return jours, temperatures

@app.route('/')
def index():
    # Générer les données
    jours, temperatures = generer_temperatures()
    
    # Créer un graphique avec Plotly (courbe interactive)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=jours, y=temperatures, mode='lines+markers', name='Température (°C)',
                             line=dict(color='royalblue', width=3), marker=dict(size=8, color='orange')))
    fig.update_layout(
        title="Températures de la Semaine - Un Voyage Climatique ! 🌡️",
        xaxis_title="Jours",
        yaxis_title="Température (°C)",
        template="plotly_white",  # Thème créatif
        paper_bgcolor='lightblue',  # Fond coloré pour un look ludique
        plot_bgcolor='aliceblue'
    )
    
    # Convertir le graphique en HTML
    graph_html = fig.to_html(full_html=False)
    
    # HTML de la page web avec un style créatif (thème arc-en-ciel et animations)
    html_template = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Températures de la Semaine</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(45deg, #ff9a9e, #fecfef, #a8edea, #fed6e3);
                color: #333;
                text-align: center;
                padding: 20px;
                animation: rainbow 5s infinite;
            }
            @keyframes rainbow {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            h1 {
                color: #fff;
                text-shadow: 2px 2px 4px #000;
                font-size: 2.5em;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            p {
                font-size: 1.2em;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 Températures de la Semaine 🌟</h1>
            <p>Découvre les fluctuations de température avec cette courbe interactive ! Chaque jour apporte son lot de surprises météo.</p>
            <div>{{ graph_html | safe }}</div>
            <p>Données générées aléatoirement pour cet exemple. Actualise la page pour de nouvelles valeurs !</p>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
