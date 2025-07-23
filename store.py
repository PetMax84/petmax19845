class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # словарь {название_товара: цена}

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент"""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}'")

    def remove_item(self, item_name):
        """Удаление товара из ассортимента"""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте")

    def get_item_price(self, item_name):
        """Получение цены товара по названию"""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновление цены товара"""
        if item_name in self.items:
            old_price = self.items[item_name]
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' изменена с {old_price} на {new_price}")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте")

    def display_items(self):
        """Отображение всех товаров магазина"""
        print(f"\nАссортимент магазина '{self.name}' по адресу {self.address}:")
        if not self.items:
            print("Ассортимент пуст")
        else:
            for item_name, price in self.items.items():
                print(f"  {item_name}: {price} руб.")