import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

filename = 'hn_submissions_save.json'
submission_dicts = []
with open(filename) as f_obj:
    submission_dicts = json.load(f_obj)
# print(submission_dicts)
plot_dicts, titles = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    plot_dict = {
        'value': submission_dict['comments'],
        'xlink': submission_dict['link']
    }
    plot_dicts.append(plot_dict)
# print(plot_dicts)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'The most popular article on New Hacker'.title()
chart.x_labels = titles

chart.add('', plot_dicts)
print(chart)
chart.render_to_file('hn_submissions.svg')
