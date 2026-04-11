import pstats

stats = pstats.Stats("profile.stats")
stats.sort_stats("cumulative")
stats.print_stats(5)