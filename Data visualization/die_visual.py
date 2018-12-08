from die import Die
import pygal


die1 = Die()
die2 = Die()
results = []
for roll_num in range(1000):
    results.append(die1.roll() + die2.roll())

frequencies = []
max_result = die1.num_sizes + die2.num_sizes
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
