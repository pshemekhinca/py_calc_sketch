#! /home/peha/Desktop/tempProjects/01/venv/bin/python
tile_size = int(input("Tile width: "))
room_length = int(input("Room length: "))
grout = input("Grout width: ")

# div_result = int(room_length) / int(tile_size)
# sides_cuts = str((room_length % tile_size) / 2)
# whole_tiles = str(tile_size).split() * int(div_result)
# print(sides_cuts, whole_tiles, sides_cuts)
# print('| ]', '[ ]'*int(div_result), '[ |')
# print()
# div_result = int(room_length) / int(tile_size)
# sides_cuts = str((room_length % tile_size) / 2)
# whole_tiles = str(tile_size).split() * int(room_length / tile_size)
# horizontal = grout.join([sides_cuts, *whole_tiles, sides_cuts])
# print(horizontal)

# print('| ]', '[ ]'*int(div_result), '[ |')
# print()

section = 180
length_to_divide: int = 2150
interject: int = "  3  "

cut_side = str((room_length % tile_size) / 2)
tiles_ncut = int(room_length / tile_size)
whole = str(tile_size).split() * int(room_length / tile_size)
grout_sum = int(interject * (tiles_ncut + 1))
print(f"Suma fug {len(grout_sum) * interject}")
result = interject.join([cut_side, *whole, cut_side])
print(result)
# if (float(cut_side) > (float(tile_size) / 2)):
#     print(f"Ilość płytek w rzędzie {whole +2}")
# else:
#     print(f"Ilość płytek w rzędzie {whole +1}")


