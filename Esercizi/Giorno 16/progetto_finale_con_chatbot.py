import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import warnings
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

warnings.filterwarnings("ignore")

# Carica le variabili d'ambiente
load_dotenv()

# Configurazione per i grafici
plt.style.use("seaborn-v0_8")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 10

# Variabile globale per il dataframe
df_global = None
analyzer_global = None


class StockMarketAnalyzer:
    def __init__(self, file_path):
        """Inizializza l'analizzatore caricando i dati"""
        self.df = pd.read_csv(file_path)
        self.prepare_data()
        # Rendi il dataframe disponibile globalmente per il chatbot
        global df_global, analyzer_global
        df_global = self.df
        analyzer_global = self

    def prepare_data(self):
        """Prepara e pulisce i dati"""
        print("🔄 Preparazione dei dati...")

        # Converti la data
        self.df["Date"] = pd.to_datetime(self.df["Date"], format="%d-%m-%Y")

        # Crea nuove features
        self.df["Price_Range"] = self.df["High Price"] - self.df["Low Price"]
        self.df["Daily_Return"] = (
            (self.df["Close Price"] - self.df["Open Price"]) / self.df["Open Price"]
        ) * 100
        self.df["Volatility"] = (self.df["Price_Range"] / self.df["Open Price"]) * 100
        self.df["Volume_Million"] = self.df["Volume Traded"] / 1_000_000
        self.df["Market_Cap_Billion"] = self.df["Market Cap"] / 1_000_000_000

        # Rimuovi valori NaN
        self.df = self.df.dropna()

        print(
            f"✅ Dati preparati: {len(self.df)} righe, {len(self.df.columns)} colonne"
        )
        print(
            f"📅 Periodo: {self.df['Date'].min().strftime('%d/%m/%Y')} - {self.df['Date'].max().strftime('%d/%m/%Y')}"
        )

    def exploratory_analysis(self):
        """Analisi esplorativa dei dati"""
        print("\n" + "=" * 50)
        print("📊 ANALISI ESPLORATIVA DEI DATI")
        print("=" * 50)

        # Informazioni generali
        print(f"🏢 Numero di aziende uniche: {self.df['Ticker'].nunique()}")
        print(f"🏭 Settori rappresentati: {self.df['Sector'].nunique()}")
        print(
            f"📈 Range prezzi: ${self.df['Close Price'].min():.2f} - ${self.df['Close Price'].max():.2f}"
        )
        print(f"💰 Market Cap medio: ${self.df['Market_Cap_Billion'].mean():.2f}B")

        # Statistiche descrittive
        print("\n📋 Statistiche descrittive principali:")
        stats_cols = [
            "Close Price",
            "Daily_Return",
            "Volatility",
            "PE Ratio",
            "Dividend Yield",
        ]
        print(self.df[stats_cols].describe().round(2))

        # Top 10 aziende per Market Cap
        print("\n🏆 Top 10 aziende per Market Cap:")
        top_companies = self.df.nlargest(10, "Market_Cap_Billion")[
            ["Ticker", "Sector", "Market_Cap_Billion", "Close Price"]
        ]
        for idx, row in top_companies.iterrows():
            print(
                f"{row['Ticker']:>6} | {row['Sector']:<20} | ${row['Market_Cap_Billion']:>8.1f}B | ${row['Close Price']:>7.2f}"
            )

    def create_visualizations(self):
        """Crea visualizzazioni dei dati"""
        print("\n📈 Creazione visualizzazioni...")

        # Setup della figura con subplots
        fig = plt.figure(figsize=(20, 24))

        # 1. Distribuzione dei prezzi di chiusura
        plt.subplot(4, 2, 1)
        plt.hist(
            self.df["Close Price"],
            bins=50,
            alpha=0.7,
            color="skyblue",
            edgecolor="black",
        )
        plt.title(
            "Distribuzione dei Prezzi di Chiusura", fontsize=14, fontweight="bold"
        )
        plt.xlabel("Prezzo di Chiusura ($)")
        plt.ylabel("Frequenza")
        plt.grid(True, alpha=0.3)

        # 2. Market Cap per Settore
        plt.subplot(4, 2, 2)
        sector_marketcap = (
            self.df.groupby("Sector")["Market_Cap_Billion"]
            .sum()
            .sort_values(ascending=True)
        )
        plt.barh(
            range(len(sector_marketcap)), sector_marketcap.values, color="lightcoral"
        )
        plt.yticks(range(len(sector_marketcap)), sector_marketcap.index, fontsize=10)
        plt.title("Market Cap Totale per Settore", fontsize=14, fontweight="bold")
        plt.xlabel("Market Cap (Miliardi $)")
        plt.grid(True, alpha=0.3, axis="x")

        # 3. Relazione PE Ratio vs Dividend Yield
        plt.subplot(4, 2, 3)
        scatter = plt.scatter(
            self.df["PE Ratio"],
            self.df["Dividend Yield"],
            c=self.df["Market_Cap_Billion"],
            cmap="viridis",
            alpha=0.6,
            s=30,
        )
        plt.colorbar(scatter, label="Market Cap (Miliardi $)")
        plt.title("PE Ratio vs Dividend Yield", fontsize=14, fontweight="bold")
        plt.xlabel("PE Ratio")
        plt.ylabel("Dividend Yield (%)")
        plt.grid(True, alpha=0.3)

        # 4. Volatilità per Settore
        plt.subplot(4, 2, 4)
        sector_volatility = (
            self.df.groupby("Sector")["Volatility"].mean().sort_values(ascending=False)
        )
        colors = plt.cm.Set3(np.linspace(0, 1, len(sector_volatility)))
        plt.bar(range(len(sector_volatility)), sector_volatility.values, color=colors)
        plt.xticks(
            range(len(sector_volatility)),
            sector_volatility.index,
            rotation=45,
            ha="right",
        )
        plt.title("Volatilità Media per Settore", fontsize=14, fontweight="bold")
        plt.ylabel("Volatilità (%)")
        plt.grid(True, alpha=0.3, axis="y")

        # 5. Volume vs Prezzo
        plt.subplot(4, 2, 5)
        plt.scatter(
            self.df["Volume_Million"],
            self.df["Close Price"],
            alpha=0.5,
            s=20,
            color="orange",
        )
        plt.title("Volume di Trading vs Prezzo", fontsize=14, fontweight="bold")
        plt.xlabel("Volume (Milioni)")
        plt.ylabel("Prezzo di Chiusura ($)")
        plt.grid(True, alpha=0.3)

        # 6. Trend temporale dei prezzi medi
        plt.subplot(4, 2, 6)
        daily_avg = self.df.groupby("Date")["Close Price"].mean()
        plt.plot(daily_avg.index, daily_avg.values, linewidth=2, color="green")
        plt.title("Trend del Prezzo Medio nel Tempo", fontsize=14, fontweight="bold")
        plt.xlabel("Data")
        plt.ylabel("Prezzo Medio ($)")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)

        # 7. Heatmap delle correlazioni
        plt.subplot(4, 2, 7)
        corr_cols = [
            "Close Price",
            "PE Ratio",
            "Dividend Yield",
            "EPS",
            "Volatility",
            "Volume_Million",
        ]
        correlation_matrix = self.df[corr_cols].corr()
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="coolwarm",
            center=0,
            square=True,
            fmt=".2f",
            cbar_kws={"shrink": 0.8},
        )
        plt.title("Matrice di Correlazione", fontsize=14, fontweight="bold")

        # 8. Distribuzione dei rendimenti giornalieri
        plt.subplot(4, 2, 8)
        plt.hist(
            self.df["Daily_Return"],
            bins=50,
            alpha=0.7,
            color="lightgreen",
            edgecolor="black",
        )
        plt.axvline(
            self.df["Daily_Return"].mean(),
            color="red",
            linestyle="--",
            label=f'Media: {self.df["Daily_Return"].mean():.2f}%',
        )
        plt.title(
            "Distribuzione dei Rendimenti Giornalieri", fontsize=14, fontweight="bold"
        )
        plt.xlabel("Rendimento Giornaliero (%)")
        plt.ylabel("Frequenza")
        plt.legend()
        plt.grid(True, alpha=0.3)

        plt.tight_layout(pad=3.0)
        plt.savefig("stock_market_analysis.png", dpi=300, bbox_inches="tight")
        plt.show()

        print("✅ Visualizzazioni create e salvate come 'stock_market_analysis.png'")

    def sector_analysis(self):
        """Analisi dettagliata per settore"""
        print("\n🏭 ANALISI PER SETTORE")
        print("=" * 50)

        sector_stats = (
            self.df.groupby("Sector")
            .agg(
                {
                    "Close Price": ["mean", "std", "min", "max"],
                    "Market_Cap_Billion": ["sum", "mean"],
                    "PE Ratio": "mean",
                    "Dividend Yield": "mean",
                    "Daily_Return": "mean",
                    "Volatility": "mean",
                    "Ticker": "count",
                }
            )
            .round(2)
        )

        # Flatten column names
        sector_stats.columns = ["_".join(col).strip() for col in sector_stats.columns]
        sector_stats = sector_stats.rename(columns={"Ticker_count": "Num_Companies"})

        print(sector_stats)

        # Trova il settore più performante
        best_sector = sector_stats.loc[sector_stats["Daily_Return_mean"].idxmax()]
        worst_sector = sector_stats.loc[sector_stats["Daily_Return_mean"].idxmin()]

        print(f"\n🥇 Settore più performante: {best_sector.name}")
        print(f"   Rendimento medio: {best_sector['Daily_Return_mean']:.2f}%")
        print(f"🥉 Settore meno performante: {worst_sector.name}")
        print(f"   Rendimento medio: {worst_sector['Daily_Return_mean']:.2f}%")

    def prepare_ml_features(self):
        """Prepara le features per il machine learning"""
        print("\n🤖 Preparazione features per Machine Learning...")

        # Seleziona le features numeriche
        feature_columns = [
            "Open Price",
            "High Price",
            "Low Price",
            "Volume_Million",
            "PE Ratio",
            "Dividend Yield",
            "EPS",
            "Price_Range",
            "Volatility",
        ]

        # Aggiungi encoding per il settore
        le = LabelEncoder()
        self.df["Sector_Encoded"] = le.fit_transform(self.df["Sector"])
        feature_columns.append("Sector_Encoded")

        # Rimuovi outliers estremi
        Q1 = self.df["Close Price"].quantile(0.25)
        Q3 = self.df["Close Price"].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        self.df_clean = self.df[
            (self.df["Close Price"] >= lower_bound)
            & (self.df["Close Price"] <= upper_bound)
        ].copy()

        # Prepara X e y
        X = self.df_clean[feature_columns]
        y = self.df_clean["Close Price"]

        # Rimuovi righe con valori mancanti
        mask = ~(
            X.isin([np.inf, -np.inf]).any(axis=1) | X.isna().any(axis=1) | y.isna()
        )
        X = X[mask]
        y = y[mask]

        print(
            f"✅ Dataset preparato: {len(X)} campioni, {len(feature_columns)} features"
        )
        print(f"📊 Target range: ${y.min():.2f} - ${y.max():.2f}")

        return X, y, feature_columns, le

    def train_prediction_model(self):
        """Addestra il modello di regressione lineare"""
        print("\n🎯 MODELLO DI PREDIZIONE PREZZI AZIONARI")
        print("=" * 50)

        # Prepara i dati
        X, y, feature_columns, label_encoder = self.prepare_ml_features()

        # Split train/test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Addestra il modello
        print("🚀 Addestramento del modello...")
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predizioni
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        # Metriche
        train_r2 = r2_score(y_train, y_pred_train)
        test_r2 = r2_score(y_test, y_pred_test)
        train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

        print(f"\n📈 PERFORMANCE DEL MODELLO:")
        print(f"🎯 R² Score (Training): {train_r2:.4f}")
        print(f"🎯 R² Score (Test): {test_r2:.4f}")
        print(f"📏 RMSE (Training): ${train_rmse:.2f}")
        print(f"📏 RMSE (Test): ${test_rmse:.2f}")

        # Feature importance
        feature_importance = pd.DataFrame(
            {"Feature": feature_columns, "Importance": abs(model.coef_)}
        ).sort_values("Importance", ascending=False)

        print(f"\n🔍 IMPORTANZA DELLE FEATURES:")
        for idx, row in feature_importance.head(10).iterrows():
            print(f"{row['Feature']:<20}: {row['Importance']:.4f}")

        # Visualizzazione dei risultati
        self.plot_prediction_results(y_test, y_pred_test, feature_importance)

        # Esempio di predizione
        self.make_sample_predictions(model, X_test, feature_columns, label_encoder)

        return model, feature_columns, label_encoder

    def plot_prediction_results(self, y_test, y_pred_test, feature_importance):
        """Visualizza i risultati del modello"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

        # 1. Predetto vs Reale
        ax1.scatter(y_test, y_pred_test, alpha=0.6, s=30)
        ax1.plot(
            [y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2
        )
        ax1.set_xlabel("Prezzo Reale ($)")
        ax1.set_ylabel("Prezzo Predetto ($)")
        ax1.set_title("Predizioni vs Valori Reali")
        ax1.grid(True, alpha=0.3)

        # 2. Residui
        residuals = y_test - y_pred_test
        ax2.scatter(y_pred_test, residuals, alpha=0.6, s=30)
        ax2.axhline(y=0, color="r", linestyle="--")
        ax2.set_xlabel("Prezzo Predetto ($)")
        ax2.set_ylabel("Residui ($)")
        ax2.set_title("Grafico dei Residui")
        ax2.grid(True, alpha=0.3)

        # 3. Distribuzione degli errori
        ax3.hist(residuals, bins=30, alpha=0.7, color="lightblue", edgecolor="black")
        ax3.axvline(
            residuals.mean(),
            color="red",
            linestyle="--",
            label=f"Media: ${residuals.mean():.2f}",
        )
        ax3.set_xlabel("Errore di Predizione ($)")
        ax3.set_ylabel("Frequenza")
        ax3.set_title("Distribuzione degli Errori")
        ax3.legend()
        ax3.grid(True, alpha=0.3)

        # 4. Feature Importance
        top_features = feature_importance.head(8)
        ax4.barh(
            range(len(top_features)), top_features["Importance"], color="lightgreen"
        )
        ax4.set_yticks(range(len(top_features)))
        ax4.set_yticklabels(top_features["Feature"])
        ax4.set_xlabel("Importanza (Coefficiente Assoluto)")
        ax4.set_title("Top 8 Feature più Importanti")
        ax4.grid(True, alpha=0.3, axis="x")

        plt.tight_layout()
        plt.savefig("prediction_results.png", dpi=300, bbox_inches="tight")
        plt.show()

    def make_sample_predictions(self, model, X_test, feature_columns, label_encoder):
        """Fa predizioni di esempio"""
        print(f"\n🔮 ESEMPI DI PREDIZIONI:")
        print("=" * 50)

        # Prendi alcuni esempi casuali
        sample_indices = np.random.choice(X_test.index, size=5, replace=False)

        for idx in sample_indices:
            real_price = self.df_clean.loc[idx, "Close Price"]
            predicted_price = model.predict(X_test.loc[[idx]])[0]
            ticker = self.df_clean.loc[idx, "Ticker"]
            sector = self.df_clean.loc[idx, "Sector"]

            error = abs(real_price - predicted_price)
            error_pct = (error / real_price) * 100

            print(f"🏢 {ticker} ({sector})")
            print(f"   💰 Prezzo Reale: ${real_price:.2f}")
            print(f"   🎯 Prezzo Predetto: ${predicted_price:.2f}")
            print(f"   📊 Errore: ${error:.2f} ({error_pct:.1f}%)")
            print()

    def generate_insights(self):
        """Genera insights e conclusioni"""
        print("\n💡 INSIGHTS E CONCLUSIONI")
        print("=" * 70)

        # Statistiche generali
        print("📊 STATISTICHE GENERALI:")
        print(f"   • Media prezzi: ${self.df['Close Price'].mean():.2f}")
        print(f"   • Volatilità media: {self.df['Volatility'].mean():.2f}%")
        print(
            f"   • Rendimento medio giornaliero: {self.df['Daily_Return'].mean():.3f}%"
        )

        # Settore più volatile
        most_volatile_sector = self.df.groupby("Sector")["Volatility"].mean().idxmax()
        print(f"   • Settore più volatile: {most_volatile_sector}")

        # Azienda con PE ratio più alto
        highest_pe = self.df.loc[self.df["PE Ratio"].idxmax()]
        print(
            f"   • PE Ratio più alto: {highest_pe['Ticker']} ({highest_pe['PE Ratio']:.1f})"
        )

        # Azienda con dividend yield più alto
        highest_div = self.df.loc[self.df["Dividend Yield"].idxmax()]
        print(
            f"   • Dividend Yield più alto: {highest_div['Ticker']} ({highest_div['Dividend Yield']:.2f}%)"
        )

        print("\n🎯 CONCLUSIONI DELL'ANALISI:")
        print(
            "   1. Il modello di regressione lineare fornisce una buona base per predire i prezzi"
        )
        print(
            "   2. Le features più importanti sono tipicamente il prezzo di apertura e i dati storici"
        )
        print("   3. La volatilità varia significativamente tra i settori")
        print(
            "   4. Esiste una correlazione interessante tra PE Ratio e Dividend Yield"
        )
        print("   5. Il volume di trading può influenzare la stabilità dei prezzi")

        print("\n⚠️  LIMITAZIONI DEL MODELLO:")
        print("   • I dati coprono solo il mese di giugno 2025")
        print(
            "   • La regressione lineare potrebbe non catturare relazioni non lineari"
        )
        print("   • Fattori esterni (notizie, eventi) non sono considerati")
        print("   • Prestazioni passate non garantiscono risultati futuri")


# =================== FUNZIONI CHATBOT OpenAI ===================


def analyze_data(analysis_type, column=None, group_by=None):
    """Analizza i dati del mercato azionario usando pandas"""
    global df_global

    if df_global is None:
        return "❌ Dati non caricati. Esegui prima l'analisi principale."

    try:
        df = df_global.copy()

        if analysis_type == "summary":
            numeric_cols = [
                "Close Price",
                "Daily_Return",
                "Volatility",
                "PE Ratio",
                "Dividend Yield",
            ]
            return f"📊 Statistiche descrittive:\n{df[numeric_cols].describe().to_string()}"

        elif analysis_type == "mean":
            if column and column in df.columns:
                result = df[column].mean()
                return f"📈 Media di {column}: {result:.3f}"
            return f"❌ Colonna '{column}' non trovata. Colonne disponibili: {', '.join(df.columns)}"

        elif analysis_type == "group_by":
            if group_by and column and group_by in df.columns and column in df.columns:
                result = (
                    df.groupby(group_by)[column].agg(["mean", "std", "count"]).round(3)
                )
                return f"📊 Analisi di {column} per {group_by}:\n{result.to_string()}"
            return f"❌ Specificare colonne valide per group_by"

        elif analysis_type == "correlation":
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()
                return (
                    f"🔗 Matrice di correlazione:\n{corr_matrix.round(3).to_string()}"
                )
            return "❌ Non ci sono abbastanza colonne numeriche per la correlazione"

        elif analysis_type == "top_performers":
            if column and column in df.columns:
                top_10 = df.nlargest(10, column)[["Ticker", "Sector", column]]
                return f"🏆 Top 10 per {column}:\n{top_10.to_string()}"
            return f"❌ Colonna '{column}' non trovata"

        elif analysis_type == "sector_analysis":
            sector_stats = (
                df.groupby("Sector")
                .agg(
                    {
                        "Close Price": ["mean", "std"],
                        "Daily_Return": "mean",
                        "Volatility": "mean",
                        "Market_Cap_Billion": "mean",
                        "Ticker": "count",
                    }
                )
                .round(3)
            )
            sector_stats.columns = [
                "_".join(col).strip() for col in sector_stats.columns
            ]
            return f"🏭 Analisi per settore:\n{sector_stats.to_string()}"

        else:
            return "❌ Tipo di analisi non supportato. Usa: summary, mean, group_by, correlation, top_performers, sector_analysis"

    except Exception as e:
        return f"❌ Errore nell'analisi: {str(e)}"


def create_plot(plot_type, x_column=None, y_column=None, title="Grafico Stock Market"):
    """Crea grafici sui dati del mercato azionario"""
    global df_global

    if df_global is None:
        return "❌ Dati non caricati. Esegui prima l'analisi principale."

    try:
        df = df_global.copy()

        plt.figure(figsize=(12, 8))

        if plot_type == "scatter":
            if (
                x_column
                and y_column
                and x_column in df.columns
                and y_column in df.columns
            ):
                plt.scatter(df[x_column], df[y_column], alpha=0.6, s=60)
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(title)
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                filename = f"scatter_{x_column}_{y_column}.png"
                plt.savefig(filename, dpi=300, bbox_inches="tight")
                plt.show()
                return f"✅ Scatter plot creato: {filename}"
            return "❌ Specificare colonne x e y valide per scatter plot"

        elif plot_type == "bar":
            if (
                x_column
                and y_column
                and x_column in df.columns
                and y_column in df.columns
            ):
                # Prendi top 15 per evitare grafici troppo affollati
                df_plot = df.nlargest(15, y_column)
                plt.bar(
                    df_plot[x_column], df_plot[y_column], alpha=0.7, color="lightblue"
                )
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(title)
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3, axis="y")
                plt.tight_layout()
                filename = f"bar_{x_column}_{y_column}.png"
                plt.savefig(filename, dpi=300, bbox_inches="tight")
                plt.show()
                return f"✅ Grafico a barre creato: {filename}"
            return "❌ Specificare colonne x e y valide per grafico a barre"

        elif plot_type == "histogram":
            if x_column and x_column in df.columns:
                plt.hist(
                    df[x_column],
                    bins=30,
                    alpha=0.7,
                    color="lightgreen",
                    edgecolor="black",
                )
                plt.xlabel(x_column)
                plt.ylabel("Frequenza")
                plt.title(f"Distribuzione di {x_column}")
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                filename = f"histogram_{x_column}.png"
                plt.savefig(filename, dpi=300, bbox_inches="tight")
                plt.show()
                return f"✅ Istogramma creato: {filename}"
            return "❌ Specificare una colonna valida per l'istogramma"

        elif plot_type == "line":
            if (
                x_column
                and y_column
                and x_column in df.columns
                and y_column in df.columns
            ):
                # Ordina per x_column se è una data
                if "Date" in x_column:
                    df = df.sort_values(x_column)
                plt.plot(
                    df[x_column], df[y_column], marker="o", linewidth=2, markersize=4
                )
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(title)
                plt.grid(True, alpha=0.3)
                plt.xticks(rotation=45)
                plt.tight_layout()
                filename = f"line_{x_column}_{y_column}.png"
                plt.savefig(filename, dpi=300, bbox_inches="tight")
                plt.show()
                return f"✅ Grafico a linea creato: {filename}"
            return "❌ Specificare colonne x e y valide per grafico a linea"

        else:
            return (
                "❌ Tipo di grafico non supportato. Usa: scatter, bar, histogram, line"
            )

    except Exception as e:
        return f"❌ Errore nella creazione del grafico: {str(e)}"


def show_data(rows):
    """Mostra i dati del dataset"""
    global df_global

    if df_global is None:
        return "❌ Dati non caricati. Esegui prima l'analisi principale."

    try:
        if rows == -1:
            return f"📊 Dataset completo:\n{df_global.to_string()}"
        else:
            return f"📊 Prime {rows} righe del dataset:\n{df_global.head(rows).to_string()}"
    except Exception as e:
        return f"❌ Errore nel mostrare i dati: {str(e)}"


def get_stock_info(ticker):
    """Ottieni informazioni su un'azienda specifica"""
    global df_global

    if df_global is None:
        return "❌ Dati non caricati. Esegui prima l'analisi principale."

    try:
        company = df_global[
            df_global["Ticker"].str.contains(ticker, case=False, na=False)
        ]
        if not company.empty:
            info = company.iloc[0]
            return f"""
🏢 Informazioni per {info['Ticker']}:
   💰 Prezzo di chiusura: ${info['Close Price']:.2f}
   🏭 Settore: {info['Sector']}
   📊 PE Ratio: {info['PE Ratio']:.2f}
   💵 Dividend Yield: {info['Dividend Yield']:.2f}%
   📈 Rendimento giornaliero: {info['Daily_Return']:.2f}%
   🌊 Volatilità: {info['Volatility']:.2f}%
   💎 Market Cap: ${info['Market_Cap_Billion']:.2f}B
            """
        return f"❌ Azienda '{ticker}' non trovata"
    except Exception as e:
        return f"❌ Errore nel recupero informazioni: {str(e)}"


# =================== FUNCTION CALLING ===================


def function_calling(tool_calls):
    """Gestisce le chiamate agli strumenti"""
    results = []

    for tool_call in tool_calls:
        if tool_call.function.name == "analyze_data":
            args = json.loads(tool_call.function.arguments)
            result = analyze_data(args.get("analysis_type"))
            results.append(result)

        elif tool_call.function.name == "analyze_data_with_column":
            args = json.loads(tool_call.function.arguments)
            result = analyze_data(
                args.get("analysis_type"), args.get("column"), args.get("group_by")
            )
            results.append(result)

        elif tool_call.function.name == "create_plot":
            args = json.loads(tool_call.function.arguments)
            result = create_plot(
                args.get("plot_type"),
                args.get("x_column"),
                args.get("y_column"),
                args.get("title"),
            )
            results.append(result)

        elif tool_call.function.name == "show_data":
            args = json.loads(tool_call.function.arguments)
            result = show_data(args.get("rows"))
            results.append(result)

        elif tool_call.function.name == "get_stock_info":
            args = json.loads(tool_call.function.arguments)
            result = get_stock_info(args.get("ticker"))
            results.append(result)

    return "\n\n".join(results)


# =================== STRUMENTI OPENAI ===================

tools = [
    {
        "type": "function",
        "function": {
            "name": "analyze_data",
            "description": "Analizza i dati usando pandas. Supporta: summary, correlation, sector_analysis",
            "parameters": {
                "type": "object",
                "properties": {
                    "analysis_type": {
                        "type": "string",
                        "enum": ["summary", "correlation", "sector_analysis"],
                        "description": "Tipo di analisi da eseguire",
                    }
                },
                "required": ["analysis_type"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "analyze_data_with_column",
            "description": "Analizza i dati con colonne specifiche (per mean, group_by, top_performers)",
            "parameters": {
                "type": "object",
                "properties": {
                    "analysis_type": {
                        "type": "string",
                        "enum": ["mean", "group_by", "top_performers"],
                        "description": "Tipo di analisi da eseguire",
                    },
                    "column": {
                        "type": "string",
                        "description": "Nome della colonna da analizzare",
                    },
                    "group_by": {
                        "type": "string",
                        "description": "Colonna per il raggruppamento (solo per group_by)",
                    },
                },
                "required": ["analysis_type", "column", "group_by"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_plot",
            "description": "Crea grafici usando matplotlib. Supporta: scatter, bar, histogram, line",
            "parameters": {
                "type": "object",
                "properties": {
                    "plot_type": {
                        "type": "string",
                        "enum": ["scatter", "bar", "histogram", "line"],
                        "description": "Tipo di grafico da creare",
                    },
                    "x_column": {
                        "type": "string",
                        "description": "Nome della colonna per l'asse x",
                    },
                    "y_column": {
                        "type": "string",
                        "description": "Nome della colonna per l'asse y",
                    },
                    "title": {"type": "string", "description": "Titolo del grafico"},
                },
                "required": ["plot_type", "x_column", "y_column", "title"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "show_data",
            "description": "Mostra i dati del dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "rows": {
                        "type": "integer",
                        "description": "Numero di righe da mostrare (-1 per tutto il dataset)",
                    }
                },
                "required": ["rows"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_stock_info",
            "description": "Ottieni informazioni dettagliate su un'azienda specifica",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Ticker dell'azienda (es: AAPL, MSFT)",
                    }
                },
                "required": ["ticker"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
]


# =================== CHATBOT INTERFACE ===================


def start_chatbot():
    """Avvia l'interfaccia del chatbot"""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    if not OPENAI_API_KEY:
        print("❌ Errore: OPENAI_API_KEY non trovata nelle variabili d'ambiente")
        print("   Crea un file .env con: OPENAI_API_KEY=your_api_key_here")
        return

    client = OpenAI(api_key=OPENAI_API_KEY)

    print("\n🤖 CHATBOT ANALISI MERCATO AZIONARIO")
    print("=" * 50)
    print("💡 Esempi di domande:")
    print("   • 'Mostra il riepilogo dei dati'")
    print("   • 'Crea un grafico scatter tra PE Ratio e Dividend Yield'")
    print("   • 'Informazioni su AAPL'")
    print("   • 'Analisi per settore'")
    print("   • 'Media dei prezzi di chiusura per settore'")
    print("   • 'Crea istogramma della volatilità'")
    print("\n📝 Scrivi 'exit' per uscire\n")

    messages = [
        {
            "role": "system",
            "content": """Sei un assistente esperto in analisi del mercato azionario. Puoi:
            - Analizzare dati finanziari con pandas
            - Creare grafici e visualizzazioni
            - Fornire informazioni su aziende specifiche
            - Rispondere a domande sui dati del mercato
            
            Usa sempre un linguaggio professionale ma amichevole. Fornisci spiegazioni chiare e actionable insights.""",
        }
    ]

    while True:
        user_input = input("🔍 La tua domanda: ").strip()

        if user_input.lower() == "exit":
            print("👋 Grazie per aver usato il chatbot di analisi azionaria!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=messages[-10:],  # Mantieni solo gli ultimi 10 messaggi
                tools=tools,
                tool_choice="auto",
            )

            assistant_message = response.choices[0].message

            if assistant_message.tool_calls:
                # Esegui le funzioni chiamate
                function_results = function_calling(assistant_message.tool_calls)
                print(f"\n🤖 {function_results}")

                messages.append({"role": "assistant", "content": function_results})
            else:
                # Risposta testuale
                print(f"\n🤖 {assistant_message.content}")
                messages.append(assistant_message)

        except Exception as e:
            print(f"\n❌ Errore nel chatbot: {str(e)}")

        print("\n" + "-" * 50)


def main():
    """Funzione principale"""
    print("🚀 ANALISI COMPLETA DEL MERCATO AZIONARIO CON CHATBOT AI")
    print("=" * 80)

    try:
        # Inizializza l'analizzatore
        analyzer = StockMarketAnalyzer(r"Esercizi\Giorno 16\stock_market_june2025.csv")

        print("\n🎯 Scegli una modalità:")
        print("1. Analisi completa automatica")
        print("2. Chatbot AI interattivo")
        print("3. Entrambe")

        choice = input("\nInserisci la tua scelta (1-3): ").strip()

        if choice in ["1", "3"]:
            print("\n📊 Esecuzione analisi completa...")
            # Esegui l'analisi completa
            analyzer.exploratory_analysis()
            analyzer.create_visualizations()
            analyzer.sector_analysis()

            # Addestra il modello di predizione
            model, features, encoder = analyzer.train_prediction_model()

            # Genera insights finali
            analyzer.generate_insights()

            print("\n✅ ANALISI AUTOMATICA COMPLETATA!")
            print("📁 File generati:")
            print("   • stock_market_analysis.png (grafici principali)")
            print("   • prediction_results.png (risultati del modello)")

        if choice in ["2", "3"]:
            # Avvia il chatbot
            start_chatbot()

    except FileNotFoundError:
        print("❌ Errore: File 'stock_market_june2025.csv' non trovato!")
        print("   Assicurati che il file sia nella stessa cartella dello script.")
    except Exception as e:
        print(f"❌ Errore durante l'esecuzione: {str(e)}")


if __name__ == "__main__":
    main()
