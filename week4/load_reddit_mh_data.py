import pandas as pd
import glob

def load_reddit_data(file_pattern, chunk_size=None):

    try:
        # Get list of all CSV files matching the pattern
        csv_files = glob.glob(file_pattern)
        
        if not csv_files:
            raise FileNotFoundError(f"No CSV files found matching pattern: {file_pattern}")
            
        print(f"Found {len(csv_files)} CSV files")
        
        # List to store all dataframes
        dfs = []
        
        for file_path in csv_files:
            print(f"\nProcessing file: {file_path}")
            
            if chunk_size:
                # Read in chunks
                chunk_list = []
                for chunk in pd.read_csv(file_path, chunksize=chunk_size, encoding='utf-8'):
                    chunk_list.append(chunk)
                df = pd.concat(chunk_list)
            else:
                # Read entire file
                df = pd.read_csv(file_path, encoding='utf-8')
            
            dfs.append(df)
        
        # Combine all dataframes
        final_df = pd.concat(dfs, ignore_index=True)
        
        # Display basic information about the dataset
        print("\nDataset Info:")
        print(f"Total rows: {len(final_df)}")
        print(f"Columns: {final_df.columns.tolist()}")
        print("\nFirst 5 rows:")
        print(final_df.head())
        
        # Display dataset description
        print("\nDataset Description:")
        print(final_df.describe(include='all'))
        
        # Display data types and non-null counts
        print("\nDataset Details:")
        print(final_df.info())
        
        return final_df
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    data_path = "./week4/dataset/3941387/*.csv"
    df = load_reddit_data(data_path, chunk_size=200)
