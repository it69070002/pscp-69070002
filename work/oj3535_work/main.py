"""3535"""
def main():
    """main"""
    data = []
    while True:
        text = input().strip()
        if text == "END":
            break
        year = text[:2]
        faculty = int(text[2:4])
        data.append((year, faculty))
    years = sorted({item[0] for item in data})
    for year in years:
        faculties = sorted({item[1] for item in data if item[0] == year})
        is_first = True
        for faculty in faculties:
            count = data.count((year, faculty))
            if is_first:
                print(f"{year} {faculty} {count}")
                is_first = False
            else:
                print(f"-- {faculty} {count}")
main()
