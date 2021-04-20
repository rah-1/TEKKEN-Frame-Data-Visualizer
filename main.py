from tkinter import *
from tkinter import ttk
from character import Character
from move import Move
import csv

heap_mode = True
insert_mode = False
sicko_mode = False

my_char = []
my_curr_char = ""
opp_curr_char = ""
my_curr_moves = []
opp_curr_moves = []
char_dict = {}


# read in files
def file_reader(character, filename):
    arr = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0 and row[2] != "":
                notation = row[0]
                level = row[1]
                damage = row[2]
                startup = row[3]
                b = row[4]
                if len(b) > 0 and b[0] == "=":
                    b = b[1:len(b)-1]
                if len(b) > 0 and '0' < b[0] <= '9':
                    b = "+" + b
                h = row[5]
                if len(h) > 0 and h[0] == "=":
                    h = h[1:len(h)-1]
                if len(h) > 0 and '0' < h[0] <= '9':
                    h = "+" + h
                ch = row[6]
                if len(ch) > 0 and ch[0] == "=":
                    ch = ch[1:len(ch)-1]
                if len(ch) > 0 and '0' < ch[0] <= '9':
                    ch = "+" + ch
                tracking = ""
                if row[7] == "l":
                    tracking = "left side"
                elif row[7] == "r":
                    tracking = "right side"
                elif row[7] == "b":
                    tracking = "both sides"
                notes = row[8]

                move = Move(notation, level, damage, startup, b, h, ch, tracking, notes)
                character.add_move(move)

            line_count += 1


armor_king = Character("Armor King")
my_char.append(armor_king.name)
char_dict[armor_king.name] = armor_king
file_reader(armor_king, "armor_king.csv")

bryan = Character("Bryan")
my_char.append(bryan.name)
char_dict[bryan.name] = bryan
file_reader(bryan, "bryan.csv")

hwoarang = Character("Hwoarang")
my_char.append(hwoarang.name)
char_dict[hwoarang.name] = hwoarang
file_reader(hwoarang, "hwoarang.csv")

jin = Character("Jin")
my_char.append(jin.name)
char_dict[jin.name] = jin
file_reader(jin, "jin.csv")

julia = Character("Julia")
my_char.append(julia.name)
char_dict[julia.name] = julia
file_reader(julia, "julia.csv")

kazumi = Character("Kazumi")
my_char.append(kazumi.name)
char_dict[kazumi.name] = kazumi
file_reader(kazumi, "kazumi.csv")

kazuya = Character("Kazuya")
my_char.append(kazuya.name)
char_dict[kazuya.name] = kazuya
file_reader(kazuya, "kazuya.csv")

lars = Character("Lars")
my_char.append(lars.name)
char_dict[lars.name] = lars
file_reader(lars, "lars.csv")

law = Character("Law")
my_char.append(law.name)
char_dict[law.name] = law
file_reader(law, "law.csv")

paul = Character("Paul")
my_char.append(paul.name)
char_dict[paul.name] = paul
file_reader(paul, "paul.csv")

steve = Character("Steve")
my_char.append(steve.name)
char_dict[steve.name] = steve
file_reader(steve, "steve.csv")


root = Tk()
root.geometry("450x550")
root.title("TEKKEN Frame Data Visualizer")
if heap_mode:
    root.title("TEKKEN Frame Data Visualizer (Heap Sort Mode)")
elif insert_mode:
    root.title("TEKKEN Frame Data Visualizer (Insertion Sort Mode)")
elif sicko_mode:
    root.title("TEKKEN Frame Data Visualizer (SICKO MODE!)")

# frame advantage: default = 0
frame_adv = 0


def reset():
    global frame_adv
    frame_adv = 0
    frame_slider.set(0)
    my_dropdown.set("")
    opp_dropdown.set("")
    infobox.config(text="")
    my_moves.selection_clear(ANCHOR)
    my_moves.delete(0, 'end')
    opp_moves.selection_clear(ANCHOR)
    opp_moves.delete(0, 'end')
    my_movelist.config(text="")
    opp_movelist.config(text="")


def move_select(bro):  # print info
    if my_moves.curselection():
        for move in char_dict[my_curr_char].moveset:
            if move.notation == my_moves.get(ANCHOR):
                infobox.config(text="Move Information:\nNotation: "+move.notation+"\nHit Level: "+move.level
                               + "\nDamage: "+move.damage+"\nStartup Frame: i"+move.startup+"\nOn Block: "
                               + move.b+"\nOn Hit: "+move.h+"\nOn Counter Hit: "+move.ch+"\nTracking: "
                               + move.tracking+"\nNotes: "+move.notes)
    elif opp_moves.curselection():
        for move in char_dict[opp_curr_char].moveset:
            if move.notation == opp_moves.get(ANCHOR):
                infobox.config(text="Move Information:\nNotation: "+move.notation+"\nHit Level: "+move.level
                               + "\nDamage: "+move.damage+"\nStartup Frame: i"+move.startup+"\nOn Block: "
                               + move.b+"\nOn Hit: "+move.h+"\nOn Counter Hit: "+move.ch+"\nTracking: "
                               + move.tracking+"\nNotes: "+move.notes)
    global frame_adv
    frame_adv = frame_slider.get()


def char_select(event):
    global my_curr_moves
    global my_curr_char
    my_curr_moves = set_moves(my_dropdown.get())
    my_curr_char = my_dropdown.get()
    my_movelist.config(text=my_dropdown.get()+"'s moveset")
    my_moves.selection_clear(ANCHOR)
    my_moves.delete(0, 'end')
    for i in my_curr_moves:
        my_moves.insert(END, i)


def opp_select(event):
    global opp_curr_moves
    global opp_curr_char
    opp_curr_moves = set_moves(opp_dropdown.get())
    opp_curr_char = opp_dropdown.get()
    opp_movelist.config(text=opp_dropdown.get() + "'s moveset")
    opp_moves.selection_clear(ANCHOR)
    opp_moves.delete(0, 'end')
    for i in opp_curr_moves:
        opp_moves.insert(END, i)


def set_moves(name):
    arr = []
    t = []
    if name in char_dict:
        t = char_dict[name].moveset
    for i in t:
        arr.append(i.notation)
    return arr


def loser():
    global frame_adv
    frame_adv = frame_slider.get()
    if my_curr_char in char_dict and opp_curr_char in char_dict and my_moves.curselection():
        if insert_mode:
            insertion_sort("loser")
        if heap_mode:
            heap_sort("loser")
        if sicko_mode:
            print("SICKO MODE")


def trader():
    global frame_adv
    frame_adv = frame_slider.get()
    if my_curr_char in char_dict and opp_curr_char in char_dict and my_moves.curselection():
        if insert_mode:
            insertion_sort("trader")
        if heap_mode:
            heap_sort("trader")
        if sicko_mode:
            print("SICKO MODE")


def winner():
    global frame_adv
    frame_adv = frame_slider.get()
    if my_curr_char in char_dict and opp_curr_char in char_dict and my_moves.curselection():
        if insert_mode:
            insertion_sort("winner")
        if heap_mode:
            heap_sort("winner")
        if sicko_mode:
            print("SICKO MODE")


def heap_sort(tipo):
    threshold = 0
    global opp_curr_moves
    opp_curr_moves.clear()
    opp_moves.selection_clear(ANCHOR)
    opp_moves.delete(0, 'end')
    new_moves = []
    for move in char_dict[my_curr_char].moveset:
        if move.notation == my_moves.get(ANCHOR):
            threshold = int(move.startup) - frame_adv
            break

    for move in char_dict[opp_curr_char].moveset:
        if int(move.startup) < threshold and tipo == "loser":
            new_moves.append(move)
        elif int(move.startup) == threshold and tipo == "trader":
            new_moves.append(move)
        elif int(move.startup) > threshold and tipo == "winner":
            new_moves.append(move)

    # the actual sorting
    min_heap = []
    for move in new_moves:
        min_heap = heap_insert(min_heap, int(len(min_heap)), move)

    new_moves.clear()
    while len(min_heap) > 0:
        new_moves.append(min_heap[0])
        min_heap = heap_remove(min_heap, len(min_heap)-1)

    for move in new_moves:
        opp_curr_moves.append(move.notation)
        opp_moves.insert(END, move.notation)


def heap_insert(heap, size, key):
    heap.append(key)
    while size > 0 and heap[size].startup < heap[int((size-1)/2)].startup:
        heap[size], heap[int((size-1)/2)] = heap[int((size-1)/2)], heap[size]
        size = int((size-1)/2)
    return heap


def heap_remove(heap, size):
    heap[0] = heap[size]
    del(heap[size])
    index = 0
    while index < size:
        left = 2*index+1
        right = 2*index+2
        if left < size < right and int(heap[left].startup) < int(heap[index].startup):
            heap[index], heap[left] = heap[left], heap[index]
            index = left
        elif right < size < left and int(heap[right].startup) < int(heap[index].startup):
            heap[index], heap[right] = heap[right], heap[index]
            index = right
        elif left < size and right < size:
            if int(heap[left].startup) < int(heap[index].startup) and int(heap[left].startup) <= int(heap[right].startup):
                heap[index], heap[left] = heap[left], heap[index]
                index = left
            elif int(heap[right].startup) < int(heap[index].startup) and int(heap[left].startup) > int(heap[right].startup):
                heap[index], heap[right] = heap[right], heap[index]
                index = right
            else:
                break
        else:
            break
    return heap


def insertion_sort(tipo):
    threshold = 0
    global opp_curr_moves
    opp_curr_moves.clear()
    opp_moves.selection_clear(ANCHOR)
    opp_moves.delete(0, 'end')
    new_moves = []
    for move in char_dict[my_curr_char].moveset:
        if move.notation == my_moves.get(ANCHOR):
            threshold = int(move.startup) - frame_adv
            break

    for move in char_dict[opp_curr_char].moveset:
        if int(move.startup) < threshold and tipo == "loser":
            new_moves.append(move)
        elif int(move.startup) == threshold and tipo == "trader":
            new_moves.append(move)
        elif int(move.startup) > threshold and tipo == "winner":
            new_moves.append(move)

    # the actual sorting
    index = 1
    while index < len(new_moves):
        i = index
        while i > 0:
            if int(new_moves[i].startup) < int(new_moves[i - 1].startup):
                new_moves[i], new_moves[i - 1] = new_moves[i - 1], new_moves[i]
            i -= 1
        index += 1

    for move in new_moves:
        opp_curr_moves.append(move.notation)
        opp_moves.insert(END, move.notation)


# buttons
reset = Button(root, text="RESET", command=reset).pack(side=BOTTOM, anchor='se')
lose = Button(root, text="Loses to", command=loser).pack(side=BOTTOM, anchor='s')
trade = Button(root, text="Trades with", command=trader).pack(side=BOTTOM, anchor='s')
win = Button(root, text="Wins against", command=winner).pack(side=BOTTOM, anchor='s')

# move properties/information
infobox = Label(root, text="", anchor='w', justify=LEFT, padx=30)
infobox.pack(side=BOTTOM, fill="both")
frame_label = Label(root, text="Frame Advantage:").pack()

# slider for frame advantage
frame_slider = Scale(root, from_=-20, to_=+20, orient=HORIZONTAL, resolution=1,)
frame_slider.pack()

# labels for character/opponent names
name_frame = Frame(root)
name_frame.pack()
char_label = Label(name_frame, text=" Character\t\t\t            Opponent").pack(padx=15, side=TOP)

# frame and scrollbar for movelists
my_frame = Frame(root)
my_movelist = Label(my_frame, text="")
my_movelist.pack()
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

my_moves = Listbox(my_frame, width=25, yscrollcommand=my_scrollbar.set)
my_moves.bind('<<ListboxSelect>>', move_select)  # function that executes when move selected

my_scrollbar.config(command=my_moves.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack(side=LEFT, padx=30)

my_moves.pack()

# same but for opponent
opp_frame = Frame(root)
opp_movelist = Label(opp_frame, text="")
opp_movelist.pack()
opp_scrollbar = Scrollbar(opp_frame, orient=VERTICAL)

opp_moves = Listbox(opp_frame, width=25, yscrollcommand=opp_scrollbar.set)
opp_moves.bind('<<ListboxSelect>>', move_select)  # function that executes when move selected

opp_scrollbar.config(command=opp_moves.yview)
opp_scrollbar.pack(side=RIGHT, fill=Y)
opp_frame.pack(side=RIGHT, padx=20)

opp_moves.pack()


my_dropdown = ttk.Combobox(name_frame, value=my_char, width=11)
my_dropdown.bind("<<ComboboxSelected>>", char_select)
my_dropdown.pack(side=LEFT, padx=70)

opp_dropdown = ttk.Combobox(name_frame, value=my_char, width=11)
opp_dropdown.bind("<<ComboboxSelected>>", opp_select)
opp_dropdown.pack(side=BOTTOM, padx=70)

root.mainloop()
