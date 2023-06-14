"""
File: my_drawing.py
Name: Emilie Chen
----------------------
Title: My Boba Tea

下午快睡著需要來杯飲料ＸＤ
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    bg>>drink>>bobble>>straw>>text
    """
    window = GWindow(width=500, height=500, title='my_drawing')

    bg1 = GRect(500, 200, x=0, y=300)
    bg1.filled = True
    bg1.fill_color = 'peru'
    bg1.color = 'khaki'
    window.add(bg1)

    bg2 = GRect(500, 300, x=0, y=0)
    bg2.filled = True
    bg2.fill_color = 'azure'
    bg2.color = 'azure'
    window.add(bg2)

    c1 = GOval(120, 60, x=50, y=50)
    c1.filled = True
    c1.fill_color = 'white'
    c1.color = 'white'
    window.add(c1)

    c2 = GOval(125, 80, x=70, y=50)
    c2.filled = True
    c2.fill_color = 'white'
    c2.color = 'white'
    window.add(c2)

    c3 = GOval(120, 60, x=90, y=50)
    c3.filled = True
    c3.fill_color = 'white'
    c3.color = 'white'
    window.add(c3)

    c4 = GOval(125, 80, x=365, y=80)
    c4.filled = True
    c4.fill_color = 'white'
    c4.color = 'white'
    window.add(c4)

    body1 = GPolygon()
    body1.add_vertex((150, 150))
    body1.add_vertex((200, 150))
    body1.add_vertex((200, 400))
    body1.filled = True
    body1.fill_color = 'beige'
    body1.color = 'beige'
    window.add(body1)

    body2 = GRect(100, 250, x=200, y=150)
    body2.filled = True
    body2.fill_color = 'beige'
    body2.color = 'beige'
    window.add(body2)

    body3 = GPolygon()
    body3.add_vertex((300, 150))
    body3.add_vertex((350, 150))
    body3.add_vertex((300, 400))
    body3.filled = True
    body3.fill_color = 'beige'
    body3.color = 'beige'
    window.add(body3)

    lid = GOval(200, 100, x=150, y=100)
    lid.filled = True
    lid.fill_color = 'ivory'
    lid.color = 'beige'
    window.add(lid)

    hole = GOval(30, 15, x=235, y=142)
    hole.filled = True
    hole.fill_color = 'beige'
    hole.color = 'beige'
    window.add(hole)

    o1 = GOval(20, 20, x=200, y=376)
    o1.filled = True
    o1.fill_color = 'burlywood'
    o1.color = 'burlywood'
    window.add(o1)

    o2 = GOval(20, 20, x=222, y=378)
    o2.filled = True
    o2.fill_color = 'burlywood'
    o2.color = 'burlywood'
    window.add(o2)

    o3 = GOval(20, 20, x=254, y=376)
    o3.filled = True
    o3.fill_color = 'burlywood'
    o3.color = 'burlywood'
    window.add(o3)

    or1 = GOval(20, 20, x=240, y=374)
    or1.filled = True
    or1.fill_color = 'brown'
    or1.color = 'brown'
    window.add(or1)

    o4 = GOval(20, 20, x=280, y=378)
    o4.filled = True
    o4.fill_color = 'burlywood'
    o4.color = 'burlywood'
    window.add(o4)

    ob1 = GOval(20, 20, x=270, y=377)
    ob1.filled = True
    ob1.fill_color = 'black'
    ob1.color = 'black'
    window.add(ob1)

    or2 = GOval(20, 20, x=200, y=365)
    or2.filled = True
    or2.fill_color = 'brown'
    or2.color = 'brown'
    window.add(or2)

    or3 = GOval(20, 20, x=245, y=350)
    or3.filled = True
    or3.fill_color = 'brown'
    or3.color = 'brown'
    window.add(or3)

    or4 = GOval(20, 20, x=273, y=365)
    or4.filled = True
    or4.fill_color = 'brown'
    or4.color = 'brown'
    window.add(or4)

    ob2 = GOval(20, 20, x=215, y=358)
    ob2.filled = True
    ob2.fill_color = 'black'
    ob2.color = 'black'
    window.add(ob2)

    o5 = GOval(20, 20, x=195, y=350)
    o5.filled = True
    o5.fill_color = 'burlywood'
    o5.color = 'burlywood'
    window.add(o5)

    o6 = GOval(20, 20, x=228, y=356)
    o6.filled = True
    o6.fill_color = 'burlywood'
    o6.color = 'burlywood'
    window.add(o6)

    o7 = GOval(20, 20, x=255, y=352)
    o7.filled = True
    o7.fill_color = 'burlywood'
    o7.color = 'burlywood'
    window.add(o7)

    o8 = GOval(20, 20, x=285, y=351)
    o8.filled = True
    o8.fill_color = 'burlywood'
    o8.color = 'burlywood'
    window.add(o8)

    straw1 = GPolygon()
    straw1.add_vertex((50, 320))
    straw1.add_vertex((60, 305))
    straw1.add_vertex((200, 488))
    straw1.filled = True
    straw1.fill_color = 'grey'
    straw1.color = 'grey'
    window.add(straw1)

    straw2 = GPolygon()
    straw2.add_vertex((60, 305))
    straw2.add_vertex((210, 475))
    straw2.add_vertex((200, 488))
    straw2.filled = True
    straw2.fill_color = 'grey'
    straw2.color = 'grey'
    window.add(straw2)

    label = GLabel('Welcome! : )')
    label.color = "white"
    label.font = 'Times-38-bold'
    window.add(label, 280, 480)

if __name__ == '__main__':
    main()
