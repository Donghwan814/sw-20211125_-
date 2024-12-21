import random
import string

# 학생 정보 생성 함수
def generate_student_data(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 두 글자 알파벳
        age = random.randint(18, 22)  # 18~22 사이의 나이
        grade = random.randint(0, 100)  # 0~100 사이의 성적
        students.append({"이름": name, "나이": age, "성적": grade})
    return students

# 선택 정렬
def selection_sort(students, key):
    n = len(students)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][key] < students[min_idx][key]:
                min_idx = j
        # Swap
        students[i], students[min_idx] = students[min_idx], students[i]
        print(f"Step {i + 1}: {students}")  # 단계별 출력

# 삽입 정렬
def insertion_sort(students, key):
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and students[j][key] > current[key]:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current
        print(f"Step {i}: {students}")  # 단계별 출력

# 퀵 정렬
def quick_sort(students, key):
    def partition(arr, low, high):
        pivot = arr[high][key]
        i = low - 1
        for j in range(low, high):
            if arr[j][key] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    _quick_sort(students, 0, len(students) - 1)
    print(f"Sorted students: {students}")

# 기수 정렬
def counting_sort(arr, key, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for student in arr:
        index = student[key] // exp % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i][key] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(students, key):
    max_grade = max(students, key=lambda x: x[key])[key]
    exp = 1
    while max_grade // exp > 0:
        counting_sort(students, key, exp)
        exp *= 10
    print(f"Sorted students by grade: {students}")

# 메뉴 출력 함수
def print_menu():
    print("1. 이름 기준으로 정렬")
    print("2. 나이 기준으로 정렬")
    print("3. 성적 기준으로 정렬")
    print("4. 프로그램 종료")

# 학생 정렬 처리 함수
def sort_students():
    students = generate_student_data()
    
    # 학생 정보 먼저 출력
    print("현재 학생 목록:")
    for student in students:
        print(student)
    
    while True:
        print_menu()
        choice = int(input("정렬 기준을 선택하세요 (1, 2, 3, 4): "))
        
        if choice == 1:
            print("이름 기준으로 정렬을 선택했습니다.")
            sort_key = "이름"
        elif choice == 2:
            print("나이 기준으로 정렬을 선택했습니다.")
            sort_key = "나이"
        elif choice == 3:
            print("성적 기준으로 정렬을 선택했습니다.")
            sort_key = "성적"
        elif choice == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        
        print("정렬 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬")
        algorithm_choice = int(input("알고리즘 선택: "))
        
        if algorithm_choice == 1:
            selection_sort(students, sort_key)
        elif algorithm_choice == 2:
            insertion_sort(students, sort_key)
        elif algorithm_choice == 3:
            quick_sort(students, sort_key)
        elif algorithm_choice == 4 and sort_key == "성적":
            radix_sort(students, sort_key)
        else:
            print("기수 정렬은 성적 기준으로만 가능합니다.")
            continue
        
        print("정렬된 학생 정보:")
        for student in students:
            print(student)

# 메인 실행
if __name__ == "__main__":
    sort_students()