import Project

def main():
    try:
        Project.execute()
        Project.project.run(debug=True)
    except Exception as e:
        print(f"Помилка {e}")

if __name__ == "__main__":
    main()
    

    
