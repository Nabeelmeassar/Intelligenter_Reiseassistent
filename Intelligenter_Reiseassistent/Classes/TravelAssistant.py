import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from collections import OrderedDict

class TravelAssistant:
    def __init__(self, csv_file_path, new_user_preferences, cities):
        self.csv_file_path = csv_file_path
        self.new_user_preferences = new_user_preferences
        self.cities = cities
        
    # Funktion zum Laden und Vorbereiten der Daten
    def load_and_prepare_data(self):
        try:
            # Versuch, die Daten aus der CSV-Datei zu laden, die im Konstruktor angegeben wurde.
            data = pd.read_csv(self.csv_file_path)
        
            # Entfernen der Spalte 'Bewertung' aus dem DataFrame, um die Features zu erhalten.
            # 'axis=1' gibt an, dass eine Spalte entfernt werden soll (im Gegensatz zu einer Zeile).
            features = data.drop('Bewertung', axis=1)
        
            # Die Spalte 'Bewertung' wird als Label (Zielvariable) gespeichert.
            labels = data['Bewertung']
        
            # R�ckgabe der Features und Labels, um sp�ter f�r das Training des Modells verwendet zu werden.
            return features, labels
        
        except FileNotFoundError as e:
            # Falls die angegebene Datei nicht gefunden werden kann, wird eine Fehlermeldung ausgegeben.
            print(f"Datei nicht gefunden: {e}")
        
            # Die Funktion gibt 'None' f�r Features und Labels zur�ck, um anzuzeigen, dass das Laden fehlgeschlagen ist.
            return None, None
        
        except KeyError as e:
            # Dieser Block f�ngt Fehler ab, die durch das Fehlen einer erwarteten Spalte im CSV verursacht werden.
            print(f"Fehlende Spalte: {e}")
        
            # �hnlich wie beim FileNotFoundError gibt die Funktion 'None' zur�ck, um ein Problem zu signalisieren.
            return None, None
    
    # Hauptfunktion f�r Vorhersagen
    def predict_user_preferences(self):
        # Laden und Vorbereiten der Daten mit der zuvor definierten Funktion.
        X, y = self.load_and_prepare_data()
        if X is None or y is None:
            # Wenn das Laden der Daten fehlschl�gt, wird die Funktion abgebrochen und None zur�ckgegeben.
            return None

        # Identifizieren kategorischer Spalten f�r die sp�tere Verarbeitung.
        categorical_features = ['Ziel']  # Beispielkategorie; muss entsprechend den Daten angepasst werden.
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        # Erstellen des ColumnTransformers, um kategorische Daten automatisch zu verarbeiten.
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', categorical_transformer, categorical_features),
            ],
            remainder='passthrough'
        )

        # Aufteilen der Daten in Trainings- und Testdatens�tze.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
        # Erstellen einer Pipeline zur Kapselung der Vorverarbeitung und des Regressormodells.
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
        ])

        # Trainieren des Modells mit den Trainingsdaten.
        pipeline.fit(X_train, y_train)

        # Vorhersagen mit dem Testdatensatz und Bewertung des Modells.
        predictions = pipeline.predict(X_test)
        model_mse = mean_squared_error(y_test, predictions)
    
        # Vorbereiten von individuellen Vorhersagen basierend auf Benutzerpr�ferenzen.
        user_predictions = {}
        for city in self.cities:
            # Extrahieren einer Datenzeile f�r die gegebene Stadt.
            city_data = X[X['Ziel'] == city].iloc[0:1].copy()
        
            # Aktualisieren der Datenzeile mit den neuen Benutzerpr�ferenzen.
            for feature, value in self.new_user_preferences.items():
                if feature in city_data:
                    city_data[feature] = value
        
            # Vorhersage der Bewertung f�r die einzelne Stadt.
            city_pred = pipeline.predict(city_data)[0]
            user_predictions[city] = city_pred
        
            # Aktualisieren der Bewertung im cities-Dictionary, falls vorhanden.
            if self.cities[city].name == city:
                self.cities[city].update_rating(city_pred)
    
        # Sortieren der Vorhersagen in absteigender Reihenfolge der Bewertungen.
        sorted_predictions = OrderedDict(sorted(user_predictions.items(), key=lambda x: x[1], reverse=True))

        # Ausgabe der sortierten Vorhersagen.
        for city, pred in sorted_predictions.items():
            print(f"Stadt: {city}, Vorhergesagte Bewertung: {pred}")

        # R�ckgabe des aktualisierten St�dte-Dictionary und des Modellfehlers (MSE).
        return self.cities, model_mse