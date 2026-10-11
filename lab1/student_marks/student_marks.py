import os

# --- Зчитати файли ---
directory = '.' # Поточна директорія
required_files = ['math.txt', 'statistics.txt', 'physics.txt', 'student_names.txt']

# Перевіряємо, чи є всі файли
missing_files = []
for req_file in required_files:
    if req_file not in os.listdir(directory):
        missing_files.append(req_file)

if len(missing_files) > 0:
    print("Не знайдено файли:", missing_files)
else:
    raw_data = {}
    
    # Проходимо по файлах у директорії
    for filename in os.listdir(directory):
        if filename in required_files:
            file = open(filename, 'r', encoding='utf-8')
            
            lines = []
            for line in file:
                lines.append(line.strip()) # прибираємо зайві пробіли/перенесення рядків
                
            file.close() # Закриваємо файл
            
            # Якщо це файл з іменами - просто зберігаємо
            if filename == 'student_names.txt':
                raw_data['names'] = lines
            else:
                # Відкидаємо txt з назви, щоб отримати назву предмету
                subject = filename.replace('.txt', '')
                
                # Перетворюємо оцінки у цілі числа
                grades = []
                for line in lines:
                    grades.append(int(line))
                
                raw_data[subject] = grades

    # --- Обробка даних ---
    student_names = raw_data['names']
    subjects = ['math', 'statistics', 'physics']
    
    students_dict = {}
    
    # Заповнюємо словник
    for i in range(len(student_names)):
        student = student_names[i]
        students_dict[student] = {}
        
        for subj in subjects:
            students_dict[student][subj] = raw_data[subj][i]

    # --- Виведення результатів ---
    # Рахуємо середні оцінки
    student_averages = {}
    for student in students_dict:
        grades_dict = students_dict[student]
        
        total_score = 0
        count = 0
        for subj in grades_dict:
            total_score += grades_dict[subj]
            count += 1
            
        avg_score = total_score / count
        student_averages[student] = avg_score

    print("--- Статистика для кожного студента ---")
    for student in student_averages:
        avg = student_averages[student]
        print("студент:", student, ", середня оцінка:", round(avg, 2))

    print("\n--- Три студенти з найвищими середніми оцінками ---")
    # Робимо пошук максимуму 3 рази
    temp_averages = {}
    for student in student_averages:
        temp_averages[student] = student_averages[student]
        
    for i in range(3):
        best_student = None
        best_avg = -1
        
        # Шукаємо максимальне значення
        for student in temp_averages:
            avg = temp_averages[student]
            if avg > best_avg:
                best_avg = avg
                best_student = student
                
        if best_student != None:
            print(best_student)
            # Видаляємо знайденого, щоб наступного разу знайти наступного за ним
            del temp_averages[best_student]

    print("\n--- Загальна статистика ---")
    total_students = len(student_names)
    print("Загальна кількість студентів:", total_students)
    
    for subj in subjects:
        subj_grades = raw_data[subj]
        
        # Шукаємо суму, мінімум і максимум циклом
        total_subj_score = 0
        min_grade = float('inf')
        max_grade = -1
        
        for grade in subj_grades:
            total_subj_score += grade
            
            if grade > max_grade:
                max_grade = grade
            if grade < min_grade:
                min_grade = grade
                
        subj_avg = total_subj_score / total_students
        print("предмет:", subj, ", середня оцінка", round(subj_avg, 2), ", min оцінка:", min_grade, ", max оцінка:", max_grade)

    print("\n--- Найвищий бал по предметах ---")
    for subj in subjects:
        top_student = None
        top_grade = -1
        
        for student in students_dict:
            grade = students_dict[student][subj]
            if grade > top_grade:
                top_grade = grade
                top_student = student
                
        print("Предмет:", subj, "| студент:", top_student, ", оцінка:", top_grade)

    print("\n--- Студенти з середньою оцінкою нижче 50 ---")
    struggling_students = []
    
    for student in student_averages:
        avg = student_averages[student]
        if avg < 50:
            struggling_students.append(student)
            
    print("Кількість студентів з оцінкою нижче 50:", len(struggling_students))
    for student in struggling_students:
        print(student)