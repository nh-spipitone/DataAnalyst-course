import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import warnings

warnings.filterwarnings("ignore")

# Configurazione per i grafici
plt.style.use("seaborn-v0_8")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 10


class StockMarketAnalyzer:
    def __init__(self, file_path):
        """Inizializza l'analizzatore caricando i dati"""
        self.df = pd.read_csv(file_path)
        self.prepare_data()

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


def main():
    """Funzione principale"""
    print("🚀 ANALISI COMPLETA DEL MERCATO AZIONARIO")
    print("=" * 70)

    try:
        # Inizializza l'analizzatore
        analyzer = StockMarketAnalyzer(r"Esercizi\Giorno 16\stock_market_june2025.csv")

        # Esegui l'analisi completa
        analyzer.exploratory_analysis()
        analyzer.create_visualizations()
        analyzer.sector_analysis()

        # Addestra il modello di predizione
        model, features, encoder = analyzer.train_prediction_model()

        # Genera insights finali
        analyzer.generate_insights()

        print("\n✅ ANALISI COMPLETATA CON SUCCESSO!")
        print("📁 File generati:")
        print("   • stock_market_analysis.png (grafici principali)")
        print("   • prediction_results.png (risultati del modello)")

    except FileNotFoundError:
        print("❌ Errore: File 'stock_market_june2025.csv' non trovato!")
        print("   Assicurati che il file sia nella stessa cartella dello script.")
    except Exception as e:
        print(f"❌ Errore durante l'esecuzione: {str(e)}")


if __name__ == "__main__":
    main()
