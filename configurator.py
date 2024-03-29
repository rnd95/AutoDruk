def create_configurator(file_path):
    def configurator(**kwargs):
        params = {}
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    params[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"File {file_path} not found, using default parameters.")

        params.update(kwargs)
        return params
    return configurator

# Пример использования
config_file = 'config.txt'
configurator = create_configurator(config_file)

# Изменение параметров
new_params = configurator(param1=200, param3='new_value')

print(new_params)

