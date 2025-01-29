import kagglehub
import pandas as pd
import os


def download_reddit_data_kaggle(destination_folder):
    try:
        # Ensure the folder exists
        os.makedirs(destination_folder, exist_ok=True)
        
        # Update to the correct dataset URL
        dataset_name = "kamaruladha/mental-health-in-tech-survey-2016"
        
        # Download the dataset to the specified folder
        path = kagglehub.dataset_download(dataset_name, destination_folder)
        print(f"Successfully downloaded dataset to: {path}")
        return path
        
    except kagglehub.exceptions.KaggleApiHTTPError as e:
        print(f"Error downloading dataset: {e}")
        print("\nPlease ensure:")
        print("1. You have a valid Kaggle account")
        print("2. You have accepted the dataset terms on Kaggle")
        print("3. You have configured your Kaggle API credentials")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def load_reddit_data_csv(file_path, chunk_size=None):
    try:
        # For CSV files:
        chunk_generator = pd.read_csv(file_path, chunksize=chunk_size, encoding='utf-8')
        
        for chunk in chunk_generator:
            print(f"Loaded chunk with {len(chunk)} rows.")
            # Process your chunks here
            
        return chunk_generator
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Download the data
    #data_path = download_reddit_data_kaggle("./dataset")
    
    # Load the data
    current_path = os.getcwd()
    # csv_file = current_path +"/dataset/reddit-mental-health-data/versions/1/data_to_be_cleansed.csv" # Update filename as needed
    csv_file = "/Users/bo/Desktop/uni_of_the_cumberland/Spring2025/MSAI-532/week4/dataset/reddit-mental-health-data/versions/1/data_to_be_cleansed.csv"
    load_reddit_data_csv(csv_file, chunk_size=200)



    