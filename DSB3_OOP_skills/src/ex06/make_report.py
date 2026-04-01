import os
import analytics
import config

base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir, config.DATA_FILE)

research = analytics.Research(filepath)

try:
    data = research.file_reader(has_header=config.HAS_HEADER)

    analysis = research.Analytics(data)

    heads, tails = analysis.counts()
    p_heads, p_tails = analysis.fractions(heads, tails)

    report = config.REPORT_TEMPLATE.format(
        total=heads + tails,
        heads=heads,
        tails=tails,
        heads_percent=f"{p_heads * 100:.2f}".replace(".", ","),
        tails_percent=f"{p_tails * 100:.2f}".replace(".", ","),
        steps=config.NUM_OF_STEPS,
        forecast=analysis.predict_random(config.NUM_OF_STEPS),
    )

    analysis.save_file(report, config.REPORT_FILENAME, config.REPORT_EXT)
    print(report)

    research.send_telegram("Отчет успешно создан")

except Exception:
    research.send_telegram("Отчёт не создан из-за ошибки.")
    raise