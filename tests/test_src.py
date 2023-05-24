from src import __version__
from src.data import (
    download_one_file_of_raw_data, 
    select_and_rename_raw_columns, 
    validate_raw_data,
    load_raw_data
)

def test_version():
    assert __version__ == '0.1.0'


def test_download_one_file_of_raw_data():
    year = 2020
    month = 1
    download_one_file_of_raw_data(year, month)
    assert True


def test_select_and_rename_raw_columns():
    import pandas as pd

    df = pd.DataFrame(
        columns=[
                'VendorID',
                'tpep_pickup_datetime',
                'tpep_dropoff_datetime',
                'passenger_count',
                'trip_distance',
                'RatecodeID',
                'store_and_fwd_flag',
                'PULocationID',
                'DOLocationID',
                'payment_type',
                'fare_amount',
                'extra',
                'mta_tax',
                'tip_amount',
                'tolls_amount',
                'improvement_surcharge',
                'total_amount',
                'congestion_surcharge',
                'airport_fee'
            ]
    )
    df = select_and_rename_raw_columns(df)
    assert df.columns.tolist() == ['pickup_datetime', 'pickup_location_id']
