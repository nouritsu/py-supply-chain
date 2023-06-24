import flet as ft
import time
from game import Game

def main(page: ft.Page):
    page.title = "Py Supply Chain"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 675
    page.window_width = 440

    GAME = Game(2)
    role = ft.Text(size=20)
    game_round = ft.Text(size=20)
    orders_placed = ft.Column()
    orders_received = ft.Column()
    orders_fulfilled = ft.Column()
    role_stats = ft.Text("", size=16)

    def init():
        role.value = "Customer"
        game_round.value = 1
        role_stats.value = "Production: NA  |  Stock: NA"

    def to_num_str(num: int, length: int):
        while len(str(num)) < length:
            num = f"0{num}"
        return str(num)

    def command_submit(e: ft.ControlEvent):
        nonlocal GAME

        command = e.control.value
        result = GAME.execute(command)
        command_textfield.error_text = ""
        print(command)

        if result.is_err():
            print(result.err())
            command_textfield.error_text = result.err()

            if result.err() == "Exit":
                raise SystemExit from None
            
        stats = GAME.current.stats()
        
        def update_orders(order_dict: str, column: ft.Column):
            if not order_dict in stats or not len(stats[order_dict]):
                return None

            orders = stats[order_dict]
            rows = []
            for k, v in orders.items():
                if type(v) == dict:
                    v = f"{v['count']} round {v['week']}"
                row = ft.Text(f"{to_num_str(k, 4)}×{to_num_str(v, 2)}", size=15)
                rows.append(row)

            column.controls = rows

        if role.value != stats["role"]:
            role.value = stats["role"]
            orders_placed.controls = []
            orders_received.controls = []
            orders_fulfilled.controls = []
    
        prod_stats = stats["production"] if "production" in stats else "NA"
        stock_stats = stats["stock"] if "stock" in stats else "NA"
        role_stats.value = f"Production: {prod_stats}  |  Stock: {stock_stats}"

        update_orders("placed-orders", orders_placed)
        update_orders("received-orders", orders_received)
        update_orders("fulfilled-orders", orders_fulfilled)

        game_round.value = stats["round"]

        page.update()
    
    command_textfield = ft.TextField(label="Command", on_submit=command_submit)
    init()

    page.padding = 45
    page.add(
        ft.Column([

            ft.Row([

                ft.Column([
                    ft.Row([
                        ft.Icon(name=ft.icons.PERSON_2_ROUNDED),
                        ft.Text("ROLE", size=15, weight=ft.FontWeight.BOLD),
                    ]),
                    role,
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),

                ft.Column([
                    ft.Row([
                        ft.Icon(name=ft.icons.NEXT_PLAN_ROUNDED),
                        ft.Text("ROUND", size=15, weight=ft.FontWeight.BOLD),
                    ]),
                    game_round,
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),

            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            ft.Row([
                ft.Column([
                    ft.Row([
                        ft.Icon(ft.icons.SHOPPING_CART_ROUNDED),
                        ft.Text("PLACED", weight=ft.FontWeight.W_600)
                        ]),
                    orders_placed
                ], ),
                ft.Column([
                    ft.Row([
                        ft.Icon(ft.icons.INVENTORY_2_ROUNDED),
                        ft.Text("RECEIVED", weight=ft.FontWeight.W_600)
                        ]),
                    orders_received
                ]),
                ft.Column([
                    ft.Row([
                        ft.Icon(ft.icons.INVENTORY_ROUNDED),
                        ft.Text("FULFILLED", weight=ft.FontWeight.W_600)
                        ]),
                    orders_fulfilled
                ]),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, height=page.height/2.5),

            ft.Row([
                ft.Text("STATISTICS:", size=15, weight=ft.FontWeight.BOLD),
                role_stats
            ]),

            command_textfield
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, height=page.height/1.25)
    )

ft.app(target=main)