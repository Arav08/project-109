import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("project_109.csv")

reading_list = df["reading score"]
math_list = df["math score"]
writing_list = df["writing score"]

# median, mean, mode, and stdev for reading score
reading_median = statistics.median(reading_list)
reading_mean = statistics.mean(reading_list)
reading_mode = statistics.mode(reading_list)
reading_stdev = statistics.stdev(reading_list)

# median, mean, mode, and stdev for math score
math_median = statistics.median(math_list)
math_mean = statistics.mean(math_list)
math_mode = statistics.mode(math_list)
math_stdev = statistics.stdev(math_list)

# median, mean, mode, and stdev for writing score
writing_median = statistics.median(writing_list)
writing_mean = statistics.mean(writing_list)
writing_mode = statistics.mode(writing_list)
writing_stdev = statistics.stdev(writing_list)

# show median, mean, mode for reading, math, and writing respectively
print("The median, mean, and mode of reading is: {}, {}, {}, respectively".format(reading_median, reading_mean, reading_mode))
print("The median, mean, and mode of math is: {}, {}, {}, respectively".format(math_median, math_mean, math_mode))
print("The median, mean, and mode of writing is: {}, {}, {}, respectively".format(writing_median, writing_mean, writing_mode))

# first, second, third stdev for reading
reading_first_stdev_start, reading_first_stdev_end = reading_mean - reading_stdev, reading_mean + reading_stdev
reading_second_stdev_start, reading_second_stdev_end = reading_mean - (2*reading_stdev), reading_mean + (2*reading_stdev)
reading_third_stdev_start, reading_third_stdev_end = reading_mean - (3*reading_stdev), reading_mean + (3*reading_stdev)

# first, second, third stdev for math
math_first_stdev_start, math_first_stdev_end = math_mean - math_stdev, math_mean + math_stdev
math_second_stdev_start, math_second_stdev_end = math_mean - (2*math_stdev), math_mean + (2*math_stdev)
math_third_stdev_start, math_third_stdev_end = math_mean - (3*math_stdev), math_mean + (3*math_stdev)

# first, second, third stdev for writing
writing_first_stdev_start, writing_first_stdev_end = writing_mean - writing_stdev, writing_mean + writing_stdev
writing_second_stdev_start, writing_second_stdev_end = writing_mean - (2*writing_stdev), writing_mean + (2*writing_stdev)
writing_third_stdev_start, writing_third_stdev_end = writing_mean - (3*writing_stdev), writing_mean + (3*writing_stdev)

# calculate % of data within first, second, third stdev for reading
reading_listifdata_within_firststdev = [result for result in reading_list if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_listifdata_within_secondstdev = [result for result in reading_list if result > reading_second_stdev_start and result < reading_second_stdev_end]
reading_listifdata_within_thirdstdev = [result for result in reading_list if result > reading_third_stdev_start and result < reading_third_stdev_end]

# calculate % of data within first, second, third stdev for math
math_listifdata_within_firststdev = [result for result in math_list if result > math_first_stdev_start and result < math_first_stdev_end]
math_listifdata_within_secondstdev = [result for result in math_list if result > math_second_stdev_start and result < math_second_stdev_end]
math_listifdata_within_thirdstdev = [result for result in math_list if result > math_third_stdev_start and result < math_third_stdev_end]

# calculate % of data within first, second, third stdev for writing
writing_listifdata_within_firststdev = [result for result in writing_list if result > writing_first_stdev_start and result < writing_first_stdev_end]
writing_listifdata_within_secondstdev = [result for result in writing_list if result > writing_second_stdev_start and result < writing_second_stdev_end]
writing_listifdata_within_thirdstdev = [result for result in writing_list if result > writing_third_stdev_start and result < writing_third_stdev_end]

# print the results for reading within the three stdev
print("{}% of data for reading scores lies within the first standard deviation".format(len(reading_listifdata_within_firststdev) * 100.0 / len(reading_list)))
print("{}% of data for reading scores lies within the second standard deviation".format(len(reading_listifdata_within_secondstdev) * 100.0 / len(reading_list)))
print("{}% of data for reading scores lies within the third standard deviation".format(len(reading_listifdata_within_thirdstdev) * 100.0 / len(reading_list)))

# print the results for math within the three stdev
print("{}% of data for math scores lies within the first standard deviation".format(len(math_listifdata_within_firststdev) * 100.0 / len(math_list)))
print("{}% of data for math scores lies within the second standard deviation".format(len(math_listifdata_within_secondstdev) * 100.0 / len(math_list)))
print("{}% of data for math scores lies within the third standard deviation".format(len(math_listifdata_within_thirdstdev) * 100.0 / len(math_list)))

# print the results for writing within the three stdev
print("{}% of data for writing scores lies within the first standard deviation".format(len(writing_listifdata_within_firststdev) * 100.0 / len(writing_list)))
print("{}% of data for writing scores lies within the second standard deviation".format(len(writing_listifdata_within_secondstdev) * 100.0 / len(writing_list)))
print("{}% of data for writing scores lies within the third standard deviation".format(len(writing_listifdata_within_thirdstdev) * 100.0 / len(writing_list)))

# show graph of reading scores
fig_reading = ff.create_distplot([reading_list], ["result"], show_hist = False)
fig_reading.show()

# show graph of math scores
fig_math = ff.create_distplot([math_list], ["result"], show_hist = False)
fig_math.show()

# show graph of writing scores
fig_writing = ff.create_distplot([writing_list], ["result"], show_hist = False)
fig_writing.show()