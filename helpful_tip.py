from jinja2 import Environment
CONFIG_TEMPLATE = """
you name {{ name | lower }}\ndescription {{ description | upper }}\nvolume {% if x == "y" %}z {% elif x == "w" %}k {% elif x == "i" %}o
{% else %}sss {% endif %}\nendtemplate
"""
env = Environment(
    keep_trailing_newline=True
)
OUTPUT_FILE = "helpful_tip.txt"
def generate_config(name, description, x):
    template = env.from_string(CONFIG_TEMPLATE)
    return template.render(name=name, description=description, x=x
    )
def main():
    while True:
        print("\n===Генератор конфига===\n")
        name = input("Введите имя:").strip()
        description = input("Введите описание:").strip()
        x = input("Выбрать X, варианты y / w / i :").strip().lower()
        config = generate_config(name, description, x)
        print("\n" + "=" * 50)
        print("ГОТОВО")
        print("=" * 50)
        print(config)
        print("=" * 50)
        answer = input("\nСохранить?(да,нет): ").strip().lower()
        if answer in ("да"):
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(config)
            print(f"\nСохранено")
            input("Нажмите Enter")
            break
        else:
            print("\nВозврат в меню\n")
if __name__ == "__main__":
    main()
