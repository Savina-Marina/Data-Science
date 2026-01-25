#!/bin/sh
jq -f filter.jq ../ex00/hh.json | \
jq -r '(["id", "created_at", "name", "has_test", "alternate_url"] | @csv), (.[] | [.id, .created_at, .name, .has_test, .alternate_url] | @csv)' > hh.csv