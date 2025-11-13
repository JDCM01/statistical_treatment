import pandas as pd
from pathlib import Path

def read_excel_file(path: str = "evaluacion_agropecuaria_2025.xlsx"):
    p = Path(path)
    if not p.exists():
        print(f"File not found: {p}")
        return

    try:
        # Use read_excel for .xlsx files. openpyxl is the recommended engine for modern .xlsx files.
        df = pd.read_excel(p, engine="openpyxl")
        return df
    except ValueError as e:
        # e.g., sheet not found
        print(f"ValueError: {e}")
        return None
    except Exception as e:
        # catch-all for other issues (parsing, permissions, engine missing, etc.)
        print(f"An error occurred: {e}")
        return None

def compute_descriptive_statistics(df: pd.DataFrame):
    if df is not None:
        descriptive_stats = df.agg(
            {
                "area_sembrada": ["min", "max", "median", "mean", "skew", "std", "sum", "var", "kurt"],
                "area_cosechada": ["min", "max", "median", "mean", "skew", "std", "sum", "var", "kurt"],
                "produccion": ["min", "max", "median", "mean", "skew", "std", "sum", "var", "kurt"], 
                "rendimiento": ["min", "max", "median", "mean", "skew", "std", "sum", "var", "kurt"]
           }
        )
        return descriptive_stats
    else:
        return None

def compute_range(df):
    if df is not None:
        range_stats = df.agg(
            {
                "area_sembrada": lambda x: x.max() - x.min(),
                "area_cosechada": lambda x: x.max() - x.min(),
                "produccion": lambda x: x.max() - x.min(),
                "rendimiento": lambda x: x.max() - x.min()
           }
        )
        return range_stats

def mode(data):
    frequency = {}
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_count = max(frequency.values())
    return max_count

def analyze_data(df: pd.DataFrame):
    df = read_excel_file()
    if df is not None:
        descriptive_statistics_df = compute_descriptive_statistics(df)
        range_statistics_df = compute_range(df)
        mode_area_sembrada = mode(df["area_sembrada"])
        mode_area_cosechada = mode(df["area_cosechada"])
        mode_produccion = mode(df["produccion"])
        mode_rendimiento = mode(df["rendimiento"])
        print("Descriptive Statistics:")
        print(descriptive_statistics_df)
        print("La moda en hectareas del area sembrada es: ", mode_area_sembrada)
        print("La moda en hectareas del area cosechada es: ", mode_area_cosechada)
        print("La moda en toneladas de la produccion es: ", mode_produccion)
        print("La moda en toneladas por hectarea del rendimiento es: ", mode_rendimiento)
        print("rango de las estadisticas: ", range_statistics_df)
        return df
    else:
        return None
    
def obtain_data():
    df = read_excel_file()
    if df is not None:
        return df
    
analyze_data(read_excel_file())

    
    
    