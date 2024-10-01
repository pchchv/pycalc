from flet import ( app, colors, Page, ElevatedButton, Row, TextField, TextAlign, TextStyle )


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
        pass

    button_row0 = Row(
        [
            ElevatedButton(text='C',  on_click=button_click),
            ElevatedButton(text='^',  on_click=button_click),
            ElevatedButton(text='%',  on_click=button_click),
            ElevatedButton(text='/',  on_click=button_click),
        ]
    )
    button_row1 = Row(
        [
            ElevatedButton(text='7',  on_click=button_click),
            ElevatedButton(text='8',  on_click=button_click),
            ElevatedButton(text='9',  on_click=button_click),
            ElevatedButton(text='*',  on_click=button_click),
        ]
    )
    button_row2 = Row(
        [
            ElevatedButton(text='4',  on_click=button_click),
            ElevatedButton(text='5',  on_click=button_click),
            ElevatedButton(text='6',  on_click=button_click),
            ElevatedButton(text='-',  on_click=button_click),
        ]
    )
    button_row3 = Row(
        [
            ElevatedButton(text='1',  on_click=button_click),
            ElevatedButton(text='2',  on_click=button_click),
            ElevatedButton(text='3',  on_click=button_click),
            ElevatedButton(text='+',  on_click=button_click),
        ]
    )
    button_row4 = Row(
        [
            ElevatedButton(text='0',  on_click=button_click),
            ElevatedButton(text='.',  on_click=button_click),
            ElevatedButton(text='=',  on_click=button_click),
        ]
    )


if __name__ == '__main__':
    app(target=main)
