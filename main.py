import sqlizer
sqlizer.config.API_KEY = 'RYODRkbxduXNV4WQ4yYDjrRKL6mUxQmsxmctb6LmsYblVs9hMY8qqR6d5bkYQ2QVMHp3EFLSDC5zZUseM2A'
with open('Book9.xlsx', mode='rb') as file_content:
    converter = sqlizer.File(file_content, sqlizer.DatabaseType.MySQL, sqlizer.FileType.XLSX, 'example.xlsx', 'my_table')
    converter.convert(wait=True)
    with open('result.sql', mode='w') as result_file:
        result_file.write(converter.download_result_file().text)