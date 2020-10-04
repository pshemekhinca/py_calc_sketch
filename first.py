#! /home/peha/Desktop/tempProjects/01/venv/bin/python
tile_size = int(input("Podaj szerokość płytki [mm]: "))
room_length = int(input("Podaj szrokość pokoju [mm]: "))
grout = f"  {input('Podaj szerokość fugi [mm]: ')}  "  # grout input with spaces

grout_sum = int(grout) * int(room_length / tile_size + 1)
room_length = room_length - grout_sum  # new room length minus grouts sum
two_cuts = str((room_length % tile_size) / 2)
one_cut = str(room_length % tile_size)
whole = str(tile_size).split() * int(room_length / tile_size)
result_whole = grout.join([*whole, one_cut])
result_centr = grout.join([two_cuts, *whole, two_cuts])
print(f"\n-> Wycentrowany układ płytek. \nPotrzebnych {len(whole) + 1} całych płytek na 1 rząd.\n")
print(result_centr)
print('\n-------------------------------------')
print(f'\n-> Rząd płytek z całą na początku.\nPotrzebnych {len(whole) + 1} całych płytek na 1 rząd.\n')
print(result_whole)