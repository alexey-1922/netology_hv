from pprint import pprint
with open('recipes', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            ingr, quant, meas = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingr, 'quantity': quant, 'measure': meas})
        file.readline()
        cook_book[dish_name] = ingredients  
    
    def get_shop_list_by_dishes(dishes, person_count):  
        result = {}
        for key in dishes:
            for res_dict in cook_book[key]:
                nested_dict = {}
                if res_dict['ingredient_name'] not in result.keys():
                    nested_dict['measure'] = res_dict['measure']
                    nested_dict['quantity'] = int(res_dict['quantity']) * person_count
                    result[res_dict['ingredient_name']] = nested_dict
                else:
                    nested_dict = result[res_dict['ingredient_name']]
                    nested_dict['quantity'] += int(res_dict['quantity']) * person_count
                           
        return result                     
if __name__ == '__main__':
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    