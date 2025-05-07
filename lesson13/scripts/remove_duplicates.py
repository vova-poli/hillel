import pandas as pd

def remove_duplicates_from_csv(file1, file2, output_file):
    # Зчитування даних з обох файлів
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Об'єднання датафреймів
    combined_df = pd.concat([df1, df2], ignore_index=True)

    # Видалення дублікатів
    unique_df = combined_df.drop_duplicates()

    # Збереження результату
    unique_df.to_csv(output_file, index=False)
    print(f"Результат збережено у файл: {output_file}")

# Виклик функції з конкретними шляхами
remove_duplicates_from_csv(
    "../ideas_for_test/work_with_csv/r-m-c.csv",
    "../ideas_for_test/work_with_csv/random-michaels.csv",
    "../ideas_for_test/work_with_csv/result_Polishchuk.csv"
)
