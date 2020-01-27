input_list = [[1,2,3,4],[0,2,6],[0,1,3],[0,2,4,7],[0,3,5,7],[4,6,7],[1,5],[3,5]]

def find_parent(input_list, starting_val):
    layers = [[starting_val]]
    seen_nodes = {starting_val,}
    while True:
        previous_layer = layers[-1]
        current_layer = []
        for layer in previous_layer:
            possible_vals_in_layer = input_list[layer]
            current_layer.extend(possible_vals_in_layer)
        append_list = []
        continue_layering = False
        for node in current_layer:
            if node not in seen_nodes:
                append_list.append(node)
                continue_layering = True
                seen_nodes.add(node)
        if continue_layering:
            layers.append(append_list)
        else:
            break

    return_arr = [None]*len(input_list)
    left_pointer = -1
    right_pointer = 0
    while(right_pointer < len(layers)):
        if left_pointer < 0:
            for val in layers[right_pointer]:
                return_arr[val] = layers[right_pointer]
        else:
            for right_val in layers[right_pointer]:
                append_list = []
                for left_val in layers[left_pointer]:
                    if left_val in input_list[right_val]:
                        append_list.append(left_val)
                return_arr[right_val] = append_list
        left_pointer+=1
        right_pointer+=1


    return (return_arr)
print(find_parent(input_list, 0))
