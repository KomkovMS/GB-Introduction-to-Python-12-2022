# Условие: дана строка: "Первые 5 мест на соревнованиях: 1. иванов 2. петров
# 3. сидоров 4. орлов 5. соколов"

# Результат - позравляем 1-ые 3 места:
# "Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!"


str_res = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. \
    орлов 5. соколов'

start = str_res.find('1')
end = str_res.find('4')
print(f'Поздравляем {str_res[start:end].upper()} с успехом!')
