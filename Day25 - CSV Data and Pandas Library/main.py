import pandas

data = pandas.read_csv("squirrel_count_original.csv")

fur_list = data["Primary Fur Color"].to_list()

red_count = fur_list.count("Cinnamon")
black_count = fur_list.count("Black")
grey_count = fur_list.count("Gray")

new_file = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

squirrel_count = pandas.DataFrame(new_file)
squirrel_count = squirrel_count.to_csv("squirrel_count.csv")

# INNA METODA
# bierzemy liczymy wszystkie wiersze gdzie wystepuje dany kolor
# Reszta jest tak samo
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
