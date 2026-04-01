import os

DATA_FILE = "../../datasets/ex05/data.csv"
HAS_HEADER = True
NUM_OF_STEPS = 3
REPORT_FILENAME = "report"
REPORT_EXT = "txt"
REPORT_TEMPLATE = (
    "Мы сделали {total} наблюдений, подбрасывая монету: {tails} — решка, {heads} — орёл. "
    "Вероятности составляют соответственно {tails_percent}% и {heads_percent}%. "
    "Наш прогноз — следующие {steps} наблюдения: {forecast}."
)