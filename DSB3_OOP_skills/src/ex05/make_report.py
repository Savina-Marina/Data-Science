import os
import analytics
import config

filepath = os.path.join(os.path.dirname(__file__), config.DATA_FILE)

research = analytics.Research(filepath)
data = research.file_reader(config.HAS_HEADER)

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
    forecast=analysis.predict_random(config.NUM_OF_STEPS)
)

analysis.save_file(report, config.REPORT_FILENAME, config.REPORT_EXT)
print(report)