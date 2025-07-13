"""
Script semplificato per la previsione del prezzo delle auto usando Linear Regression
Dataset: CarPrice_Assignment.csv
Librerie: scikit-learn con preprocessing - Versione Educational
"""

import pandas as pd  # Importa pandas per la gestione dei dati
import numpy as np  # Importa numpy per operazioni numeriche
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
)  # Importa funzioni per split e validazione incrociata
from sklearn.linear_model import (
    LinearRegression,
)  # Importa il modello di regressione lineare
from sklearn.preprocessing import (
    StandardScaler,
    LabelEncoder,
)  # Importa scaler e label encoder
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    mean_absolute_error,
)  # Importa metriche di valutazione
import matplotlib.pyplot as plt  # Importa matplotlib per la visualizzazione
import warnings  # Importa warnings per gestire avvisi

warnings.filterwarnings(
    "ignore"
)  # Disabilita i warning per una visualizzazione più pulita


def load_and_explore_data(file_path):
    """Carica e esplora il dataset"""
    print("🚗 Caricamento del dataset...")  # Messaggio di caricamento
    df = pd.read_csv(file_path)  # Carica il dataset da file CSV

    print(f"📊 Dimensioni del dataset: {df.shape}")  # Stampa dimensioni dataset
    print(f"📋 Colonne: {list(df.columns)}")  # Stampa nomi colonne
    print(
        f"💰 Target variable: 'price' - Min: ${df['price'].min()}, Max: ${df['price'].max()}"
    )  # Stampa range della variabile target
    print("🔍 Valori mancanti per colonna:")  # Messaggio per valori mancanti
    print(
        df.isnull().sum()[df.isnull().sum() > 0]
    )  # Stampa colonne con valori mancanti

    return df  # Ritorna il dataframe


def preprocess_data(df):
    """Preprocessa i dati per il machine learning"""
    print("\n🔧 Preprocessing dei dati...")  # Messaggio di inizio preprocessing

    # Rimuovi la colonna car_ID (non utile per la predizione)
    df = df.drop("car_ID", axis=1)  # Elimina colonna identificativa

    # Estrai il brand dal CarName
    df["brand"] = (
        df["CarName"].str.split().str[0].str.lower()
    )  # Estrae il brand dal nome auto
    df = df.drop("CarName", axis=1)  # Elimina la colonna CarName

    # Gestisci valori anomali/inconsistenti
    # Correzioni per alcuni brand name inconsistenti
    brand_corrections = {
        "toyouta": "toyota",
        "vokswagen": "volkswagen",
        "maxda": "mazda",
        "porcshce": "porsche",
    }  # Dizionario correzioni brand
    df["brand"] = df["brand"].replace(brand_corrections)  # Applica correzioni

    # Converti le colonne categoriche in formato appropriato
    categorical_features = [
        "fueltype",
        "aspiration",
        "doornumber",
        "carbody",
        "drivewheel",
        "enginelocation",
        "enginetype",
        "cylindernumber",
        "fuelsystem",
        "brand",
    ]  # Lista colonne categoriche

    numerical_features = [
        "symboling",
        "wheelbase",
        "carlength",
        "carwidth",
        "carheight",
        "curbweight",
        "enginesize",
        "boreratio",
        "stroke",
        "compressionratio",
        "horsepower",
        "peakrpm",
        "citympg",
        "highwaympg",
    ]  # Lista colonne numeriche

    # Verifica che tutte le feature siano presenti
    existing_categorical = [
        col for col in categorical_features if col in df.columns
    ]  # Filtra colonne categoriche esistenti
    existing_numerical = [
        col for col in numerical_features if col in df.columns
    ]  # Filtra colonne numeriche esistenti

    print(
        f"✅ Feature categoriche: {len(existing_categorical)}"
    )  # Stampa numero colonne categoriche
    print(
        f"✅ Feature numeriche: {len(existing_numerical)}"
    )  # Stampa numero colonne numeriche

    return (
        df,
        existing_categorical,
        existing_numerical,
    )  # Ritorna dataframe e liste colonne


def train_model(X, y):
    """Addestra il modello di regressione lineare"""
    print("\n🎯 Addestramento del modello...")  # Messaggio di inizio training

    # Suddividi i dati
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )  # Split train/test

    # Crea i preprocessori
    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()  # Trova colonne categoriche

    # Preprocessing personalizzato per le feature categoriche
    # Usiamo LabelEncoder manualmente per gestire meglio le categorie
    X_processed = X.copy()  # Copia X per il preprocessing
    label_encoders = {}  # Dizionario per salvare i label encoder

    for col in categorical_features:
        le = LabelEncoder()  # Crea label encoder
        X_processed[col] = le.fit_transform(
            X_processed[col].astype(str)
        )  # Applica encoding
        label_encoders[col] = le  # Salva encoder

    # Suddividi i dati processati
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=0.2, random_state=42
    )  # Split train/test su dati processati

    # Preprocessor per le feature numeriche
    numerical_preprocessor = StandardScaler()  # Crea scaler
    X_train_scaled = numerical_preprocessor.fit_transform(X_train)  # Scala train
    X_test_scaled = numerical_preprocessor.transform(X_test)  # Scala test

    # Modello da addestrare
    model = LinearRegression()  # Crea il modello di regressione lineare

    print("\n📈 Addestramento Linear Regression...")  # Messaggio modello

    model.fit(X_train_scaled, y_train)  # Addestra modello
    y_pred = model.predict(X_test_scaled)  # Predice su test

    # Calcola le metriche
    mse = mean_squared_error(y_test, y_pred)  # Calcola MSE
    rmse = np.sqrt(mse)  # Calcola RMSE
    mae = mean_absolute_error(y_test, y_pred)  # Calcola MAE
    r2 = r2_score(y_test, y_pred)  # Calcola R2

    # Cross-validation
    cv_scores = cross_val_score(
        model, X_train_scaled, y_train, cv=5, scoring="r2"
    )  # Calcola CV R2
    cv_mean = cv_scores.mean()  # Media CV
    cv_std = cv_scores.std()  # Deviazione standard CV

    # Salva i risultati
    results = {
        "model": model,
        "mse": mse,
        "rmse": rmse,
        "mae": mae,
        "r2": r2,
        "cv_mean": cv_mean,
        "cv_std": cv_std,
        "y_pred": y_pred,
        "y_test": y_test,
    }  # Salva risultati

    print(f"   RMSE: ${rmse:.2f}")  # Stampa RMSE
    print(f"   MAE: ${mae:.2f}")  # Stampa MAE
    print(f"   R²: {r2:.4f}")  # Stampa R2
    print(f"   CV R² (media ± std): {cv_mean:.4f} ± {cv_std:.4f}")  # Stampa CV

    return (
        results,
        X_test_scaled,
        y_test,
        numerical_preprocessor,
        label_encoders,
    )  # Ritorna risultati e oggetti utili


def visualize_results(results):
    """Visualizza i risultati del modello"""
    print("\n📊 Creazione visualizzazioni...")  # Messaggio visualizzazione

    # Configura il plot - 2 grafici per il singolo modello
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))  # Crea figure e assi
    fig.suptitle(
        "Analisi Linear Regression - Previsione Prezzo Auto",
        fontsize=16,
        fontweight="bold",
    )  # Titolo generale

    # Estrae i risultati del modello
    y_test = results["y_test"]  # Valori reali
    y_pred = results["y_pred"]  # Valori predetti
    r2 = results["r2"]  # R2
    rmse = results["rmse"]  # RMSE

    # 1. Predicted vs Actual
    axes[0].scatter(
        y_test, y_pred, alpha=0.6, color="blue"
    )  # Scatter plot reale vs predetto
    axes[0].plot(
        [y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2
    )  # Linea ideale
    axes[0].set_xlabel("Prezzo Reale ($)")  # Etichetta asse x
    axes[0].set_ylabel("Prezzo Predetto ($)")  # Etichetta asse y
    axes[0].set_title(f"Predicted vs Actual\nR² = {r2:.4f}")  # Titolo
    axes[0].grid(alpha=0.3)  # Griglia

    # 2. Residui
    residuals = y_test - y_pred  # Calcola residui
    axes[1].scatter(y_pred, residuals, alpha=0.6, color="green")  # Scatter residui
    axes[1].axhline(y=0, color="r", linestyle="--")  # Linea zero
    axes[1].set_xlabel("Prezzo Predetto ($)")  # Etichetta asse x
    axes[1].set_ylabel("Residui ($)")  # Etichetta asse y
    axes[1].set_title(f"Analisi dei Residui\nRMSE = ${rmse:.2f}")  # Titolo
    axes[1].grid(alpha=0.3)  # Griglia

    plt.tight_layout()  # Layout compatto
    plt.savefig(
        "car_price_prediction_results.png", dpi=300, bbox_inches="tight"
    )  # Salva grafico
    plt.show()  # Mostra grafico

    return "Linear Regression"  # Ritorna nome modello


def make_predictions(model, preprocessor, label_encoders, sample_data):
    """Fa predizioni su nuovi dati"""
    print("\n🔮 Esempio di predizione...")  # Messaggio predizione

    # Esempio di nuova auto
    new_car = pd.DataFrame([sample_data])  # Crea dataframe per nuova auto

    # Applica label encoding
    for col, le in label_encoders.items():
        if col in new_car.columns:
            try:
                new_car[col] = le.transform(
                    new_car[col].astype(str)
                )  # Applica encoding
            except ValueError:
                # Se la categoria non è stata vista durante il training, usa la categoria più frequente
                new_car[col] = 0  # Gestione categoria sconosciuta

    # Scala le features
    new_car_scaled = preprocessor.transform(new_car)  # Applica scaling

    # Predici
    predicted_price = model.predict(new_car_scaled)[0]  # Predice prezzo

    print(
        f"💰 Prezzo predetto per la nuova auto: ${predicted_price:.2f}"
    )  # Stampa risultato

    return predicted_price  # Ritorna prezzo predetto


def main():
    """Funzione principale"""
    print("🚀 Avvio analisi previsione prezzo auto...")  # Messaggio avvio

    # Carica dati
    file_path = r"Esercizi\Giorno 13\CarPrice_Assignment.csv"  # Percorso file
    df = load_and_explore_data(file_path)  # Carica dati

    # Preprocessing
    df_processed, categorical_features, numerical_features = preprocess_data(
        df
    )  # Preprocessing

    # Prepara features e target
    X = df_processed.drop("price", axis=1)  # Features
    y = df_processed["price"]  # Target

    print(f"\n📏 Shape finale - X: {X.shape}, y: {y.shape}")  # Stampa shape finale

    # Addestra modello
    results, X_test_scaled, y_test, preprocessor, label_encoders = train_model(
        X, y
    )  # Training

    # Visualizza risultati
    model_name = visualize_results(results)  # Visualizzazione
    model = results["model"]  # Estrae modello

    print(f"\n🏆 Modello utilizzato: {model_name}")  # Stampa modello
    print(f"   R²: {results['r2']:.4f}")  # Stampa R2
    print(f"   RMSE: ${results['rmse']:.2f}")  # Stampa RMSE
    print(f"   MAE: ${results['mae']:.2f}")  # Stampa MAE
    print(
        f"   CV R² (media ± std): {results['cv_mean']:.4f} ± {results['cv_std']:.4f}"
    )  # Stampa CV

    # Esempio di predizione
    sample_car = {
        "symboling": 1,
        "fueltype": "gas",
        "aspiration": "std",
        "doornumber": "four",
        "carbody": "sedan",
        "drivewheel": "fwd",
        "enginelocation": "front",
        "wheelbase": 98.8,
        "carlength": 177.8,
        "carwidth": 66.5,
        "carheight": 55.5,
        "curbweight": 2410,
        "enginetype": "ohc",
        "cylindernumber": "four",
        "enginesize": 122,
        "fuelsystem": "2bbl",
        "boreratio": 3.39,
        "stroke": 3.39,
        "compressionratio": 8.6,
        "horsepower": 84,
        "peakrpm": 4800,
        "citympg": 26,
        "highwaympg": 32,
        "brand": "toyota",
    }  # Dizionario esempio auto

    make_predictions(
        model, preprocessor, label_encoders, sample_car
    )  # Predizione esempio

    print("\n✅ Analisi completata!")  # Messaggio fine
    print(
        "📊 Grafico salvato come 'car_price_prediction_results.png'"
    )  # Messaggio salvataggio grafico


if __name__ == "__main__":
    main()  # Esegue main se il file è eseguito direttamente
