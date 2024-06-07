import pandas as pd
import os

def group_attachments():
  try:
    if not os.listdir("export"):
      print("Export directory is empty. Nothing to do.")
      return

    if not os.path.isfile("attachments.csv"):
      print("CSV file does not exist.")
      return

    csv_data = pd.read_csv("attachments.csv", sep=";")
    data = csv_data.to_dict(orient="records")

    directories_list = set(v["nowe_id_pac_mm"] for v in data)

    if not os.path.isdir("import"):
      os.mkdir("import")

    for directory in directories_list:
      if not os.path.isdir(f"import/{directory}"):
        os.mkdir(f"import/{directory}")

    for row in data:
      src = f'export/{row["nowa_nazwa_export"]}'
      dst = f'import/{row["nowe_id_pac_mm"]}/{row["nowa_nazwa"]}'
      os.replace(src, dst)
      print(f"Moved {src} to {dst}")

  except FileNotFoundError:
    print("Export directory does not exist.")
    return

  except Exception as e:
    print(f"An error occurred: {e}")
    return

group_attachments()