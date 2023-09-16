| Операція в Excel                        | Еквівалент в Pandas                           |
| --------------------------------------- | --------------------------------------------- |
| Відкрити файл Excel                     | `pd.read_excel('file.xlsx')`                  |
| Відкрити файл CSV                       | `pd.read_csv('file.csv')`                     |
| Експорт в Excel                         | `df.to_excel('output.xlsx', index=False)`     |
| Експорт у CSV                           | `df.to_csv('output.csv', index=False)`        |
| Експорт у JSON                          | `df.to_json('data.json')`                     |
| Вибір стовпця                           | `df['ColumnName']`                            |
| Вибір декількох стовпців                | `df[['Column1', 'Column2']]`                  |
| Фільтрація рядків                       | `df[df['Column'] > 5]`                        |
| Сортування за стовпцем                  | `df.sort_values(by='Column')`                 |
| Групування за стовпцем                  | `df.groupby('Column').mean()`                 |
| Обчислення середнього значення          | `df['Column'].mean()`                         |
| Перейменування стовпця                  | `df.rename(columns={'OldName': 'NewName'})`   |
| Додавання нового стовпця                | `df['NewColumn'] = ...`                       |
| Видалення стовпця                       | `df.drop('Column', axis=1)`                   |
| Видалення стовпця за індексом           | `df.drop(columns=['Column'])`                 |
| Застосування функції до стовпця         | `df['Column'].apply(func)`                    |
| Отримання списку унікальних значень     | `df['Column'].unique()`                       |
| Підрахунок унікальних значень у стовпці | `df['Column'].nunique()`                      |
| Об'єднання двох DataFrame               | `pd.concat([df1, df2])`                       |
| Об'єднання за ключем (аналог SQL JOIN)  | `pd.merge(df1, df2, on='KeyColumn')`          |
| Заповнення пропусків                    | `df.fillna(value)`                            |
| Видалення дублікатів                    | `df.drop_duplicates()`                        |
| Видалення рядків за індексом            | `df.drop(index)`                              |
| Робота з датами (парсинг, форматування) | `pd.to_datetime(df['Date'])`                  |
| Фільтрація за кількома умовами          | `df[(df['Condition1']) & (df['Condition2'])]` |
| Створення категоріальних даних          | `pd.Categorical(df['Column'])`                |
| Зміна типу даних стовпця                | `df['Column'].astype('dtype')`                |
| Підсумовування за групами з умовою      | `df.groupby('Group')['Column'].sum()`         |
