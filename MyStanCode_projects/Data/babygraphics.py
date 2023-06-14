"""
File: babygraphics.py
Name: Emilie Chen
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width = CANVAS_WIDTH
    x_coordinate = ((width-GRAPH_MARGIN_SIZE*2)/len(YEARS))*year_index+GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    x_line = (CANVAS_WIDTH-GRAPH_MARGIN_SIZE*2)/(len(YEARS))
    y_line = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000
    y_none = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

    # i: list of different names
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        print("names success")
        rank = 0
        the_next_rank = 0
        the_next_year = 0

        # ranking in different years
        for j in range(len(YEARS)):
            year = YEARS[j]
            if j+1 < len(YEARS):
                the_next_year = YEARS[j + 1]
                the_last_rank = False
            else:
                the_last_rank = True
            print(str(year)+"&"+str(the_next_year))

            # check the x y position
            if str(year) in name_data[name]:
                no_rank = False
                rank = int(name_data[name][str(year)])
                print(name + ' ' + str(rank))
            else:
                no_rank = True
                print('*')

            if str(the_next_year) in name_data[name]:
                no_next_rank = False
                the_next_rank = int(name_data[name][str(the_next_year)])
                print('the_next_rank' + str(the_next_rank))
            else:
                no_next_rank = True
                print('no_next_rank')

            # draw text and line
            if no_rank and no_next_rank and not the_last_rank:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_line, y_none,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_line, y_none, fill=COLORS[i % 4],
                                   width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_line, y_none,
                                   text=name + ' *', fill=COLORS[i % 4], anchor=tkinter.SW)
                print("no+no")

            elif no_rank and not no_next_rank and not the_last_rank:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_line, y_none,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_line, GRAPH_MARGIN_SIZE + the_next_rank * y_line,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_line, y_none,
                                   text=name + ' *', fill=COLORS[i % 4], anchor=tkinter.SW)
                print("no yes")

            elif not no_rank and no_next_rank and not the_last_rank:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_line, GRAPH_MARGIN_SIZE + rank * y_line,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_line, y_none, fill=COLORS[i % 4],
                                   width=LINE_WIDTH)
                name_and_rank = str(name) + " " + str(rank)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_line, GRAPH_MARGIN_SIZE + rank * y_line,
                                   text=name_and_rank, fill=COLORS[i % 4], anchor=tkinter.SW)
                print("yes no")

            elif not no_rank and not no_next_rank and not the_last_rank:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_line, GRAPH_MARGIN_SIZE + rank * y_line,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_line, GRAPH_MARGIN_SIZE + the_next_rank * y_line,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                name_and_rank = str(name) + " "+str(rank)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_line, GRAPH_MARGIN_SIZE + rank * y_line,
                                   text=name_and_rank, fill=COLORS[i % 4], anchor=tkinter.SW)
                print("yes yes")

            if no_next_rank and the_last_rank:
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_line, y_none,
                                   text=name + ' *', fill=COLORS[i % 4], anchor=tkinter.SW)
            elif not no_next_rank and the_last_rank:
                name_and_rank = str(name) + " " + str(the_next_rank)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_line, GRAPH_MARGIN_SIZE + the_next_rank * y_line,
                                   text=name_and_rank, fill=COLORS[i % 4], anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
