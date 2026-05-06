
import json
import pytest
import pandas as pd
from pathlib import Path

# --- Shared Test Data ---------------------------------------------------
@pytest.fixture
def sample_data():
    """Mimics exact structure returned by Open-Meteo API."""
    return {
        "latitude": 40.71,
        "longitude": -74.01,
        "hourly": {
            "time":                  ["2025-06-01T00:00","2025-06-01T01:00",
                                      "2025-06-02T00:00","2025-06-02T01:00"],
            "temperature_2m":        [22.0, 23.5, 30.1, 31.0],
            "apparent_temperature":  [21.0, 22.0, 28.5, 30.0],
            "relative_humidity_2m":  [60, 62, 70, 68],
            "precipitation":         [0.0, 1.2, 0.0, 0.5],
            "windspeed_10m":         [10.0, 12.0, 8.0, 15.0],
        }
    }

@pytest.fixture
def raw_df(sample_data):
    return pd.DataFrame(sample_data["hourly"])

# --- TEST 1: API Schema Validation --------------------------------------
class TestAPISchema:
    """Checks the raw API response has correct structure."""

    def test_all_required_keys_present(self, sample_data):
        required = {"time","temperature_2m","apparent_temperature",
                    "relative_humidity_2m","precipitation","windspeed_10m"}
        actual = set(sample_data["hourly"].keys())
        missing = required - actual
        assert not missing, f"Missing keys: {missing}"

    def test_all_arrays_same_length(self, sample_data):
        lengths = [len(v) for v in sample_data["hourly"].values()]
        assert len(set(lengths)) == 1, "Arrays have different lengths!"

    def test_humidity_between_0_and_100(self, sample_data):
        for h in sample_data["hourly"]["relative_humidity_2m"]:
            assert 0 <= h <= 100, f"Invalid humidity: {h}"

    def test_precipitation_not_negative(self, sample_data):
        for p in sample_data["hourly"]["precipitation"]:
            assert p >= 0, f"Negative precipitation: {p}"

# --- TEST 2: Transformation Logic ---------------------------------------
class TestTransformation:
    """Checks the transform logic produces correct results."""

    def get_transformed(self, raw_df):
        df = raw_df.copy()
        df["time"] = pd.to_datetime(df["time"])
        df["date"] = df["time"].dt.date
        df.rename(columns={
            "temperature_2m":        "temp_c",
            "apparent_temperature":  "feels_like_c",
            "relative_humidity_2m":  "humidity_pct",
            "precipitation":         "precip_mm",
            "windspeed_10m":         "wind_kmh",
        }, inplace=True)
        df["is_raining"] = df["precip_mm"] > 0.0
        return df

    def test_rain_flag_is_correct(self, raw_df):
        df = self.get_transformed(raw_df)
        for _, row in df.iterrows():
            expected = row["precip_mm"] > 0.0
            assert row["is_raining"] == expected

    def test_renamed_columns_exist(self, raw_df):
        df = self.get_transformed(raw_df)
        for col in ["temp_c","feels_like_c","humidity_pct","precip_mm","wind_kmh"]:
            assert col in df.columns, f"Missing column: {col}"

    def test_daily_summary_row_count(self, raw_df):
        df = self.get_transformed(raw_df)
        daily = df.groupby("date").agg(temp_max=("temp_c","max")).reset_index()
        assert len(daily) == df["date"].nunique()

# --- TEST 3: File I/O ---------------------------------------------------
class TestFileIO:
    """Checks files are correctly saved to disk."""

    def test_json_is_valid_and_has_hourly_key(self, sample_data, tmp_path):
        path = tmp_path / "test.json"
        with open(path, "w") as f:
            json.dump(sample_data, f)
        with open(path) as f:
            loaded = json.load(f)
        assert "hourly" in loaded

    def test_csv_row_count_matches_data(self, sample_data, tmp_path):
        df = pd.DataFrame(sample_data["hourly"])
        path = tmp_path / "test.csv"
        df.to_csv(path, index=False)
        loaded = pd.read_csv(path)
        assert len(loaded) == len(sample_data["hourly"]["time"])

    def test_csv_columns_match_api_keys(self, sample_data, tmp_path):
        df = pd.DataFrame(sample_data["hourly"])
        path = tmp_path / "test.csv"
        df.to_csv(path, index=False)
        loaded = pd.read_csv(path)
        assert set(loaded.columns) == set(sample_data["hourly"].keys())
