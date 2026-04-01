import os
import json
import logging
import requests
from random import randint
import config


logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)

logger = logging.getLogger(__name__)


class Research:
    def __init__(self, path):
        self.path = path
        logger.info("Research object created with path=%s", self.path)

    def file_reader(self, has_header=True):
        logger.info("Reading file: %s (has_header=%s)", self.path, has_header)

        if not os.path.exists(self.path):
            logger.info("File does not exist: %s", self.path)
            raise Exception("File does not exist")

        with open(self.path, "r") as file:
            lines = file.readlines()

        if len(lines) < 1:
            logger.info("Incorrect file structure: empty file")
            raise Exception("Incorrect file structure")

        data_lines = lines[1:] if has_header else lines

        result = []
        for line in data_lines:
            line = line.strip()

            if not line:
                logger.info("Invalid data string: empty line")
                raise Exception("Invalid data string")

            if line not in ("0,1", "1,0"):
                logger.info("Invalid data string: %s", line)
                raise Exception("Invalid data string")

            parts = line.split(",")
            result.append([int(parts[0]), int(parts[1])])

        logger.info("File parsed successfully, rows=%d", len(result))
        return result

    def send_telegram(self, message):

        logger.info("Sending Telegram message")
        token = config.TELEGRAM_BOT_TOKEN
        chat_id = config.TELEGRAM_CHAT_ID

        if not token or not chat_id:
            logger.info("Telegram is not configured (token/chat_id empty). Message skipped.")
            return False

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}

        try:
            r = requests.post(url, json=payload, timeout=10)
            logger.info("Telegram response status=%s", r.status_code)
            return r.status_code == 200
        except Exception as e:
            logger.info("Telegram send failed: %s", str(e))
            return False

    class Calculations:
        def __init__(self, data):
            self.data = data
            logger.info("Calculations object created, rows=%d", len(self.data))

        def counts(self):
            logger.info("Calculating the counts of heads and tails")

            heads = 0
            tails = 0

            for row in self.data:
                if row == [1, 0]:
                    heads += 1
                elif row == [0, 1]:
                    tails += 1

            logger.info("Counts calculated: heads=%d tails=%d", heads, tails)
            return heads, tails

        def fractions(self, heads, tails):
            logger.info("Calculating fractions")

            total = heads + tails
            if total == 0:
                logger.info("No data for fractions")
                raise Exception("No data")

            head_frac = int(heads / total * 10000) / 10000
            tail_frac = int(tails / total * 10000) / 10000

            logger.info("Fractions calculated: head_frac=%s tail_frac=%s", head_frac, tail_frac)
            return head_frac, tail_frac

    class Analytics(Calculations):
        def predict_random(self, number_predictions):
            logger.info("Predicting random values, steps=%d", number_predictions)

            if number_predictions < 1:
                logger.info("Incorrect number of predictions: %d", number_predictions)
                raise Exception("Incorrect number of predictions")

            result = []
            for _ in range(number_predictions):
                coin = randint(0, 1)
                if coin == 1:
                    result.append([1, 0])
                else:
                    result.append([0, 1])

            logger.info("Random prediction generated: %s", str(result))
            return result

        def predict_last(self):
            logger.info("Predicting last value")

            if len(self.data) == 0:
                logger.info("No data for predict_last")
                raise Exception("No data")

            last = self.data[-1]
            logger.info("Last value: %s", str(last))
            return last

        def save_file(self, data, file_name, ext):
            logger.info("Saving result to file: name=%s ext=%s", file_name, ext)

            if not file_name:
                logger.info("Incorrect file name")
                raise Exception("Incorrect file name")

            if not ext:
                logger.info("Incorrect file extension")
                raise Exception("Incorrect file extension")

            safe_ext = ext.lstrip(".")
            full_name = f"{file_name}.{safe_ext}"

            with open(full_name, "w") as f:
                f.write(str(data))

            logger.info("File saved: %s", full_name)
            return full_name