from task_manager import TaskManager
from store import Store


def demonstrate_task_manager():
    print("=== Демонстрация работы с задачами ===")
    task_manager = TaskManager()

    # Добавляем задачи
    task_manager.add_task("Купить продукты", "2024-01-15")
    task_manager.add_task("Закончить отчет", "2024-01-20")
    task_manager.add_task("Позвонить врачу", "2024-01-12")

    print("Все текущие задачи:")
    task_manager.print_current_tasks()

    # Отмечаем одну задачу как выполненную
    task_manager.mark_task_completed(0)

    print("\nПосле выполнения одной задачи:")
    task_manager.print_current_tasks()

    print("\n" + "=" * 50 + "\n")


def demonstrate_stores():
    print("=== Демонстрация работы с магазинами ===")

    # Создаем магазины
    store1 = Store("Продукты у дома", "ул. Ленина, 10")
    store2 = Store("Электроника", "пр. Победы, 45")
    store3 = Store("Книжный мир", "ул. Гагарина, 12")

    # Добавляем товары в первый магазин
    store1.add_item("Яблоки", 80.0)
    store1.add_item("Бананы", 60.0)
    store1.add_item("Хлеб", 30.0)
    store1.add_item("Молоко", 70.0)

    # Добавляем товары во второй магазин
    store2.add_item("Смартфон", 25000.0)
    store2.add_item("Наушники", 3500.0)
    store2.add_item("Чехол", 500.0)

    # Добавляем товары в третий магазин
    store3.add_item("Роман", 400.0)
    store3.add_item("Учебник", 800.0)
    store3.add_item("Журнал", 150.0)

    # Отображаем ассортимент всех магазинов
    store1.display_items()
    store2.display_items()
    store3.display_items()

    print("\n" + "=" * 50 + "\n")
    print("=== Тестирование методов магазина 'Продукты у дома' ===")

    # Тестирование методов на первом магазине
    test_store = store1

    # Получаем цену товара
    apple_price = test_store.get_item_price("Яблоки")
    print(f"Цена яблок: {apple_price} руб.")

    # Получаем цену несуществующего товара
    orange_price = test_store.get_item_price("Апельсины")
    print(f"Цена апельсинов: {orange_price}")  # Должно быть None

    # Обновляем цену товара
    test_store.update_item_price("Бананы", 65.0)

    # Пытаемся обновить цену несуществующего товара
    test_store.update_item_price("Апельсины", 70.0)

    # Удаляем товар
    test_store.remove_item("Хлеб")

    # Пытаемся удалить несуществующий товар
    test_store.remove_item("Хлеб")  # Товар уже удален

    # Отображаем обновленный ассортимент
    test_store.display_items()

    # Добавляем новый товар
    test_store.add_item("Груши", 90.0)
    test_store.display_items()


if __name__ == "__main__":
    demonstrate_task_manager()
    demonstrate_stores()