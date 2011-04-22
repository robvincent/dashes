#!/bin/bash
echo "{"
echo "  \"title\" : \"`hostname` - $1\""
echo "  \"updated\" : \"`date "+%Y-%m-%d %H:%M:%S"`\""
echo "  \"headers\": [\"Directory\", \"Size (MB)\"]"
echo "  \"data\": ["
du -sm $1/* | sort -nr | awk '{print "    [ \"" $2 "\", \"" $1 "\" ],"}'
echo "  ]"
echo "}"
