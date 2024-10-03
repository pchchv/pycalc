from flet import (
    app, colors, border_radius, Page, ElevatedButton, Row,
    TextField, TextAlign, TextStyle, Container, Column
)


def main(page: Page):
    page.title = "Calculator"
    result = TextField(
        hint_text='0', text_size=20,
        color='white', text_align=TextAlign.RIGHT,
        hint_style=TextStyle(
            color=colors.WHITE, size=20
        ),
        read_only=True
    )

    def button_click(e):
        if e.control.text == "=":
            try:
                result.value = str(eval(result.value))
            except Exception:
                result.value = "Error"
        elif e.control.text == "C":
            result.value = ""
        else:
            result.value += e.control.text
        result.update()

    button_row0 = Row(
        [
            ElevatedButton(text='C', expand=1, on_click=button_click,
                           bgcolor=colors.RED_ACCENT, color=colors.WHITE),
            ElevatedButton(text='^', expand=1, on_click=button_click,
                           bgcolor=colors.BLUE_ACCENT_100,
                           color=colors.RED_900
                           ),
            ElevatedButton(text='%', expand=1, on_click=button_click,
                           bgcolor=colors.BLUE_ACCENT_100,
                           color=colors.RED_900
                           ),
            ElevatedButton(text='/', expand=1, on_click=button_click,
                           bgcolor=colors.BLUE_ACCENT_100,
                           color=colors.RED_900
                           ),
        ]
    )
    button_row1 = Row(
        [
            ElevatedButton(text='7', expand=1, on_click=button_click),
            ElevatedButton(text='8', expand=1, on_click=button_click),
            ElevatedButton(text='9', expand=1, on_click=button_click),
            ElevatedButton(text='*', expand=1, on_click=button_click,
                           bgcolor=colors.BLUE_ACCENT_100,
                           color=colors.RED_900
                           ),
        ]
    )
    button_row2 = Row(
        [
            ElevatedButton(text='4', expand=1, on_click=button_click),
            ElevatedButton(text='5', expand=1, on_click=button_click),
            ElevatedButton(text='6', expand=1, on_click=button_click),
            ElevatedButton(text='-', expand=1, on_click=button_click,
                           bgcolor=colors.BLUE_ACCENT_100
                           ),
        ]
    )
    button_row3 = Row(
        [
            ElevatedButton(text='1', expand=1, on_click=button_click),
            ElevatedButton(text='2', expand=1, on_click=button_click),
            ElevatedButton(text='3', expand=1, on_click=button_click),
            ElevatedButton(text='+', expand=1, on_click=button_click,
                           bgcolor=colors.BLUE_ACCENT_100,
                           color=colors.RED_900),
        ]
    )
    button_row4 = Row(
        [
            ElevatedButton(text='0', expand=1, on_click=button_click),
            ElevatedButton(text='.', expand=1, on_click=button_click),
            ElevatedButton(text='=', expand=2, on_click=button_click,
                           bgcolor=colors.GREEN_ACCENT, color=colors.AMBER
                           ),
        ]
    )
    container = Container(
        width=350, padding=20,
        bgcolor=colors.BLACK, border_radius=border_radius.all(20),
        content=Column(
            [
                result,
                button_row0, button_row1, button_row2,
                button_row3, button_row4
            ]
        )
    )
    page.add(container)


if __name__ == '__main__':
    app(target=main)
