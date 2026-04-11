#!/usr/bin/env python3

import sys
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def submit_yahoo_consent(session, response, headers):
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find("form")

    if form is None:
        raise Exception("Yahoo consent page returned: no form found")

    action = form.get("action") or response.url
    post_url = urljoin(response.url, action)

    data = {}

    for inp in form.find_all("input"):
        name = inp.get("name")
        if not name:
            continue

        inp_type = (inp.get("type") or "text").lower()
        value = inp.get("value") or ""

        if inp_type in ("checkbox", "radio"):
            if "agree" in name.lower() or "accept" in name.lower() or inp.has_attr("checked"):
                data[name] = value if value != "" else "1"
        else:
            data[name] = value

    lowered_names = {k.lower() for k in data.keys()}
    if not any("agree" in k or "accept" in k for k in lowered_names):
        data["agree"] = "1"

    consent_headers = headers.copy()
    consent_headers["Referer"] = response.url

    session.post(post_url, headers=consent_headers, data=data, allow_redirects=True)


def get_financial_page(session, url, headers):
    response = session.get(url, headers=headers, allow_redirects=True)

    if response.status_code != 200:
        raise Exception("URL does not exist")

    if "consent.yahoo.com" in response.url:
        submit_yahoo_consent(session, response, headers)
        response = session.get(url, headers=headers, allow_redirects=True)

    if response.status_code != 200:
        raise Exception("URL does not exist")

    if "consent.yahoo.com" in response.url:
        raise Exception("Yahoo consent page returned")

    return response


def extract_field(lines, field):
    for i, line in enumerate(lines):
        if line.lower() == field.lower():
            values = []

            for x in lines[i + 1:]:
                t = x.replace(",", "").replace("-", "").replace(".", "")
                if t.isdigit():
                    values.append(x)
                if len(values) == 5:
                    break

            if len(values) < 5:
                raise Exception("Field not found")

            return tuple([line] + values)

    raise Exception("Field not found")


def main():
    if len(sys.argv) != 3:
        raise Exception("Usage: ./financial.py TICKER FIELD")

    ticker = sys.argv[1].upper()
    field = sys.argv[2]

    url = f"https://finance.yahoo.com/quote/{ticker}/financials"

    time.sleep(5)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    session = requests.Session()
    response = get_financial_page(session, url, headers)

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text("\n")
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    result = extract_field(lines, field)
    print(result)


if __name__ == "__main__":
    main()