def check_input(user_input, allowed_list):
    while user_input not in allowed_list:

        output_string = 'Должно быть '

        for element in allowed_list[:-1]:
            output_string += f'{element}, '
        
        output_string = f'{output_string[:-2]} или {allowed_list[-1]}.'

            
        print(output_string)
        user_input = input('Попробуй ещё раз:\n')

    return user_input