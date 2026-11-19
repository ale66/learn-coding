'''
Example in-class project file

Complete the cells


'''

# Setup phase: change as needed

MYWORKDIR = "C:\\Users\\ale\\Downloads\\_git\\learn-coding\\76-matplotlib"

#%%
import os
os.chdir(MYWORKDIR)

#%%
import urllib.request

myopener = urllib.request.build_opener()

myopener.addheaders = [
    ("User-Agent", "Mozilla/5.0"),
    ("Referer", "https://data.spectator.co.uk/"),
]

urllib.request.install_opener(myopener)

#%%
import wget

# data of the "small boat crossings" chart on data.spectator.co.uk/migration
# these are not all-caps constants: we plan to do this for more than one file

url = "https://datawrapper.dwcdn.net/58WcU/22/dataset.csv"

new_data_file = "data/small-boats.csv"
new_figure = "data/small-boats-replica.png"

os.makedirs("data", exist_ok=True)

if os.path.exists(new_data_file):
    os.remove(new_data_file)

fname = wget.download(url, out=new_data_file)

print(f"Data file from {url} saved as {new_data_file}")

# Open the file, import data

#%%
import csv

# Check out the first 5 rows
R = 5

with open(new_data_file) as f:
    reader = csv.reader(f, delimiter="\t")

    for _ in range(R):
        print(next(reader))

# Data ingestion: read data and put it into your lists

#%%
labels = []
albanians = []
others = []

with open(new_data_file) as f:
    reader = csv.reader(f, delimiter="\t")

    # chuck the first row
    next(reader)
    
    for row in reader:
        labels.append(row[0])
        albanians.append(int(row[1]))
        others.append(int(row[2]))

# preview the data: the first R values
print('This is the data from file ', new_data_file)
print(labels[:R])
print(albanians[:R])
print(others[:R])


# Visualisation: reproduce the original data display


#%%
import matplotlib.pyplot as plt

# our main command: create a 8x5 inches black canvas
fig, ax = plt.subplots(figsize=(8, 5), facecolor="black")

# set the area between the axes
ax.set_facecolor("black")

#%%
# select labels for the horizontal axis (the 'x')
# to reproduce the plot, we will keep one label in 8, i.e., every two years
x = range(len(labels))

tick_pos = []
tick_names = []

for i in x:
    if i % 4 == 0:  # one label every two years
        tick_pos.append(i)
        tick_names.append(labels[i])

# check the work done
print("We'll use these tick positions and labels: ")
print(tick_pos)
print(tick_names)

#%%
# ok, prepare the x-axis visualisation
ax.set_xticks(tick_pos)
ax.set_xticklabels(tick_names)


#%%
# prepare the y-axis visualisation

# draw horizontal lines for values 0, 5000 etc.
ax.set_yticks([0, 5000, 10000, 15000, 20000])

# keep as it is: it prints values near the horizontal lines as 5,000, 10,000 (instead of 5000, 10000...)
ax.yaxis.set_major_formatter("{x:,.0f}")

# ok, draw a grid with horizontal white lines
ax.yaxis.grid(True, color="white")

# makes the lines pass below the actual values
ax.set_axisbelow(True)

# print the ticks in gray instead of the default black. Don't show the tick on the axis
ax.tick_params(colors="lightgray", length=0)

# show only the bottom of the grid, in white
for side in ["top", "right", "left"]:
    ax.spines[side].set_visible(False)

ax.spines["bottom"].set_color("white")

# write a description on top left corner of the data display
# the writing begins in position (0.03, 0.97)
fig.text(0.03, 0.97, "Irregular migrants", color="white", fontsize=22,
         fontfamily="serif", fontweight="bold", va="top")

fig.text(0.03, 0.88, "Numbers of irregular migrants detected each quarter",
         color="lightgray", fontsize=13, fontfamily="serif", va="top")

ax.legend(loc="lower left", bbox_to_anchor=(-0.05, 1.0), ncol=2, frameon=False,
          labelcolor="white", fontsize=11, handlelength=1, handleheight=1)


#%%
# draw the data for Albanians
# change ax.bar for a different visualisation style
ax.bar(x, albanians, width=0.65, color="tomato", label="Albanians")

# uncomment to also draw the data about all others
ax.bar(x, others, width=0.65, color="deepskyblue", label="Others", bottom=albanians)


#%%
# ok, we can put the data display out

# set the padding around the data display as a percentage
# empty space at the top if for title/caption
plt.subplots_adjust(top=0.75, left=0.1, right=0.9, bottom=0.1)

plt.savefig(new_figure)
plt.show()