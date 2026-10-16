import gzip
import pickle
import threading


def save_data_async(data, filename="students.pkl.gz"):
    def _write_file():
        try:
            with gzip.open(filename, "wb") as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"\n[Success] Data background-saved to {filename}")
        except Exception as e:
            print(f"\n[Error] Failed to save data: {e}")

    thread = threading.Thread(target=_write_file, daemon=True)
    thread.start()
    return thread


def load_data(filename="students.pkl.gz"):
    try:
        with gzip.open(filename, "rb") as f:
            data = pickle.load(f)
            print(f"[Success] Loaded data from {filename}")
            return data
    except FileNotFoundError:
        print(f"[Info] {filename} not found. Starting with empty data.")
        return None
    except Exception as e:
        print(f"[Error] Failed to load data: {e}")
        return None