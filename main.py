import statistics
text = "4.0 49.0 13.0 33.0 24.0 24.0 35.0 104.0 34.0 40.0 38.0 1.0"
new_text = text.replace(" ", ",")
print(new_text)


nums = [4.0,49.0,13.0,33.0,24.0,24.0,35.0,104.0,34.0,40.0,38.0,1.0]
print(f"Amount of values: {len(nums)}")
print(f"Sorted values: {sorted(nums)}")
print(f"Median: {statistics.median(nums)}")
print(f"Mean: {statistics.mean(nums)}")


