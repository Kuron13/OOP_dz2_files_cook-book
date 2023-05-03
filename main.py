from pprint import pprint
def recipes_read():
    cook_book = {}
    with open('Recipes.txt', 'rt', encoding='utf-8') as recipes_file:
        for line in recipes_file:
            recipe_name = line.strip()
            quantity_ingr = int(recipes_file.readline())
            ingredients = []
            for i in range(quantity_ingr):
                ingr_info = recipes_file.readline().strip().split(' | ')
                ingr_dict = {'ingredient_name' : ingr_info[0], 'quantity' : ingr_info[1], 'measure' : ingr_info[2]}
                ingredients.append(ingr_dict)
            cook_book.setdefault(recipe_name, ingredients)
            recipes_file.readline()
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    book = recipes_read()
    shop = {}
    for i in dishes:
        for ingr in book[i]:
            if ingr['ingredient_name'] in shop.keys():
                shop['ingredient_name']['quantity'] += ingr['quantity']
            else:
                shop.setdefault(ingr['ingredient_name'], {'quantity' : int(ingr['quantity'])*person_count, 'measure' : ingr['measure']})
    return shop

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))