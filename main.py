from json import loads
import pandas as pd
import math


config = {}
df = None
chunks = []


with open("config.json") as config_file:
    config = loads(config_file.read())

df = pd.read_excel(
    io=config["filename"],
    sheet_name=0,
    header=None
)

number_of_chunks = math.ceil(len(df) / config["chunk_size"])

for i in range(number_of_chunks):
    chunks.append(df[i*config["chunk_size"]:(i+1)*config["chunk_size"]])

for i, chunk in enumerate(chunks):
    chunk.to_excel(
        excel_writer=config["output_template"].format(i),
        sheet_name="Лист1",
        header=False,
        index=False
    )

